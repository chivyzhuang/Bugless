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
        apk = ApkPackage.objects.filter(package_name=ask.package_name).\
                order_by('-version_code')[0]
    except ApkPackage.DoesNotExist:
        answer.has_update = False
        return answer.SerializeToString()
    if ask.version_code < apk.version_code:
        answer.has_update = True
        try:
            patch = apk.patch_set.get(pre_version_code=ask.version_code)
        except Patch.DoesNotExist:
            answer.type = updatemessage_pb2.APK
            answer.url = reverse(
                    'bsdiff:get_apk', 
                    args = [
                        apk.package_name,
                        '%s.apk' % apk.version_code
                        ]
                    )
            answer.apk_md5 = apk.file_md5
            return answer.SerializeToString()
        answer.type = updatemessage_pb2.PATCH
        answer.url = reverse(
                'bsdiff:get_patch',
                args = [
                    apk.package_name,
                    '%s_%s' % (patch.pre_version_code, apk.version_code)
                    ]
                )
        answer.apk_md5 = apk.file_md5
        answer.patch_md5 = patch.file_md5
        return answer.SerializeToString()
    else:
        answer.has_update = False
        return answer.SerializeToString()
