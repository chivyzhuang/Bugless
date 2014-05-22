# -*e coding: utf-8 -*-
from bugreceiver.models import JavaBug, NativeBug
from bugfix.models import FixPackage
from gfunction.operation import generate_java_repair_path, generate_native_repair_path, get_file_md5


def handle_remove_java_repair(pk):
    try:
        javaBug = JavaBug.objects.get(pk=pk)
    except JavaBug.DoesNotExist:
        return
    javaBug.is_fix = 'N'
    javaBug.repair_package.delete()
    javaBug.repair_package = None
    javaBug.is_repair_published = False
    javaBug.save()


def handle_remove_native_repair(pk):
    try:
        nativeBug = NativeBug.objects.get(pk=pk)
    except NativeBug.DoesNotExist:
        return
    nativeBug.is_fix = 'N'
    nativeBug.repair_package.delete()
    nativeBug.repair_package = None
    nativeBug.is_repair_published = False
    nativeBug.save()


def handle_remove_java_publish(pk):
    try:
        javaBug = JavaBug.objects.get(pk=pk)
    except JavaBug.DoesNotExist:
        return
    javaBug.is_repair_published = not javaBug.is_repair_published
    javaBug.save()


def handle_remove_native_publish(pk):
    try:
        nativeBug = NativeBug.objects.get(pk=pk)
    except NativeBug.DoesNotExist:
        return
    nativeBug.is_repair_published = not nativeBug.is_repair_published
    nativeBug.save()


def handle_uploaded_java_repair_file(f, pk, method, brief):
    try:
        javaBug = JavaBug.objects.get(pk=pk)
    except JavaBug.DoesNotExist:
        return '缺陷不存在'
    javaBug.is_fix = method
    if javaBug.repair_package == None:
        repair_package = FixPackage.objects.create()
        javaBug.repair_package = repair_package
    else:
        repair_package = javaBug.repair_package
    # write the file
    repair_package.file_path = generate_java_repair_path(pk)
    with open(repair_package.file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    destination.close()
    # get md5
    repair_package.file_md5 = get_file_md5(repair_package.file_path)
    # brief
    repair_package.brief = brief
    repair_package.save()
    javaBug.save()
    return None


def handle_uploaded_native_repair_file(f, pk, method, brief):
    try:
        nativeBug = NativeBug.objects.get(pk=pk)
    except NativeBug.DoesNotExist:
        return '缺陷不存在'
    nativeBug.is_fix = method
    if nativeBug.repair_package == None:
        repair_package = FixPackage.objects.create()
        nativeBug.repair_package = repair_package
    else:
        repair_package = nativeBug.repair_package
    # write the file
    repair_package.file_path = generate_native_repair_path(pk)
    with open(repair_package.file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    destination.close()
    # get md5
    repair_package.file_md5 = get_file_md5(repair_package.file_path)
    # brief
    repair_package.brief = brief
    repair_package.save()
    nativeBug.save()
    return None