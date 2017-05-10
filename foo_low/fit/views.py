from django.shortcuts import render
from django.template import loader
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tag, Profile
from .forms import TagForm
from datetime import datetime

# Models
from .models import Profile, Tag, Event

# Index redirection in the website.
def index(request):
    if not request.user.is_authenticated:
        template = loader.get_template('fit/login.html')
        context ={}
        return HttpResponse(template.render(context, request))

    else:
        # Template render
        template = loader.get_template('fit/index.html')
        tag_list = Tag.objects.all()
        context = {
            'tag_list': tag_list
        }
        return HttpResponse(template.render(context, request))

# Log in
def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    print(username)
    print(password)
    if user is not None:
        login(request, user)
        return index(request)
    else:
        messages.error(request, 'Wrong username or password.')
        return index(request)

# Log out
def log_out(request):
    logout(request)
    return index(request)

# Webpage to follow or unfollow interests.
def my_account(request):

    # Data from tags
    tags = Tag.objects.all()

    # Data from user
    current_user = request.user
    username = current_user.username
    current_profile = Profile.objects.get(user=current_user)
    sel_tags = current_profile.profile_tag.all()

    # Template render
    template = loader.get_template('fit/my_account.html')
    
    # Create the form
    if request.method == 'POST':
        form = TagForm(request.POST or None,
                       request.FILES or None,
                       instance=current_profile,)
        if form.is_valid():
            form.save()
        
    else:
        form = TagForm(instance=current_profile)

    # Context for rendering
    context = {
        'tags' : tags,
        'username' : username,
        'sel_tags' : sel_tags,
        'form' : form,
    }

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
