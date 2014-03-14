from django.test import TestCase
from django.shortcuts import render_to_response, RequestContext

def home_page(request):
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

