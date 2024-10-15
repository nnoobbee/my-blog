"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.conf.urls import include, url
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'', include('blog.urls')),
# ]

from django.contrib import admin
from django.urls import path
from blog.views import qwe
from django.conf.urls import include
# from django.conf.urls import utl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qwe', qwe),
    # path(r'^admin/', include(admin.site.urls)),
    path(r'', include('blog.urls')),
]
