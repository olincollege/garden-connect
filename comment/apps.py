"""
Establishes the interactable protocol for user comments
"""
from django.apps import AppConfig


class CommentConfig(AppConfig):
    """
    Class for configuring the commenting protocols for the
    Garden Connect app

    Attributes:
        name: A string representing the naming reference to use
        for refering to the comment protocol
    """
    name = 'comment'
