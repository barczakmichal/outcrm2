from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #1 agent = 1 client

    def __str__(self):
        return self.user.email

class Client(models.Model):

    short_name = models.CharField(max_length=64, unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    website = models.CharField(max_length=64)
    tax_number = models.PositiveBigIntegerField(max_length=10,unique=True)
    email = models.EmailField(blank=True)
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)  # all leads/client neet to have owner
    phoned = models.BooleanField(default=False) 
    source_lead = models.CharField(max_length=64)
    status = models.CharField(max_length=32)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_name}"

class PersonInCompany(models.Model):
    surname = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    phone_number = models.SmallIntegerField(max_length=10,unique=True)
    email = models.EmailField(max_length=64)
    position = models.CharField(max_length=64)
    notes = models.CharField(max_length=64)
    company = models.ForeignKey("Client", on_delete=models.SET_NULL, null=True)  # all person neet to have company)

    def __str__(self):
        return f'{self.name} {self.surname}'
