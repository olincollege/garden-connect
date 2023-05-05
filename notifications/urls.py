"""
Establishing URL pathways accessible for displayed notifications
"""
from django.urls import path
from notifications.views import show_notifications, delete_notification, plant_signup # pylint: disable=E0401


urlpatterns = [
    path("", show_notifications, name="show-notifications"),
    path("<noti_id>/delete", delete_notification, name="delete-notification"),
    path("plant_signup/", plant_signup, name="plant_signup"),
]
