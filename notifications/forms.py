"""
Creates a form where users may create new plant reminders
"""
from django import forms
from django.db import models
from django.contrib.auth.models import User # pylint: disable=E0401

class PlantForm(forms.ModelForm):
    """
    Creating the form information for establishing plant notifications
    Attributes:
		CROP_CHOICES: A list of tuples corresponding to the type
        of crop notifications to receive
        GARDEN_LOCATION: A list of tuples corresponding to the location
        to calculate necessary gardening information
        TIME_CHOICES: A list of tuples corresponding to the desired times
        to get notifications
        user: A class instance representing a user receiving the notification
        interest: A class where a string for the type of plant is accounted
        for
        location: A class instance representing a string for where the
        plant has been placed
        time: A class instance representing a string for when to get a
        notification
    """
    CROP_CHOICES= [
    ('cucumber', 'Cucumber'),
    ('tomato', 'Tomato'),
    ('kale', 'Kale'),
    ('lettuce', 'Lettuce'),
    ]
    GARDEN_LOCATION = [('indoor', 'Indoor'),('outdoor', 'Outdoor')]
    TIME_CHOICES= ([tuple([time,str(time)+" AM"]) for time in range(1,13)] +
                   [tuple([time,str(time)+" PM"]) for time in range(1,13)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = forms.CharField(label='Which plant are you interested in?',
                               widget=forms.Select(choices=CROP_CHOICES))
    location = forms.CharField(label='Do you plan to have a garden inside or outside?',
                               widget=forms.Select(choices=GARDEN_LOCATION))
    time = forms.CharField(label='What time of day is best for watering your plants?',
                           widget=forms.Select(choices=TIME_CHOICES))

    class Meta: # pylint: disable=R0903
        """
		Creating the formatting fields for creating a new plant notification

		Attributes:
			model: A class representing an instance of a new comment
			being formed
			fields: A tuple showing the areas the field arrangements
            for notifications relevant to the interest ofm plant,
            crop location, and desired time for notifications
		"""
        model = User
        fields = ('interest', 'location', 'time')
	