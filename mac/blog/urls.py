from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('products/<int:myid>', views.productView, name = 'productView')
]