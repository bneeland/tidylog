from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class Home(LoginRequiredMixin, TemplateView):
    login_url = "login"

    template_name = "app/home.html"
