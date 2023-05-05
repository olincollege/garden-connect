"""
Creates the view canvas for direct messaging between users
"""
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from notifications.models import Notification # pylint: disable=E0401
from notifications.forms import PlantForm # pylint: disable=E0401

# Create your views here.


def show_notifications(request):
    """
    Establishes the notifications meant to be displayed to
    a user
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		An http response with a dictionary containing all of
        the notifications that were not cleared
    """
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by("-date") # pylint: disable=E1101
    Notification.objects.filter(user=user, is_seen=False).update(is_seen=True) # pylint: disable=E1101

    template = loader.get_template("notifications.html")

    context = {
        "notifications": notifications,
    }

    return HttpResponse(template.render(context, request))


def delete_notification(request, noti_id):
    """
    Deletes a given notification
    Args:
		request: An http GET request when a user would like
		to access the page
        noti_id: A string linking to a specific notification
    Returns:
		A redirection to the notification page without the
        selected notification
    """
    user = request.user
    Notification.objects.filter(id=noti_id, user=user).delete() # pylint: disable=E1101
    return redirect("show-notifications")


def CountNotifications(request): # pylint: disable=C0103
    """
    Counts the number of of unread notifications
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A dictionary with the number of unread notifications
    """
    count_notifications_index = 0
    if request.user.is_authenticated:
        count_notifications_index = Notification.objects.filter( # pylint: disable=E1101
            user=request.user, is_seen=False
        ).count()

    return {"count_notifications": count_notifications_index}

def plant_signup(request):
    """
    Establishes the plant sign up form for notifications
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A redireaction to the form where a user can sign up for
        reminder notifications
    """
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = PlantForm()
    context = {
        'form':form,
	}

    return render(request, 'plant_reminder.html', context)
