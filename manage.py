#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line

def main():
    """
    Define the function that will run the application and all control interfaces
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'garden_interface.settings')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
