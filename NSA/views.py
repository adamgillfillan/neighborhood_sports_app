from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('nsa/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('nsa/about.html', context_dict, context)


