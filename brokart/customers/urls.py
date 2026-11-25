<<<<<<< HEAD

=======
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
<<<<<<< HEAD
urlpatterns = [
    path('account',views.show_account,name='account'),
    path('logout',views.sign_out,name='logout'),
  
]
=======

urlpatterns = [ 
    path('account', views.show_account, name = 'account'),
]
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
