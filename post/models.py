"""
Establishing the model used for posting items
"""
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify
from django.urls import reverse
from notifications.models import Notification # pylint: disable=E0401

# Create your models here.

def user_directory_path(instance, filename):
    """
    Takes a pathway for a photo and utilizes it for a profile picture
    Args:
        instance: A class instance containing the information about the
        user making the photo change
        filename: A string representing the path way derived from a given
        image from the user's computer
    Returns:
        A formatted string for the file used for the given user's profile
        image
    """
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{0}/{1}'.format(instance.user.id, filename)

class Tag(models.Model):
    """
    Creates a set of posts separated by tags
    Attributes:
		title: A class instance where there are a set of words
        separated by commas used as tags
        slug: A class instance where a link is made from the
        tags generated in title
    """
    title = models.CharField(max_length=75, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True)
    class Meta: # pylint: disable=R0903
        """
		Creating the field for the tagging functions
		Attributes:
			verbose_name: A string where there is one set of characters
            for one tag
			verbose_name_plural: A string separated by commas where there
            are multiple tags
		"""
        verbose_name='Tag'
        verbose_name_plural = 'Tags'

    def get_absolute_url(self):
        """
        Creates a url from a specific tag
        Returns:
			A url based on a tag that can be used in GardenConnect
        """
        return reverse('tags', args=[self.slug])
    def __str__(self):
        """
        Creates a tag title on a specific tag page
        Returns:
			A string used to display the given tag name
        """
        return str(self.title)

    def save(self, *args, **kwargs):
        """
        Saves the tag information of a given tag
        Returns:
			A class instance of a new tag on a post
        """
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class PostFileContent(models.Model):
    """
    Compiles the conent of a given post from a file
    Attributes:
		user: A class instance representing a given user
        in GardenConnect
        file: A class instance where a leading file directory
        links to an uploadable file
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_owner')
    file = models.FileField(upload_to=user_directory_path)

class Post(models.Model):
    """
    Establishes post model for GardenConnect
    Attributes:
		id: A class instance corresponding to the url ID of the post
    	content: A class instance representing the image details of a
        post
    	caption: A class instance representing the comment body of
        the post
    	posted: A class instance representing the time the post
        was made
    	tags: A class instance representing the tags of the post
    	user: A class instance representing the user that made the
        post
    	likes: A class instance representing the number of likes
        made on the post
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content =  models.ManyToManyField(PostFileContent, related_name='contents')
    caption = models.TextField(max_length=1500, verbose_name='Caption')
    posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='tags')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)


    def get_absolute_url(self):
        """
        Creates a url from a specific post
        Returns:
			A url based on a post that can be used in GardenConnect
        """
        return reverse('postdetails', args=[str(self.id)])

    def __str__(self):
        """
        Creates a referable post from the post ID
        Returns:
			A string used to display the given post ID
        """
        return str(self.id)


class Follow(models.Model):
    """
    Establishes the follower model in GardenConnect
    Attributes:
		follower: A class instance representing a user following someone
    	following: A class instance representing a user being followed by someone
    """
    follower = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='follower')
    following = models.ForeignKey(User,on_delete=models.CASCADE,
                                  null=True, related_name='following')

    def user_follow(sender, instance, *args, **kwargs): # pylint: disable=E0213, W0613
        """
        Allow one user to follow another user
        Args:
			sender: A class instance who would like to follow another given
            user
            instance: A request made to follow a given account
        """
        follow = instance
        sender = follow.follower # pylint: disable=W0642
        following = follow.following
        notify = Notification(sender=sender, user=following, notification_type=3)
        notify.save()

    def user_unfollow(sender, instance, *args, **kwargs): # pylint: disable=E0213, W0613
        """
        Allow one user to unfollow another user
        Args:
			sender: A class instance who would like to stop following another given
            user
            instance: A request made to ufollow a given account
        """
        follow = instance
        sender = follow.follower # pylint: disable=W0642
        following = follow.following # pylint: disable=E1101
        notify = Notification.objects.filter(sender=sender, user=following, notification_type=3) # pylint: disable=E1101
        notify.delete()

class Stream(models.Model):
    """
    Establishes the follower model in GardenConnect
    Attributes:
    	following: A class instance representing a user being followed
        by a given user
		user: A class instance representing a user's posting feed
    	post: A class instance representing a post within the user's feed
        date: A class instance representing a post's time when posted
    """
    following = models.ForeignKey(User, on_delete=models.CASCADE,null=True,
                                  related_name='stream_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()

    def add_post(sender, instance, *args, **kwargs): # pylint: disable=E0213, W0613
        """
        Allow a post to be added to one's stream from a followed user
        Args:
			sender: A class instance for someone following a list of people
            instance: A request made to like compile all posts from the followed
            users
        """
        post = instance
        user = post.user # pylint: disable=E1101
        followers = Follow.objects.all().filter(following=user) # pylint: disable=E1101
        for follower in followers:
            stream = Stream(post=post, user=follower.follower, date=post.posted, following=user)
            stream.save()

class Likes(models.Model):
    """
    Establishes the like model in GardenConnect
    Attributes:
		user: A class instance representing a user adding a like
    	post: A class instance representing a post having a like added
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')

    def user_liked_post(sender, instance, *args, **kwargs): # pylint: disable=E0213, W0613
        """
        Allow one user to like a post
        Args:
			sender: A class instance for someone who wants to like a post
            instance: A request made to like a given post
        """
        like = instance
        post = like.post
        sender = like.user # pylint: disable=W0642
        notify = Notification(post=post, sender=sender, user=post.user, notification_type=1)
        notify.save()

    def user_unlike_post(sender, instance, *args, **kwargs): # pylint: disable=E0213, W0613
        """
        Allow one user to unlike a post
        Args:
			sender: A class instance for someone who wants to unlike a post
            instance: A request made to unlike a given post
        """
        like = instance
        post = like.post
        sender = like.user # pylint: disable=W0642
        notify = Notification.objects.filter(post=post, sender=sender, notification_type=1) # pylint: disable=E1101
        notify.delete()


#Stream
post_save.connect(Stream.add_post, sender=Post)

#Likes
post_save.connect(Likes.user_liked_post, sender=Likes)
post_delete.connect(Likes.user_unlike_post, sender=Likes)

#Follow
post_save.connect(Follow.user_follow, sender=Follow)
post_delete.connect(Follow.user_unfollow, sender=Follow)
