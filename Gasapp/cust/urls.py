from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('home/',views.home_view,name='home'),
    path('', views.login_view, name='login'),
    path('success/',views.success_view,name='success'),
    path('service/',views.service_view,name='service'),
]
