__author__ = 'adamg_000'
from django import forms
from NSA.models import Event
#frnom django.contrib.auth.models import User


class EventForm(forms.ModelForm):
    sport = forms.CharField(max_length=50, help_text="Sport")
    players = forms.IntegerField(help_text="Number of players you need.")
    # info = forms.CharField(widget=forms.Textarea, required=False, help_text=" (Optional) Please enter any information that may help those "
    #                                                         "wishing to play with you.")
    address = forms.CharField(help_text="Address")
    latitude = forms.FloatField(widget=forms.HiddenInput(), initial=0)
    longitude = forms.FloatField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Event