from usermanager.models import User


def update_user(unique_id, product, model, system_sdk):
    try:
        user = User.objects.get(pk=unique_id)
        user.product = product
        user.model = model
        user.system_sdk = system_sdk
    except User.DoesNotExist:
        user = User(
                unique_id=unique_id,
                product=product,
                model=model,
                system_sdk=system_sdk
                )
    user.save()
    return user
