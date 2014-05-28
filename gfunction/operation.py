import os
from hashlib import md5
from time import gmtime, strftime


def get_apk_dir_path(package_name):
	dir_path = 'media/apk/%s_/' % (package_name)
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	return dir_path


def get_patch_dir_path(package_name):
	dir_path = 'media/patch/%s_/' % (package_name)
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	return dir_path


def get_java_repair_path():
	dir_path = 'media/repair/java/%s/' % strftime("%Y/%m/%d", gmtime())
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	return dir_path


def get_native_repair_path():
	dir_path = 'media/repair/native/%s/' % strftime("%Y/%m/%d", gmtime())
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	return dir_path


def generate_java_repair_path(pk):
	return get_java_repair_path() + pk


def generate_native_repair_path(pk):
	return get_native_repair_path() + pk


def get_apk_path(package_name, version_code):
	return get_apk_dir_path(package_name) + '%s.apk' % version_code


def get_patch_path(package_name, pre_version_code, version_code):
	return get_patch_dir_path(package_name) + '%s_%s' % (pre_version_code, version_code)


def get_file_md5(file_path):
    m = md5()
    src_file = open(file_path, 'rb')
    m.update(src_file.read())
    src_file.close()
    return m.hexdigest()