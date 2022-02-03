from django.contrib import admin

from .models import User, Client, Agent, PersonInCompany

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(PersonInCompany)
