<<<<<<< HEAD

=======
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
<<<<<<< HEAD
urlpatterns = [
    path('cart',views.show_cart,name='cart'),
    path('orders',views.show_orders,name='orders'),

    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('remove_item/<pk>',views.remove_item_from_cart,name='remove_item'),
    path('checkout',views.checkout_cart,name='checkout')

]
=======

urlpatterns = [ 
    path('cart', views.show_carts, name = 'cart'),
]
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
