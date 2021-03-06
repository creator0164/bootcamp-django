"""bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from products.views import (
    bad_view,
    search_view,
    product_create_view,
    home_view,
    product_detail_view,
    product_json_detail_view,
    product_list_view,
)

from profiles.views import (
    profile_detail_view,
)

urlpatterns = [
    path('bad-view-dont-use/', bad_view),
    path('search/', home_view),
    path('products-create/', product_create_view),
    path('search-view/', search_view),
    path('products/<int:pk>/', product_detail_view),
    re_path(r'api/products/(?P<pk>\d+)/', product_json_detail_view),
    path('profile/user/', profile_detail_view),
    path('products/', product_list_view),
    path('admin/', admin.site.urls),
]
