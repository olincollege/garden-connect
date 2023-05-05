"""
Establishing the model used for notification sending
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
    """
    Modeling the messaging protocol used in order to directly
    send messages between users in Garden Connect
    Attributes:
		NOTIFICATION_TYPES: A list of tuples corresponding to the type
        of notification to display
        post: A class instance of a given notification to display
        sender: A class instance of a given user who is
        providing the notification
        user: A class instance representing a user receiving the notification
        notification_type: A class where the type of notification is chosen
        text_preview: A class instance representing a string of characters
        representing the information to display in the notification
        date: A class instance representing a string for
        when a notification has been posted
        is_seen: A class instance representing a boolean expression for
        if a notification has been read
    """
    NOTIFICATION_TYPES = ((1,'Like'),(2,'Comment'), (3,'Follow'))
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE,
                             related_name="noti_post", blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noti_from_user")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noti_to_user")
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    text_preview = models.CharField(max_length=90, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
