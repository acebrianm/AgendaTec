from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Tag(models.Model):
    """
    Stores a single tag entry, it is related with :model:`fit.Event` and
    :model:`fit.Profile`
    """
    tag_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return '%s' %self.tag_name

class Profile(models.Model):
    """
    Stores a single profile entry, it is related with :model:`fit.Tag` 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_tag = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return '%s' %self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ Create a profile entry each time a new user is created. """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """ Saves the user profile each time the user modified. """
    instance.profile.save()

class Event(models.Model):
    """ 
    Stores a single entry for the events, related to model:`fit.Tag`.
    There is a many to many relationship with the model:`fit.Tag`.
    """
    event_name = models.CharField(max_length=30)
    description = models.TextField(max_length=140)
    image = models.ImageField(upload_to='fit/static/fit/images')
    date = models.DateField()
    event_tag = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return '%s' %self.event_name

    class Meta:
        ordering = ['-date']
