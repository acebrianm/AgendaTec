from django.forms import ModelForm, CheckboxSelectMultiple
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Profile, Tag, Event

class TagForm(ModelForm):
    profile_tag = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Tag.objects.all().filter(is_active=True))

    class Meta:
        model = Profile
        fields = ['profile_tag']
        
class TagAdminForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name']

class EventForm(ModelForm):
    event_tag = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Tag.objects.all().filter(is_active=True))
    date = forms.DateField(widget = AdminDateWidget())
        
    class Meta:
        model = Event
        fields = ['event_name', 'description', 'image', 'date', 'event_tag']
