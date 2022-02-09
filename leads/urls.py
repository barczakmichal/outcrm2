from django.urls import path
from .views import ClientList, lead_detail

app_name = "leads"

urlpatterns = [
        path('', ClientList.as_view()),
        path('<pk>', lead_detail),
]
