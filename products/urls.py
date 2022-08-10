"""products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.conf import settings

from django.contrib import admin
from django.urls import path,include
from categoryz import views
from accounts import urls
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Cart/',include('carts.urls')),
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='cat_list'),
    path('<slug:c_slug>/<slug:product_slug>',views.proddetails,name='proddetails'),
    path('search/?q',views.searching,name='searching'),
    path('accounts/',include('accounts.urls'))

    
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
