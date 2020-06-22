from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, null=True)
    bank = models.CharField(max_length=255, null=True)
    account_number = models.CharField(max_length=255, null=True)
    account_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.username


class Plan (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    interest = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=False)
    duration = models.CharField(max_length=255, null=True)
    is_approved = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    is_assigned = models.BooleanField(default=False)


class Receiver (models.Model):
    person_to_pay = models.OneToOneField(User, on_delete=models.CASCADE)
    has_received = models.BooleanField(default=False)
    amount = models.PositiveIntegerField(default=0)
    the_receiver = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='Receiver', null=True)
