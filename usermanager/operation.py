# -*- coding: utf-8 -*-
import usermessage_pb2
from usermanager.models import PhoneUser


def update_user(message):
    # get the report object
    report = usermessage_pb2.UserReport()
    report.ParseFromString(message)
    try:
        user = PhoneUser.objects.get(pk=report.user_id)
        user.product = report.phone_product
        user.model = report.phone_model
        user.system_sdk = report.phone_system_sdk_version
    except PhoneUser.DoesNotExist:
        user = PhoneUser(
                unique_id=report.user_id,
                product=report.phone_product,
                model=report.phone_model,
                system_sdk=report.phone_system_sdk_version
                )
    user.save()
    return "Success"
