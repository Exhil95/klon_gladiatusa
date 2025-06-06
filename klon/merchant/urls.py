from django.urls import path
from . import views

urlpatterns = [
    path('blacksmith/', views.blacksmith_page_view, name='blacksmith_page'),
    path('blacksmith/offer/', views.blacksmith_offer_fragment, name='blacksmith_offer'),
    path('merchant/', views.merchant_view, name='merchant_view'),
    path('blacksmith/buy/<int:offer_id>/', views.buy_offer_view, name='buy_offer'),
    path("blacksmith/sell/<int:item_id>/", views.sell_to_merchant, name="sell_to_merchant"),
    path("blacksmith/backpack-fragment/", views.backpack_fragment, name="backpack_fragment"),



]