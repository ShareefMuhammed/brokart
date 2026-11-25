"""
URL configuration for brokart project.

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
=======
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from django.contrib import admin
from django.urls import path,include
=======

from django.contrib import admin
from django.urls import path, include
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('customer/',include('customers.urls')),
    path('orders/',include('orders.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new
=======
    path("admin/", admin.site.urls),
    path('', include('products.urls')),
    path('customer/', include('customers.urls')),
    path('orders/', include('orders.urls'))
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
