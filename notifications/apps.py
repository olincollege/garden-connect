"""
Establishes notifcation protocol for Garden Conenct
"""
from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    """
    Class for configuring the notification protocols for the
    Garden Connect app

    Attributes:
        name: A string representing the naming reference to use
        for refering to the notifcation protocol
    """
    name = 'notifications'
