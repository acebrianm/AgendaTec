from django.forms import ModelForm, CheckboxSelectMultiple
from django import forms
from .models import Profile, Tag

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
