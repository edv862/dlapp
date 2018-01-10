from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User

from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    model = User
    template_name = 'user-register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
