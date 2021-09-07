from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import CustomUserCreationForm

# Create your views here.


class RegisterView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('#')