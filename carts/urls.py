from django.urls import path

from carts.views import cart_home, cart_update, checkout, checkout_done_view, view_cart

urlpatterns = [
    path('', cart_home, name='carts'),
    path('update', cart_update, name='update'),
    path('checkout', checkout, name='checkout'),
    path('checkout/success/', checkout_done_view, name='success'),
    path('viewcart/<int:pk>/', view_cart, name='viewcart')
    


]
