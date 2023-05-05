"""
Establishing the model used for comments
"""
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from post.models import Post # pylint: disable=E0401
from notifications.models import Notification # pylint: disable=E0401

# Create your models here.

class Comment(models.Model):
    """
    Modeling the messaging protocol used in order to directly
    send messages between users in Garden Connect
    Attributes:
		post: A class instance derived from the post the comment
        is placed on
		user: A class instance derived from a given user's comment
        body: A class instance of a string of text representing the
        comment information from a user
        date: A class instance of a string of text for when the comment
        was posted
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def user_comment_post(sender, instance, *args, **kwargs): # pylint: disable=E0213, W0613
        """
        User making a comment on a post
        Args:
			sender: A class instance of User representing the user that
            makes the comment
            instance: A class instance containing the information about the
            comment information, sender, and post the comment was made on
        """
        comment = instance
        post = comment.post
        text_preview = comment.body[:90]
        sender = comment.user # pylint: disable=W0642
        notify = Notification(post=post, sender=sender, user=post.user,
                              text_preview=text_preview ,notification_type=2)
        notify.save()

    def user_del_comment_post(sender, instance, *args, **kwargs): # pylint: disable=E0213, W0613
        """
        User deleting a comment on a post
        Args:
			sender: A class instance of User representing the user that
            makes the comment
            instance: A class instance containing the information about the
            comment information, sender, and post the comment was made on
        """
        like = instance
        post = like.post
        sender = like.user # pylint: disable=W0642

        notify = Notification.objects.filter(post=post, sender=sender, notification_type=2) # pylint: disable=E1101
        notify.delete()

#Comment
post_save.connect(Comment.user_comment_post, sender=Comment)
post_delete.connect(Comment.user_del_comment_post, sender=Comment)
