from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import ContextMixin

from . import models
from . import forms

# Mixins

class AreasMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(AreasMixin, self).get_context_data(**kwargs)
        areas = models.Area.objects.all()
        context['areas'] = areas
        return context

class LogsMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(LogsMixin, self).get_context_data(**kwargs)
        area = self.kwargs['area']
        logs = models.Log.objects.filter(area=area)
        context['logs'] = logs
        return context

# Views

class Home(LoginRequiredMixin, AreasMixin, LogsMixin, TemplateView):
    login_url = "login"
    template_name = "app/home.html"

# class CreateLog(LoginRequiredMixin, AreasMixin, LogsMixin, CreateView):
#

class Log(LoginRequiredMixin, AreasMixin, LogsMixin, CreateView):
    login_url = "login"
    model = models.Entry
    template_name = "app/log.html"
    # form_class = forms.CreateEntryForm
    success_url = reverse_lazy('app:log')
    fields = ['category']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        log = self.kwargs['log']
        context['entries'] = models.Entry.objects.filter(log=log)
        return context

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
