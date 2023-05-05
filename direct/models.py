"""
Establishing the model used for direct messaging between users
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max

# Create your models here.
class Message(models.Model):
    """
    Modeling the messaging protocol used in order to directly
    send messages between users in Garden Connect
    Attributes:
		user: A class instance derived from a given user's messaging
        statuses
        sender: A class instance of a given user who would like to
        send a message to another user
        recipient: A class instance of a given user who is recieving
        a message from the sender
        body: A class instance representing a string for the contents
        written by a user to send the message to
        date: A class instance representing a string for when a message
        was sent
        is_read: A class instance representing a boolean expression for
        whether or not a message has been read
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    body = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def send_message(from_user, to_user, body): # pylint: disable=E0213
        """
        Creates the messaging function for Garden connect user
        Args:
			from_user: A class instance of a given user who would like to
            send a message to another user
            to_user: A class instance of a given user who is recieving
            a message from the sender
            body: A text field class instance containing a string of the
            desired message between users
        Returns:
			A class instance representing a message string in
            addition to the given sender and recipient data
        """
        sender_message = Message(
            user=from_user,
            sender=from_user,
            recipient=to_user,
            body=body,
            is_read=True)
        sender_message.save()

        recipient_message = Message(
            user=to_user,
            sender=from_user,
            body=body,
            recipient=from_user,)
        recipient_message.save()
        return sender_message
    def get_messages(user): # pylint: disable=E0213
        """
        Displays all accounts a given user has sent messages to
        Args:
			user: A class instance of a given user who has sent
            messages to other users
        Returns:
			A list of users to be displayed on the html file
            corresponding to all other users the sender has
            communicated with
        """
        messages = Message.objects.filter(user=user).values('recipient').annotate( # pylint: disable=E1101
            last=Max('date')).order_by('-last')
        users = []
        for message in messages:
            users.append({
                'user': User.objects.get(pk=message['recipient']),
                'last': message['last'],
                'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], # pylint: disable=E1101
                                                 is_read=False).count()
                })
        return users
    