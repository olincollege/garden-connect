from django import forms
from django.db import models
from django.contrib.auth.models import User

class PlantForm(forms.ModelForm):
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
    interest = forms.CharField(label='Which plant are you interested in?', widget=forms.Select(choices=CROP_CHOICES))
    location = forms.CharField(label='Do you plan to have a garden inside or outside?', widget=forms.Select(choices=GARDEN_LOCATION))
    time = forms.CharField(label='What time of day is best for watering your plants?', widget=forms.Select(choices=TIME_CHOICES))
	
    class Meta:
        model = User
        fields = ('interest', 'location', 'time')
	