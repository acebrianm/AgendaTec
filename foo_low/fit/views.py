from django.shortcuts import render
from django.template import loader
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tag, Profile
from .forms import TagForm

# Index redirection in the website.
def index(request):

    if not request.user.is_authenticated:
        template = loader.get_template('fit/login.html')
        context ={}
        return HttpResponse(template.render(context, request))

    else:
        # Template render
        template = loader.get_template('fit/index.html')
        context = {
            'tag_list': ["Sports", "culture"]
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

    # Render the webpage
    return HttpResponse(template.render(context, request))
