__author__ = 'adamg_000'
from django import forms
from NSA.models import Event
#from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

PLAYER_CHOICES = ((5, 'Less than 5 players'), (10, '5-10 players'), (15, '11-15 players'), (16, 'More than 15 players'))
SPORT_CHOICES = (('Football', mark_safe('Football <img src="../../static/img/Football.png"/>')),
                 ('Soccer', mark_safe('Soccer <img src="../../static/img/Soccer.png"/>')),
                 ('Tennis', mark_safe('Tennis <img src="../../static/img/Football.png"/>')),
                 ('Basketball', mark_safe('Basketball <img src="../../static/img/Football.png"/>')),
                 ('Baseball', mark_safe('Baseball <img src="../../static/img/Football.png"/>')))


class EventForm(forms.ModelForm):
    sport = forms.ChoiceField(choices=SPORT_CHOICES, help_text="Sport")   #forms.CharField(max_length=50, help_text="Sport")
    players = forms.ChoiceField(choices=PLAYER_CHOICES, help_text="Number of players you have")   #forms.IntegerField(help_text="Number of players you have.")
    # info = forms.CharField(widget=forms.Textarea, required=False, help_text=" (Optional) Please enter any information that may help those "
    #                                                         "wishing to play with you.")
    address = forms.CharField(help_text="Address", widget=forms.TextInput(attrs={'placeholder': 'Carmichael Gym, Raleigh, NC'}))
    latitude = forms.FloatField(widget=forms.HiddenInput(), initial=0)
    longitude = forms.FloatField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Event