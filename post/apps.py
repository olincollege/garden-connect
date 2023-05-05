"""
Establishes posting protocol for Garden Conenct
"""
from django.apps import AppConfig


class PostConfig(AppConfig):
    """
    Class for configuring the post protocols for the
    Garden Connect app

    Attributes:
        name: A string representing the naming reference to use
        for refering to the post protocol
    """
    name = 'post'
