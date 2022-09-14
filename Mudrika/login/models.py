from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20)
    dob = models.DateTimeField(auto_now=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.IntegerField(primary_key=True)
    age = models.IntegerField(default=None, blank=True, null=True)
    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = ['dob','username']


    def __str__(self):
        return self.username
