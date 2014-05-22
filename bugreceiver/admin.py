from django.contrib import admin
from bugreceiver.models import JavaBug, NativeBug


# Register your models here.
admin.site.register(JavaBug)
admin.site.register(NativeBug)