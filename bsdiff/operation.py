# -*e coding: utf-8 -*-
import bsdiff4
from bsdiff.models import ApkPackage, Patch, ApkMark
from gfunction.operation import get_apk_path, get_patch_path, get_file_md5


def check_if_apk_valid(package_name, version_code):
    if version_code <= 0:
        return False, '应用的版本号必须大于0'
    try:
        mark = ApkMark.objects.get(package_name=package_name)
    except ApkMark.DoesNotExist:
        return False, '你还没有添加这个应用'
    if mark.version_code <= version_code:
        return True, ''
    return False, '应用的新版本必须大于或等于目前最新版本号(%d)' % mark.version_code


def update_apk_mark(package_name, version_code):
    try:
        mark = ApkMark.objects.get(package_name=package_name)
        mark.version_code = version_code
        mark.save()
        return mark
    except ApkMark.DoesNotExist:
        return ApkMark.objects.create(
                package_name=package_name,
                version_code=version_code
                )


def handle_uploaded_apk_file(f, package_name, version_code):
    # find record in db or create it if the record does not exist
    is_replace = True
    try:
        apk_pkg = ApkPackage.objects.get(
                package_name=package_name,
                version_code=version_code
        )
    except ApkPackage.DoesNotExist:
        is_replace = False
        apk_pkg = ApkPackage.objects.create(
                package_name=package_name,
                version_code=version_code,
                target_mark=update_apk_mark(package_name, version_code),
        )
    # write the file
    apk_pkg.file_path = get_apk_path(package_name, version_code)
    with open(apk_pkg.file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    destination.close()
    # get md5
    apk_pkg.file_md5 = get_file_md5(apk_pkg.file_path)
    # update mark
    apk_pkg.save()
    # generate patch
    generate_patch(apk_pkg, is_replace)


def generate_patch(apk_pkg, is_replace):
    # find the list of apks that have the same pkg_name
    # except the newest one.
    apk_list = ApkPackage.objects.filter(
            package_name=apk_pkg.package_name,
            ).order_by('-version_code')[1:]
    # first apk, now out
    if not apk_list:
        return
    # delete all old patch files
    if is_replace:
        delete_list = apk_pkg.patch_set.all()
    else:
        delete_list = apk_list[0].patch_set.all()
    for patch in delete_list:
        patch.delete()
    # generate patch file for each pre apk file
    for pre_apk in apk_list:
        # generate patch file
        patch_file_path = get_patch(
                apk_pkg.package_name,
                pre_apk.version_code,
                apk_pkg.version_code,
                apk_pkg.file_path
                )
        # create record
        Patch.objects.create(
                file_path=patch_file_path,
                file_md5=get_file_md5(patch_file_path),
                pre_version_code=pre_apk.version_code,
                target_apk=apk_pkg
                )


# return patch file path
def get_patch(
        package_name,
        pre_version_code,
        version_code,
        new_file_path):
    # generate patch
    old_file_path = get_apk_path(package_name, pre_version_code)
    patch_file_path = get_patch_path(package_name, pre_version_code, version_code)
    bsdiff4.file_diff(old_file_path, new_file_path, patch_file_path)
    return patch_file_path
