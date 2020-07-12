from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, resolve
from django.views.generic.base import ContextMixin
from django.utils import timezone
from django.conf import settings
import datetime

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

        # Get headings for current log
        log_fields_qs = log.fields.all()
        context['fields'] = log_fields_qs

        # Get entries
        entries = models.Entry.objects.filter(log=log)

        # Filter for 1-day / date-range views
        url_name = resolve(self.request.path_info).url_name
        context['url_name'] = url_name

        if url_name == "log_1_day":
            year = self.kwargs['year']
            month = self.kwargs['month']
            day = self.kwargs['day']

            date = timezone.make_aware(datetime.datetime(year, month, day))

            date_remove = date - datetime.timedelta(days=1)
            date_add = date + datetime.timedelta(days=1)
            context['date_remove'] = date_remove
            context['date_add'] = date_add

            # context['year'] = year
            # context['month'] = month
            # context['day'] = day

            # entries = entries.filter(created_at__date=timezone.localdate(year, month, day))
            entries = entries.filter(created_at__date=timezone.localtime(date))

        if url_name == "log_date_range":
            year_start = self.kwargs['year_start']
            month_start = self.kwargs['month_start']
            day_start = self.kwargs['day_start']
            year_end = self.kwargs['year_end']
            month_end = self.kwargs['month_end']
            day_end = self.kwargs['day_end']

            date_start = timezone.make_aware(datetime.datetime(year_start, month_start, day_start))
            date_end = timezone.make_aware(datetime.datetime(year_end, month_end, day_end+1))

            # context['year_start'] = year_start
            # context['month_start'] = month_start
            # context['day_start'] = day_start
            # context['year_end'] = year_end
            # context['month_end'] = month_end
            # context['day_end'] = day_end

            entries = entries.filter(
                created_at__gte=timezone.localtime(timezone.localtime(date_start)),
                created_at__lt=timezone.localtime(timezone.localtime(date_end)),
            )

        context['entries'] = entries

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
            'log_pk': self.kwargs['log_pk'],
        })
        return kwargs

    def get_success_url(self):
        url_name = resolve(self.request.path_info).url_name
        url_name_complete = 'app:'+url_name

        if url_name == 'log':
            return reverse_lazy(url_name_complete, kwargs={
                'area_pk': self.kwargs['area_pk'],
                'log_pk': self.kwargs['log_pk'],
            })
        elif url_name == 'log_1_day':
            return reverse_lazy(url_name_complete, kwargs={
                'area_pk': self.kwargs['area_pk'],
                'log_pk': self.kwargs['log_pk'],
                'year': self.kwargs['year'],
                'month': self.kwargs['month'],
                'day': self.kwargs['day'],
            })
        elif url_name == 'log_date_range':
            return reverse_lazy(url_name_complete, kwargs={
                'area_pk': self.kwargs['area_pk'],
                'log_pk': self.kwargs['log_pk'],
                'year_start': self.kwargs['year_start'],
                'month_start': self.kwargs['month_start'],
                'day_start': self.kwargs['day_start'],
                'year_end': self.kwargs['year_end'],
                'month_end': self.kwargs['month_end'],
                'day_end': self.kwargs['day_end'],
            })
