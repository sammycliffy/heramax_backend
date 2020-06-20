from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from app import views
from django.contrib.auth import views as auth_views
from app.forms import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name="home"),
    url(r'^index/$', views.index, name='index'),
    url(r'^signup/$', views.SignUp_View.as_view(), name="signup"),
    url(r'^information/$', views.information, name='information'),
    url(r'^predashboard/$', views.predashaboard, name='predashboard'),
    url(r'^profile/$', views.ProfileView.as_view(), name="profile"),
    url(r'^plan/$', views.plan, name="plan"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='app/login.html',
                                                  authentication_form=LoginForm), name='login'),
]
