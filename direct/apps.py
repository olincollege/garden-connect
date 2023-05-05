"""
Establishes the messaging protocol for direct messages
"""
from django.apps import AppConfig


class DirectConfig(AppConfig):
    """
    Class for configuring the messaging protocols for the
    Garden Connect app

    Attributes:
        name: A string representing the naming reference to use
        for refering to the direct message protocol
    """
    name = 'direct'
