from django.urls import path
from users import views
from django.contrib.auth import views as auth_view

app_name = 'users'
urlpatterns = [
    path('login', auth_view.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('forgot-password', auth_view.PasswordResetView.as_view(), name='forgot-password'),
    path('password-reset-link-done', auth_view.PasswordResetDoneView.as_view(), name='password-reset-link-done'),
    path('password-reset', auth_view.PasswordChangeView.as_view(), name='reset-password'),
    path('logout', auth_view.LogoutView.as_view(), name='logout'),
]
