from django.urls import path
from .import views

urlpatterns = [
    path('',views.thauane),
    path('luis',views.luis),
]
