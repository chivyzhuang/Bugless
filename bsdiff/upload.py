import os
from bsdiff.util import bsdiff
from hashlib import md5
from bsdiff.models import ApkPackage, Patch


def handle_uploaded_apk_file(f, pkg_name, version_code):
    # find record in db or create it if the record does not exist
    is_replace = True
    try:
        apk_pkg = ApkPackage.objects.get(
                package_name=pkg_name,
                version_code=version_code
        )
    except ApkPackage.DoesNotExist:
        is_replace = False
        apk_pkg = ApkPackage.objects.create(
                package_name=pkg_name,
                version_code=version_code
        )
    # write the file
    apk_pkg.file_path = 'Storage/apk/%s_%s.apk' % (pkg_name, version_code)
    with open(apk_pkg.file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    destination.close()
    # get md5
    apk_pkg.file_md5 = get_file_md5(apk_pkg.file_path)
    apk_pkg.save()
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
    apk_list = ApkPackage.objects.\
            filter(package_name=apk_pkg.package_name).\
            order_by('-version_code')[1:]
    # delete all old patch files
    if not apk_list:
        return
    if is_replace:
        delete_list = apk_pkg.patch_set.all()
    else:
        delete_list = apk_list[0].patch_set.all()
    for patch in delete_list:
        try:
            os.remove(patch.file_path)
        except OSError:
            pass
        patch.delete()
    # generate patch file for each pre apk file
    for pre_apk in apk_list:
        # generate patch
        oldfile = 'Storage/apk/%s_%s.apk' %\
                (apk_pkg.package_name, pre_apk.version_code)
        patchfile = 'Storage/patch/%s_%s_%s' %\
                (apk_pkg.package_name, pre_apk.version_code, apk_pkg.version_code)
        bsdiff(oldfile, apk_pkg.file_path, patchfile)
        # create record
        new_patch = Patch.objects.create(
                file_path=patchfile,
                file_md5=get_file_md5(patchfile),
                pre_version_code=pre_apk.version_code,
                target_apk=apk_pkg
        )
        new_patch.save()
