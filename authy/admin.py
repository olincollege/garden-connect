"""
Registers a user profile class for Garden Connect Users
"""
from django.contrib import admin
from authy.models import Profile # pylint: disable=E0401
# Register your models here.

admin.site.register(Profile)
