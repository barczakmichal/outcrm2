from datetime import datetime
import email
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.views import View
from .models import Client as Client

def client_list(request):
    client_list = Client.objects.all()
    context = {
        "client_list":client_list
        }
    return render(request, "clients/list_client.html", context)


def lead_detail(request, pk):
    client = Client.objects.get(id=pk)
    context = {
        "client":client
        }
    return render(request, "leads/client_detail.html", context)

class ClientAdd(View):

    def get(self, request):
        return render(request, 'add_client.html')

    def post(self, request):
        short_name = request.POST.get('short_name')
        full_name = request.POST.get('full_name')
        city = request.POST.get('city')
        website = request.POST.get('website')
        tax_number = request.POST.get('tax_number')
        email = request.POST.get('email')
        status = request.POST.get('status')

        Client.objects.create(short_name=short_name,
                             full_name=full_name,
                             city=city,
                             website=website,
                             tax_number=tax_number,
                             email=email,
                             status=status)

        context = {'message':'Dodano do bazy'}

        return render(request, "list_client_code.html", context)

class ClientList(View):

    def get(self, request):
        client_list = Client.objects.all()
        print(client_list)
        return render(request, 'list_client.html', context={'client_list': client_list})
