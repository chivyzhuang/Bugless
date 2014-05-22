from download.operation import download_file
from gfunction.operation import get_apk_path, get_patch_path


def get_apk(request, pkg_name, f_name):
    return download_file(
            request,
            get_apk_path(pkg_name, f_name)
    )


def get_patch(request, pkg_name, f_name):
    return download_file(
            request,
            get_patch_path(pkg_name, f_name)
    )


def get_file(request, file_path):
	return download_file(request, file_path)