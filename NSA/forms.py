__author__ = 'adamg_000'
from django import forms
from NSA.models import Event
#frnom django.contrib.auth.models import User


class EventForm(forms.ModelForm):
    sport = forms.CharField(max_length=50, help_text="Please enter the sport you are playing.")
    players = forms.IntegerField(help_text="Please enter the number of players you currently have.")
    info = forms.CharField(widget=forms.Textarea, help_text="Please enter any information that may help those "
                                                            "wishing to play with you.")
    address = forms.CharField(help_text="Please enter the address of where you are playing.")
    latitude = forms.FloatField(widget=forms.HiddenInput(), initial=0)
    longitude = forms.FloatField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Event