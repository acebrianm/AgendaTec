from django.contrib import admin
from .models import Profile, Tag, Event

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Event)
