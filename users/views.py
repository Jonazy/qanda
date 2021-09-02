from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.


class RegisterView(CreateView):
    template_name = ''
    form_class = ''
    success_url = reverse_lazy('#')