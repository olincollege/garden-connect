from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from plant_interest_survey import PlantInterest
from notifications.models import Notification

# Create your views here.


def ShowNOtifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by("-date")
    Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)

    template = loader.get_template("notifications.html")

    context = {
        "notifications": notifications,
    }

    return HttpResponse(template.render(context, request))


def DeleteNotification(request, noti_id):
    user = request.user
    Notification.objects.filter(id=noti_id, user=user).delete()
    return redirect("show-notifications")


def CountNotifications(request):
    count_notifications = 0
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(
            user=request.user, is_seen=False
        ).count()

    return {"count_notifications": count_notifications}


def Survey(request):
    interest_form = PlantInterest
    plant = interest_form.get_plants_interest
    garden_location = interest_form.get_garden_location
    time = interest_form.get_watering_time
    return {"plant": plant, "location": garden_location, "hour": time}
