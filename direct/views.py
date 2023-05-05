"""
Creates the view canvas for direct messaging between users
"""
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from direct.models import Message # pylint: disable=E0401

# Create your views here.

@login_required
def inbox(request):
    """
    Establishes inbox function for the compliation of user
    communications
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A dictionary where the keys map to the collection of all
        messages from a user, the compilation of all message chats,
        and the messages sent to a user
    """
    messages = Message.get_messages(user=request.user)
    active_direct = None
    direct_message = None

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        direct_message = Message.objects.filter(user=request.user, # pylint: disable=E1101
                                                recipient=message['user'])
        direct_message.update(is_read=True)
        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0

    context = {
        'directs': direct_message,
        'messages': messages,
        'active_direct': active_direct,
    }

    template = loader.get_template('direct/direct.html')

    return HttpResponse(template.render(context, request))

@login_required
def user_search(request):
    """
    Search function for users to look up people they can
    directly message
    Args:
		request: An http GET request when a user would like
		to access the page with a specific search instance
    Returns:
		An http response page corrleating to any usernames with
        similarities in the search query
    """
    query = request.GET.get("q")
    context = {}
    if query:
        users = User.objects.filter(Q(username__icontains=query))

        #Pagination
        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
                'users': users_paginator,
		}
    template = loader.get_template('direct/search_user.html')
    return HttpResponse(template.render(context, request))

@login_required
def directs(request, username):
    """
    Establishes the message history of a given user in a
    direct message chain
    Args:
		request: An http GET request when a user would like
		to access the page
        username: A user class instance correlating to
        a given user's messaging history
    Returns:
		A dictionary where the keys map to the collection of all
        messages from a user, the compilation of all message chats,
        and the messages sent to a user
    """
    user = request.user
    messages = Message.get_messages(user=user)
    active_direct = username
    direct_message = Message.objects.filter(user=user, # pylint: disable=E1101
                                             recipient__username=username)
    direct_message.update(is_read=True)
    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0

    context = {
        'directs': direct_message,
        'messages': messages,
        'active_direct':active_direct,
    }

    template = loader.get_template('direct/direct.html')

    return HttpResponse(template.render(context, request))


@login_required
def new_conversation(request, username): # pylint: disable=E1101
    """
    Establishes a new communication between two users
    Args:
		request: An http GET request when a user would like
		to access the page
        username: A class instance of a specific user that is
        receiving a new message
    Returns:
		An http response redirecting the user back to the inbox
        after sending the message to the user
    """
    from_user = request.user
    body = ''
    try:
        to_user = User.objects.get(username=username)
    except User.DoesNotExist: # pylint: disable=E1101
        return redirect('usersearch')
    if from_user != to_user:
        Message.send_message(from_user, to_user, body)
    return redirect('inbox')

@login_required
def send_direct(request):
    """
    Sends a message to a user that has already communicated
    with a selected user
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A http response redirecting the user back to the inbox
        after sending the message to the user
    """
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')
    if request.method == 'POST':
        to_user = User.objects.get(username=to_user_username)
        Message.send_message(from_user, to_user, body)
        return redirect('inbox')
    return HttpResponseBadRequest()

def checkDirects(request): # pylint: disable=C0103
    """
    Finds the number of unread messages in direct messages
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A dictionary correlating to the number of unread messages
    """
    directs_count = 0
    if request.user.is_authenticated:
        directs_count = Message.objects.filter(user=request.user, is_read=False).count() # pylint: disable=E1101

    return {'directs_count':directs_count}
	