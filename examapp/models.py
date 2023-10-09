from django.contrib.auth.models import User, Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    ACCOUNT_TYPE = (
        ('officer', 'Officer'),
        ('centers', 'Centers'),
        ('examiner', 'Examiner'),
    )
    actype = models.CharField(max_length=50, choices=ACCOUNT_TYPE)
    name = models.CharField(max_length=100)
    # email = models.EmailField()
    centername = models.CharField(max_length=100)
    branch= models.CharField(max_length=100)

    def __str__(self):
        return self.username











