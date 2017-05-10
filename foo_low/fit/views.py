from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from datetime import datetime

# Models
from .models import Profile, Tag, Event


# Logout
from django.contrib.auth import logout

# Create your views here.
def index(request):

    # Template render
    tag_list = Tag.objects.all()
    template = loader.get_template('fit/index.html')
    context = {
            'tag_list': tag_list
    }
    return HttpResponse(template.render(context, request))

def list(request, tag=None):

    tag_list = Tag.objects.all()

    if request.user.is_superuser:
        if tag:
            events = Event.objects.filter(event_tag__tag_name=tag).distinct()
        else:
            events = Event.objects.all().distinct()
    else:
        if tag:
            events = Event.objects.filter(event_tag__tag_name=tag).filter(date__gte=datetime.now()).distinct()
        else:
            user_tags = Profile.objects.get(id=request.user.id).profile_tag.all()
            events = Event.objects.filter(event_tag__in=user_tags).filter(is_active=True).filter(date__gte=datetime.now()).distinct() 
    images = []
    for event in events:
        images.append(event.image.name.split('/')[4])
        
    template = loader.get_template("fit/list.html")
    context = {
        'tag_list': tag_list, 
        'events' : zip(events, images)
    }
    return HttpResponse(template.render(context, request))
