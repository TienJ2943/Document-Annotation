from django.urls import path
from django.contrib import admin


from . import views

admin.site.site_header = 'Document Annotation Admin'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
]

