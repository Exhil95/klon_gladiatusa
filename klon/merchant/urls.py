from django.urls import path
from . import views

urlpatterns = [
    path('', views.merchant_list, name='merchant_list'),
]