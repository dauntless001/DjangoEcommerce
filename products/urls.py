from django.urls import path
from . import views


app_name = 'products'


urlpatterns = [
    path('', views.home_view, name='home'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop/', views.product_list, name='products_list'),
    path('shop/wishlist/', views.wishlist_view, name='wishlist_view'),
    path('shop/<str:slug>/', views.product_detail, name='products_details'),
    path('shop/<str:slug>/add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('shop/<str:slug>/remove-from-wishlist/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('shop/<str:slug>/add-to-cart/', views.add_to_cart_view, name='add_to_cart'),
    path('shop/<int:id>/remove-from-cart/', views.remove_from_cart_view, name='remove_from_cart'),
    path('contact-us/', views.contact_view, name='contact-us'),
    path('search/', views.search_view, name='search'),
]