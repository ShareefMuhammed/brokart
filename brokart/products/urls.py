<<<<<<< HEAD

=======
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
<<<<<<< HEAD
urlpatterns = [
    path('', views.index,name='home'),
    path('product_list',views.list_products,name='list_product'),
    path('product_details/<pk>',views.detail_product,name='detail_product')

]
=======

urlpatterns = [ 
    path('', views.index, name = 'home'),
    path('product_list', views.list_products, name = 'list_products'),
    path('product_details/<pk>', views.detailed_product, name = 'detail_product')
]
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
