from django.urls import path
from . import views

urlpatterns = [
    path('blacksmith/', views.blacksmith_page_view, name='blacksmith_page'),
    path('blacksmith/offer/', views.blacksmith_offer_fragment, name='blacksmith_offer'),
    path('merchant/', views.merchant_view, name='merchant_view'),
    path('blacksmith/buy/<int:offer_id>/', views.buy_offer_view, name='buy_offer'),
    path("blacksmith/sell/<int:item_id>/", views.sell_to_merchant, name="sell_to_merchant"),
    path("blacksmith/backpack-fragment/", views.backpack_fragment, name="backpack_fragment"),
    path("alchemist/", views.alchemist_page_view, name="alchemist"),
    path("alchemist/buy/<int:offer_id>/", views.buy_offer_alchemist, name="buy_offer_alchemist"),
    path("alchemist/sell/<int:item_id>/", views.sell_to_alchemist, name="sell_to_alchemist"),
    path("alchemist/backpack-fragment/", views.backpack_fragment_alchemist, name="backpack_fragment_alchemist"),
    path('blacksmith/offers/', views.blacksmith_offer_fragment, name='blacksmith_offer_fragment'),


]