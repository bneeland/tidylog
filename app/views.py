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
        area_pk = self.kwargs['area_pk']
        logs = models.Log.objects.filter(area=area_pk)
        context['logs'] = logs
        return context

# Views

class Home(LoginRequiredMixin, AreasMixin, TemplateView):
    login_url = "login"
    template_name = "app/home.html"

class Area(LoginRequiredMixin, AreasMixin, LogsMixin, TemplateView):
    login_url = "login"
    template_name = "app/area.html"

class Log(LoginRequiredMixin, AreasMixin, LogsMixin, CreateView):
    login_url = "login"
    model = models.Entry
    template_name = "app/log.html"
    form_class = forms.CreateEntryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get area from URL
        area_pk = self.kwargs['area_pk']
        area = models.Area.objects.get(pk=area_pk)
        context['area'] = area
        # Get log from URL
        log_pk = self.kwargs['log_pk']
        log = models.Log.objects.get(pk=log_pk)
        context['log'] = log
        context['entries'] = models.Entry.objects.filter(log=log)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
            'log_pk': self.kwargs['log_pk'],
        })
        return kwargs

    def get_success_url(self):
        return reverse_lazy('app:log', kwargs={'area_pk': self.kwargs['area_pk'], 'log_pk': self.kwargs['log_pk'],})

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
