from django.urls import path
from . import views

urlpatterns = [
    path('blacksmith/', views.blacksmith_offer_view, name='blacksmith_offer'),
    path('merchant/', views.merchant_view, name='merchant_view'),
]