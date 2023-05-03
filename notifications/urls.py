from django.urls import path
from notifications.views import ShowNOtifications, DeleteNotification, Survey


urlpatterns = [
    path("", ShowNOtifications, name="show-notifications"),
    path("<noti_id>/delete", DeleteNotification, name="delete-notification"),
    path("plant_watering_survey/", Survey),
]
