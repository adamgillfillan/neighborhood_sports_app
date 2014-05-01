from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from NSA.models import Event
from NSA.forms import EventForm
from pygeocoder import Geocoder


def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('nsa/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('nsa/about.html', context_dict, context)


def map(request):
    context = RequestContext(request)
    event_list = get_event_list()
    event_lat_long(event_list)
    context_dict = {'event_list': event_list}
    return render_to_response('nsa/map.html', context_dict, context)


def event(request):
    context = RequestContext(request)

    event_list = get_event_list()
    event_lat_long(event_list)

    context_dict = {'event_list': event_list}
    return render_to_response('nsa/event.html', context_dict, context)


def add_event(request):
    context = RequestContext(request)

    event_list = get_event_list()
    event_lat_long(event_list)

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.latitude, event.longitude = convert_address_to_lat_lng(event.address)
            event.latitude = round(event.latitude, 7)
            event.longitude = round(event.longitude, 7)
            event.save()

            #Change where redirect goes for success on form submission
            return map(request)
        else:
            print(form.errors)
    else:
        form = EventForm()
    return render_to_response('nsa/add_event.html', {'form': form, 'event_list': event_list}, context)


def get_event_list():
    event_list = Event.objects.all()
    return event_list


def event_lat_long(event_list):
    for event in event_list:
        event.latitude, event.longitude = convert_address_to_lat_lng(event.address)
        event.latitude = round(event.latitude, 7)
        event.longitude = round(event.longitude, 7)


def convert_address_to_lat_lng(address):
    results = Geocoder.geocode(address)
    return results[0].coordinates


def login(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('nsa/login.html', context_dict, context)

