from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from NSA.models import Event


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

    context_dict = {}

    return render_to_response('nsa/map.html', context_dict, context)


def event(request):
    context = RequestContext(request)

    event_list = get_event_list()
    context_dict = {'event_list': event_list}

    return render_to_response('nsa/event.html', context_dict, context)


def get_event_list():
    event_list = Event.objects.all()

    return event_list