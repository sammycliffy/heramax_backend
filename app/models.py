from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255, null=True, )
    lastname = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.firstname
