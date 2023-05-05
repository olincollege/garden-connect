"""
Registers a direct messaging interface for Garden Connect Users
"""
from django.contrib import admin
from direct.models import Message # pylint: disable=E0401

# Register your models here.
admin.site.register(Message)
