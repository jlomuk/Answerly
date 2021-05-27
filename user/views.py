from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('qanda:today_questions')
