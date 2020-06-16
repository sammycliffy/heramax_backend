from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name="home"),
    url(r'^index/$', views.index, name='index'),
    url(r'^signup/$', views.SignUp_View.as_view(), name="signup"),
]
