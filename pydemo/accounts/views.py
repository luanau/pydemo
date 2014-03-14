from django.shortcuts import render_to_response, RequestContext

from accounts.script import prime
# Create your views here.
def my_view(request):
    a = prime(1,19)
    b = 'string'
    c = 2
    d = 'string'
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))
