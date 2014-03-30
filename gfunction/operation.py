def get_apk_dir_path(package_name):
	return 'media/apk/%s' % (package_name)


def get_patch_dir_path(package_name):
	return 'media/patch/%s' % (package_name)
	

def get_apk_path(package_name, version_code):
	return 'media/apk/%s/%s.apk' % (package_name, version_code)


def get_patch_path(package_name, pre_version_code, version_code):
	return 'media/patch/%s/%s_%s' % (package_name, pre_version_code, version_code)