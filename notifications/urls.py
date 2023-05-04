from django.urls import path
from notifications.views import ShowNotifications, DeleteNotification, plant_signup


urlpatterns = [
    path("", ShowNotifications, name="show-notifications"),
    path("<noti_id>/delete", DeleteNotification, name="delete-notification"),
    path("plant_signup/", plant_signup, name="plant_signup"),
]
