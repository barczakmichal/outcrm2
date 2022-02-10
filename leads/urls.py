from django.urls import path
from .views import ClientList, ClientAdd, lead_detail, lead_create

app_name = "leads"

urlpatterns = [
        path('', ClientList.as_view()),
        path('create/', lead_create),
        path('<int:pk>', lead_detail),
]
