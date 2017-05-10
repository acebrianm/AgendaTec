from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


# Logout
from django.contrib.auth import logout

# Create your views here.
def index(request):

    # Template render
    template = loader.get_template('fit/index.html')
    context = {
            'tag_list': ["Sports", "culture"]
    }
    return HttpResponse(template.render(context, request))

