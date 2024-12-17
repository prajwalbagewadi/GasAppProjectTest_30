from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.sign_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('home/',views.home_view,name='home'),
    path('', views.sign_view, name='signup'), #127.0.0.1:8000 page
    path('success/',views.success_view,name='success'),
    path('successuser/',views.successuser_view,name='successuser'),
    path('servicelogin/',views.service_login_view,name='servicelogin'),
    path('service/',views.service_view,name='service'),
]
