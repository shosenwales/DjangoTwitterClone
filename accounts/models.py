from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'profile_picture')
    bio = models.TextField(default='')

    def __str__(self):
        return f'{self.user.username}'


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
