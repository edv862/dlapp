from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from django.contrib.auth.models import User


class UserRegisterView(CreateView):
    model = User
    template_name = 'user-register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home:login')
