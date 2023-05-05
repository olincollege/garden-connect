"""
Registers a comment interface for Garden Connect Users
"""
from django.contrib import admin
from comment.models import Comment # pylint: disable=E0401
# Register your models here.

admin.site.register(Comment)
