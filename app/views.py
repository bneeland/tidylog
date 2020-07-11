from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, resolve
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
        # Get headings for current log
        log_fields_qs = log.fields.all()
        context['fields'] = log_fields_qs
        # Get entries
        entries = models.Entry.objects.filter(log=log)
        context['entries'] = entries

        """
        Let it be known that I spent like 5 hours trying to make this work, and,
        in the end, there was an easy fix (template tags) that I should have found
        much earlier. I just didn't think of googling if there was a better way
        until just now, and them I implemented the right fix in like 5 minutes.
        """
        # entries_list = []
        # i = 0
        # for log_field in log_fields_qs:
        #     entry_values = list(entries.values(log_field.type))
        #     print("entry_values type", type(list(entries.values(log_field.type))))
        #     if i == 0:
        #         entries_list = entry_values
        #     else:
        #         entries_list = list(zip(entries_list, entry_values))
        #         print("entries_list type", type(entries_list))
        #     # entries_list.append(entries.values(log_field.type))
        #     i += 1
        # print("entries_list", entries_list)
        # context['entries'] = entries_list

        # print("ENTRIES_VALUES________", entries.values(log_fields_qs[0].type))

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
            'log_pk': self.kwargs['log_pk'],
        })
        return kwargs

    def get_success_url(self):
        current_url_name = resolve(self.request.path_info).url_name
        cuffent_url_name_complete = 'app:'+current_url_name

        if current_url_name == 'log':
            return reverse_lazy(cuffent_url_name_complete, kwargs={
                'area_pk': self.kwargs['area_pk'],
                'log_pk': self.kwargs['log_pk'],
            })
        elif current_url_name == 'log_1_day':
            return reverse_lazy(cuffent_url_name_complete, kwargs={
                'area_pk': self.kwargs['area_pk'],
                'log_pk': self.kwargs['log_pk'],
                'year': self.kwargs['year'],
                'month': self.kwargs['month'],
                'day': self.kwargs['day'],
            })
        elif current_url_name == 'log_date_range':
            return reverse_lazy(cuffent_url_name_complete, kwargs={
                'area_pk': self.kwargs['area_pk'],
                'log_pk': self.kwargs['log_pk'],
                'year_start': self.kwargs['year_start'],
                'month_start': self.kwargs['month_start'],
                'day_start': self.kwargs['day_start'],
                'year_end': self.kwargs['year_end'],
                'month_end': self.kwargs['month_end'],
                'day_end': self.kwargs['day_end'],
            })

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
