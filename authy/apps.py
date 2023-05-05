"""
Establishes the interactable protocol for user profiles
"""

from django.apps import AppConfig


class AuthyConfig(AppConfig):
    """
    Class for configuring the user protocols for the
    Garden Connect app

    Attributes:
        name: A string representing the naming reference to use
        for refering to the user protocol
    """
    name = 'authy'
