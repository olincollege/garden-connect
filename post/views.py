"""
Creates the view canvas for looking at posts
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from post.models import Stream, Post, Tag, Likes, PostFileContent # pylint: disable=E0401
from post.forms import NewPostForm # pylint: disable=E0401
from comment.models import Comment # pylint: disable=E0401
from comment.forms import CommentForm # pylint: disable=E0401
from authy.models import Profile # pylint: disable=E0401



# Create your views here.
@login_required
def index(request):
    """
    Establishes a feed of posts to view in a user's feed
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A dictionary consisting of all of the posts visible to a
        logged in user
    """
    user = request.user
    posts = Stream.objects.filter(user=user) # pylint: disable=E1101


    group_ids = []

    for post in posts:
        group_ids.append(post.post_id)
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted') # pylint: disable=E1101

    template = loader.get_template('index.html')

    context = {
        'post_items': post_items,
    }

    return HttpResponse(template.render(context, request))

def post_details(request, post_id):
    """
    Establishes statistics and logitsitcs of a post
    Args:
		request: An http GET request when a user would like
		to access the page
        post_id: A string associated to a given post to refer
        to that post
    Returns:
		An http request linking all of the post details such as
        the likes, selected post and comments to a dictionary
    """
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    profile = Profile.objects.get(user=user) # pylint: disable=E1101
    favorited = False

	# Comment
    comments = Comment.objects.filter(post=post).order_by('date') # pylint: disable=E1101
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=user) # pylint: disable=E1101
		#For the color of the favorite button

        if profile.favorites.filter(id=post_id).exists():
            favorited = True

	# Comment form
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()
            return HttpResponseRedirect(reverse('postdetails', args=[post_id]))
    else:
        form = CommentForm()


    template = loader.get_template('post_detail.html')

    context = {
        'post':post,
        'favorited':favorited,
        'profile':profile,
        'form':form,
        'comments':comments,
	}

    return HttpResponse(template.render(context, request))


@login_required
def new_post(request):
    """
    Redirects a user to commit a new post
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A request to redirect the user to the new post page
    """
    user = request.user
    tags_objs = []
    files_objs = []

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('content')
            caption = form.cleaned_data.get('caption')
            tags_form = form.cleaned_data.get('tags')

            tags_list = list(tags_form.split(','))

            for tag in tags_list:
                tagged = Tag.objects.get_or_create(title=tag) # pylint: disable=E1101
                tags_objs.append(tagged[0])

            for file in files:
                file_instance = PostFileContent(file=file, user=user)
                file_instance.save()
                files_objs.append(file_instance)

            select_post = Post.objects.get_or_create(caption=caption, user=user) # pylint: disable=E1101
            select_post = select_post[0]
            select_post.tags.set(tags_objs)
            select_post.content.set(files_objs)
            select_post.save()
            return redirect('index')
    else:
        form = NewPostForm()

    context = {
        'form':form,
	}

    return render(request, 'newpost.html', context)


@login_required
def new_plant(request):
    """
    Redirects a user to sign up for a new plant notification
    Args:
		request: An http GET request when a user would like
		to access the page
    Returns:
		A request to redirect the user to the plant notification page
    """
    user = request.user
    tags_objs = []
    files_objs = []

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('content')
            caption = form.cleaned_data.get('caption')
            tags_form = form.cleaned_data.get('tags')

            tags_list = list(tags_form.split(','))

            for tag in tags_list:
                tagged = Tag.objects.get_or_create(title=tag) # pylint: disable=E1101
                tags_objs.append(tagged[0])

            for file in files:
                file_instance = PostFileContent(file=file, user=user)
                file_instance.save()
                files_objs.append(file_instance)

            select_post = Post.objects.get_or_create(caption=caption, user=user) # pylint: disable=E1101
            select_post = select_post[0]
            select_post.tags.set(tags_objs)
            select_post.content.set(files_objs)
            select_post.save()
            return redirect('index')
    else:
        form = NewPostForm()

    context = {
        'form':form,
	}

    return render(request, 'survey.html', context)

def tags(request, tag_slug):
    """
    Redirects a user to sign up for a new plant notification
    Args:
		request: An http GET request when a user would like
		to access the page
		tag_slug: A string of characters separated by commas
        which are meant to represent tags
    Returns:
		A request to add the given post to the list of tags categorized
        under the specified tags
    """
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag).order_by('-posted') # pylint: disable=E1101

    template = loader.get_template('tag.html')

    context = {
        'posts':posts,
        'tag':tag,
	}

    return HttpResponse(template.render(context, request))



@login_required
def like(request, post_id):
    """
    Add a like to a given post
    Args:
		request: An http GET request when a user would like
		to access the page
        post_id: A string associated to a given post to refer
        to that post
    Returns:
		A request to redirect the user to the post after the
        post has been liked
    """
    user = request.user
    post = Post.objects.get(id=post_id) # pylint: disable=E1101
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count() # pylint: disable=E1101

    if not liked:
        current_likes = current_likes + 1

    else:
        Likes.objects.filter(user=user, post=post).delete() # pylint: disable=E1101
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()

    return HttpResponseRedirect(reverse('postdetails', args=[post_id]))

@login_required
def favorite(request, post_id):
    """
    Save a given post
    Args:
		request: An http GET request when a user would like
		to access the page
        post_id: A string associated to a given post to refer
        to that post
    Returns:
		A request to redirect the user to the post after the
        post has been saved
    """
    user = request.user
    post = Post.objects.get(id=post_id) # pylint: disable=E1101
    profile = Profile.objects.get(user=user) # pylint: disable=E1101

    if profile.favorites.filter(id=post_id).exists():
        profile.favorites.remove(post)

    else:
        profile.favorites.add(post)

    return HttpResponseRedirect(reverse('postdetails', args=[post_id]))
