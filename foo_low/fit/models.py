from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Tags(models.Model):
    tag_name = models.CharField(max_length=50)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_tag = models.ManyToManyField(Tags)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Event(models.Model):
    event_name = models.CharField(max_length=30)
    description = models.TextField(max_length=140)
    image = models.ImageField(upload_to='images/', height_field=400, width_field=400)
    date = models.DateField()
    event_tag = models.ManyToManyField(Tags)
