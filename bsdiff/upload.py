import os
from bsdiff.util import bsdiff
from hashlib import md5
from bsdiff.models import ApkPackage, Patch, ApkMark


def check_if_apk_expired(package_name, version_code):
    try:
        mark = ApkMark.objects.get(pk=package_name)
    except ApkMark.DoesNotExist:
        return False
    return mark.version_code > version_code


def update_apk_mark(package_name, version_code):
    try:
        mark = ApkMark.objects.get(pk=package_name)
        mark.version_code = version_code
        mark.save()
    except ApkMark.DoesNotExist:
        ApkMark.objects.create(
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
                version_code=version_code
        )
    # mybe create dir
    dir_path = 'Storage/apk/%s' % (package_name)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    # write the file
    apk_pkg.file_path = 'Storage/apk/%s/%s.apk' %\
            (package_name, version_code)
    with open(apk_pkg.file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    destination.close()
    # get md5
    apk_pkg.file_md5 = get_file_md5(apk_pkg.file_path)
    apk_pkg.save()
    # update mark
    update_apk_mark(package_name, version_code)
    # generate patch
    generate_patch(apk_pkg, is_replace)


def get_file_md5(file_path):
    m = md5()
    src_file = open(file_path, 'rb')
    m.update(src_file.read())
    src_file.close()
    return m.hexdigest()


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
        patch_file = get_patch(
                apk_pkg.package_name,
                pre_apk.version_code,
                apk_pkg.version_code,
                apk_pkg.file_path
                )
        # create record
        Patch.objects.create(
                file_path=patch_file,
                file_md5=get_file_md5(patch_file),
                pre_version_code=pre_apk.version_code,
                target_apk=apk_pkg
                )


# return patch file path
def get_patch(
        package_name,
        pre_version_code,
        version_code,
        new_file):
    # mybe create dir
    dir_path = 'Storage/patch/%s' % (package_name)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    # generate patch
    old_file = 'Storage/apk/%s/%s.apk' %\
            (package_name, version_code)
    patch_file = 'Storage/patch/%s/%s_%s' %\
            (package_name, pre_version_code, version_code)
    bsdiff(old_file, new_file, patch_file)
    return patch_file
