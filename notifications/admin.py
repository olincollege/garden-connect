"""
Import functional items for the posting function
"""
from django.contrib import admin
from notifications.models import Notification # pylint: disable=E0401
# Register your models here.
admin.site.register(Notification)
