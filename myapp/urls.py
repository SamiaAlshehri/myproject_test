# myapp/urls.py

from django.urls import path
from .views import MyAPIView

urlpatterns = [
    path('items/', MyAPIView.as_view(), name='items'),
]
