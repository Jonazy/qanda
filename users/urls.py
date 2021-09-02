from django.urls import path
from users import views
from django.contrib.auth import views as auth_view

app_name = 'users'
urlpatterns = [
    path('login', auth_view.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('register', auth_view.LogoutView.as_view(), name='logout'),
]
