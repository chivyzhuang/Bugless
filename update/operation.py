# -*- coding: utf-8 -*-
import updatemessage_pb2
from bsdiff.models import ApkPackage, Patch
from django.core.urlresolvers import reverse


def check_update(message):
    # get ask object
    ask = updatemessage_pb2.Ask()
    ask.ParseFromString(message)
    # query and answer
    answer = updatemessage_pb2.Answer()
    try:
        apk_list = ApkPackage.objects.filter(package_name=ask.package_name).order_by('-version_code')
        if len(apk_list) > 0:
            for xapk in apk_list:
                if xapk.is_published:
                    apk = xapk
                    break;
            if not apk:
                answer.has_update = False
                return answer.SerializeToString()
        else:
            answer.has_update = False
            return answer.SerializeToString()
    except ApkPackage.DoesNotExist:
        answer.has_update = False
        return answer.SerializeToString()
    if ask.version_code < apk.version_code:
        # 还没有发布
        if not apk.is_published:
            answer.has_update = False
            return answer.SerializeToString()
        # 已经发布，可供下载
        answer.has_update = True
        try:
            pre_apk = ApkPackage.objects.get(package_name=ask.package_name, version_code=ask.version_code)
            answer.pre_apk_md5 = pre_apk.file_md5
        except ApkPackage.DoesNotExist:
            answer.has_update = False
            return answer.SerializeToString()
        # 更新apk地址及apk的md5
        answer.apk_url = reverse(
                    'download:get_apk', 
                    args = [
                        apk.package_name,
                        apk.version_code
                        ]
                    )
        answer.apk_md5 = apk.file_md5
        # 如果可以增量更新，填充patch的url地址
        try:
            patch = apk.patch_set.get(pre_version_code=ask.version_code)
            answer.patch_url = reverse(
                'download:get_patch',
                args = [
                    apk.package_name,
                    '%s_%s' % (patch.pre_version_code, apk.version_code)
                    ]
                )
            answer.patch_md5 = patch.file_md5
        except Patch.DoesNotExist:
            pass
        return answer.SerializeToString()
    else:
        answer.has_update = False
        return answer.SerializeToString()
