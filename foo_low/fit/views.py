from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Tag, Profile
from .forms import TagForm

# Create your views here.
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
