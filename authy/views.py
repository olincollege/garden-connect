"""
Initializes the display information of a given user on Garden
Connect
"""
import random
from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import resolve
from django.db import transaction
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from authy.forms import SignupForm, ChangePasswordForm, EditProfileForm # pylint: disable=E0401
from authy.models import Profile # pylint: disable=E0401
from post.models import Post, Follow, Stream # pylint: disable=E0401

# Create your views here.
def user_profile(request, username):
    """
    Establishes the display information of a given user
    Args:
		request: An http GET request when a user would like
		to access the page
        username: A string representing the given user in the
        database
    Returns:
		A dictionary where the keys map to analytics of a given
        user such as their username, posts, and follower statistics
    """
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user) # pylint: disable=E1101
    url_name = resolve(request.path).url_name

    if url_name == 'profile':
        posts = Post.objects.filter(user=user).order_by('-posted') # pylint: disable=E1101

    else:
        posts = profile.favorites.all()

	#Profile info box
    posts_count = Post.objects.filter(user=user).count() # pylint: disable=E1101
    following_count = Follow.objects.filter(follower=user).count() # pylint: disable=E1101
    followers_count = Follow.objects.filter(following=user).count() # pylint: disable=E1101

	#follow status
    follow_status = Follow.objects.filter(following=user, follower=request.user).exists() # pylint: disable=E1101

	#Pagination
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    template = loader.get_template('profile.html')

    context = {
        'posts': posts_paginator,
        'profile':profile,
        'following_count':following_count,
        'followers_count':followers_count,
        'posts_count':posts_count,
        'follow_status':follow_status,
        'url_name':url_name,
	}

    return HttpResponse(template.render(context, request))

def user_profile_favorites(request, username):
    """
    Establishes the display information of a given user's
    saved posts
    Args:
		request: An http GET request when a user would like
		to access the page
        username: A string representing the given user in the
        database
    Returns:
		A dictionary where the keys map to analytics of the set of
        posts they've saved
    """
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user) # pylint: disable=E1101
    posts = profile.favorites.all()

    #Profile info box
    posts_count = Post.objects.filter(user=user).count() # pylint: disable=E1101
    following_count = Follow.objects.filter(follower=user).count() # pylint: disable=E1101
    followers_count = Follow.objects.filter(following=user).count() # pylint: disable=E1101

    #Pagination
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)
    template = loader.get_template('profile_favorite.html')

    context = {
        'posts': posts_paginator,
        'profile':profile,
        'following_count':following_count,
        'followers_count':followers_count,
        'posts_count':posts_count,
    }

    return HttpResponse(template.render(context, request))


def signup(request):
    """
    Initiates the user signup process
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A redirect request to the signup form
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('index')
    else:
        form = SignupForm()

    context = {
        'form':form,
    }

    return render(request, 'signup.html', context)

@login_required
def password_change(request):
    """
    Initiates the user password reset process
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A redirect request to the password reset form
    """
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('change_password_done')
    else:
        form = ChangePasswordForm(instance=user)

    context = {
        'form':form,
    }

    return render(request, 'change_password.html', context)

def password_change_done(request):
    """
    States if the password reset has been successfully called
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A redirect request to the successful password reset page
    """
    return render(request, 'change_password_done.html')


@login_required
def edit_profile(request):
    """
    Initiates the profile editing process
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A redirect request to the profile edit form
    """
    user = request.user.id
    profile = Profile.objects.get(user__id=user) # pylint: disable=E1101

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.picture = form.cleaned_data.get('picture')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.profile_info = form.cleaned_data.get('profile_info')
            profile.save()
            return redirect('index')
    else:
        form = EditProfileForm()

    context = {
        'form':form,
    }

    return render(request, 'edit_profile.html', context)

@login_required
def index(request): # pylint: disable=R0914
    """
    Generates a feed based on the user's following list
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A redirect request to the homepage with all of the
        relevant feed information of a given user
    """
    user_object = User.objects.get(username=request.user.username)
    user_profile_instance = Profile.objects.get(user=user_object) # pylint: disable=E1101

    user_following_list = []
    feed = []

    user_following = Follow.objects.filter(follower=request.user.username) # pylint: disable=E1101

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames) # pylint: disable=E1101
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    # user suggestion starts
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    new_suggestions_list = [x for x in list(all_users) if x not in list(user_following_all)]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if x not in list(current_user)]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids) # pylint: disable=E1101
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))


    return render(request, 'index.html', {'user_profile': user_profile_instance,
                                          'posts':feed_list, 'suggestions_username_profile_list':
                                          suggestions_username_profile_list[:4]})

@login_required
def follow(request, username, option):
    """
    Initiates the ability to follow users
    Args:
		request: An http GET request when a user would like
		to access the page
        username: A string representing the given user in the
        database
        option: An integer representing  if a user is being followed
        or not by another user
    Returns:
		A redirect request to user's profile page after they have
        been followed or unfollowed
    """
    following = get_object_or_404(User, username=username)
    try:
        follow_instance = Follow.objects.get_or_create(follower=request.user, following=following) # pylint: disable=E1101
        if int(option) == 0:
            follow_instance[0].delete()
            Stream.objects.filter(following=following, user=request.user).all().delete() # pylint: disable=E1101
        else:
            posts = Post.objects.all().filter(user=following)[:25] # pylint: disable=E1101
            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post, user=request.user,
                                    date=post.posted, following=following)
                    stream.save()

        return HttpResponseRedirect(reverse('profile', args=[username]))
    except User.DoesNotExist: # pylint: disable=E1101
        return HttpResponseRedirect(reverse('profile', args=[username]))
def explore(request):
    """
	Creates a static webpage to display the information
	page of the explore tab in Garden Connect
	Args:
		request: An http GET request when a user would like
		to access the page
	Returns:
		An html file when the get request is fulfilled corresponding
		to the explore tab
	"""
    return render(request, 'explore.html')

def cucumber(request):
    """
	Creates a static webpage to display the information
	page of cucumber
	Args:
		request: An http GET request when a user would like
		to access the page
	Returns:
		An html file when the get request is fulfilled corresponding
		to the cucumber information page
	"""
    return render(request, 'cucumber.html')

def lettuce(request):
    """
	Creates a static webpage to display the information
	page of lettuce
	Args:
		request: An http GET request when a user would like
		to access the page
	Returns:
		An html file when the get request is fulfilled corresponding
		to the lettuce information page
	"""
    return render(request, 'lettuce.html')

def tomato(request):
    """
	Creates a static webpage to display the information
	page of tomato
	Args:
		request: An http GET request when a user would like
		to access the page
	Returns:
		An html file when the get request is fulfilled corresponding
		to the tomato information page
	"""
    return render(request, 'tomato.html')

def kale(request):
    """
	Creates a static webpage to display the information
	page of kale
	Args:
		request: An http GET request when a user would like
		to access the page
	Returns:
		An html file when the get request is fulfilled corresponding
		to the kale information page
	"""
    return render(request, 'jalepenos.html')
