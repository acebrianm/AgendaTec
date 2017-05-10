from django.forms import ModelForm, CheckboxSelectMultiple
from django import forms
from .models import Profile, Tag

class TagForm(ModelForm):
    profile_tag = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Tag.objects.all())

    class Meta:
        model = Profile
        fields = ['profile_tag']
        
