from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #1 agent = 1 user

class Lead(models.Model):

    company_name = models.CharField(max_length=30)
    name_surname = models.CharField(max_length=30)
    age = models.SmallIntegerField(default=0)
    email = models.EmailField(blank=True)
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)  # all leads neet to have owner
    phoned = models.BooleanField(default=False) 
    # SOURCE_CHOUICES = (
    #     ('FB', 'Facebook'),
    #     ('Ads', "Google Ads"),
    #     ('NSL', 'Newsletter'),
    #     ('Other', 'Other'),
    # )
    # source = models.CharField(choices=SOURCE_CHOUICES, max_length=100, default=True)    
         
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)