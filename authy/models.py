"""
Establishing the model used for users
"""
import os
from PIL import Image
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from post.models import Post # pylint: disable=E0401

def user_directory_path(instance, filename): # pylint: disable=W0613
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
    profile_pic_name = f'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_pic_name

# Create your models here.
class Profile(models.Model):
    """
    Modeling the messaging protocol used in order to directly
    send messages between users in Garden Connect
    Attributes:
		user: A class instance derived from a given user's profile
        first_name: A class instance representing a string of the
        user's first name
        last_name: A class instance representing a string of the
        user's last name
        location: A class instance representing a string of the
        user's location
        url: A class instance representing a string of the
        user's personal website
        profile_info: A class instance representing a string of the
        user's description of themselves
        created: A class instance representing a string for the time the
        user made account changes
        favorites: A class instance representing a collection of user
        posts
        picture: A class instance representing an uploadably location for
        profile images
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    profile_info = models.TextField(max_length=150, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    favorites = models.ManyToManyField(Post)
    picture = models.ImageField(upload_to=user_directory_path, blank=True,
                                null=True, verbose_name='Picture')

    def save(self, *args, **kwargs):
        """
    	Saves the updated information when the
        user would like to change their account information
    	"""
        super().save(*args, **kwargs)
        size = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path) # pylint: disable=E1101
            pic.thumbnail(size, Image.LANCZOS)
            pic.save(self.picture.path) # pylint: disable=E1101

    def __str__(self):
        """
    	Returns the username that will be displayed on a user's
        profile
        Returns:
			A string representing the username of the given user
    	"""
        return self.user.username # pylint: disable=E1101
def create_user_profile(sender, instance, created, **kwargs): # pylint: disable=W0613
    """
    Creates a given user's profile for Garden Connect
    Args:
		instance: A class instance containing the information about
        user who has created their account
        created: A boolean value stating whether or not a new account
        has been created
    """
    if created:
        Profile.objects.create(user=instance) # pylint: disable=E1101

def save_user_profile(sender, instance, **kwargs): # pylint: disable=W0613
    """
    Saves a given user's profile to the dataframe
    Args:
		instance: A class instance containing the information about
        user who has created their account
    """
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
