from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from app import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
     url(r'^$',views.index, name="home"),
    url(r'^index/$', views.index, name='index')
]