from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from . import forms

# Create your views here.

class SingUp(CreateView):
    form_class = forms.UserCreateForm
    sucess_url = reverse('login')
    template_name = 'accounts/signup.html'
