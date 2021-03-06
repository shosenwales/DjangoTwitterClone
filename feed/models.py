from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class tweet(models.Model):
    text = models.TextField(max_length=200, default='', null=True)
    datetime = models.DateTimeField(default=timezone.now)
    handle = models.ForeignKey(User,on_delete=models.CASCADE)