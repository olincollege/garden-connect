from django.shortcuts import redirect
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from notifications.models import Notification, PlantInterest
from notifications.forms import PlantForm
from django.contrib.auth.models import User

# Create your views here.


def ShowNotifications(request):
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
    user = request.user
    template = loader.get_template("survey.html")
    interest_form = PlantInterest
    plant = interest_form.get_plants_interest
    garden_location = interest_form.get_garden_location
    time = interest_form.get_watering_time
    context = {"plant": plant, "location": garden_location, "hour": time}
    return HttpResponse(template.render(context, request))

def plant_signup(request):
	if request.method == 'POST':
		form = PlantForm(request.POST)
		if form.is_valid():
			interest = form.cleaned_data.get('interest')
			location = form.cleaned_data.get('location')
			time = form.cleaned_data.get('time')
			# notify = GardenNotification()
            #             notify.save()
			return redirect('index')
	else:
		form = PlantForm()
	
	context = {
		'form':form,
	}

	return render(request, 'plant_reminder.html', context)
