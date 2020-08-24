from django.contrib import admin

from . import models


class EntryAdmin(admin.ModelAdmin):
    model = models.Entry
    list_display = ['created_at', 'log', 'user', 'category', 'status',]

class AcknowledgementAdmin(admin.ModelAdmin):
    model = models.Acknowledgement
    list_display = ['for_date', 'created_at', 'log', 'user', 'group',]

class FieldAdmin(admin.ModelAdmin):
    model = models.Field
    list_display = ['name', 'type', 'shown_in_table',]

class AcknowledgementFieldAdmin(admin.ModelAdmin):
    model = models.AcknowledgementField
    list_display = ['name', 'type',]

admin.site.register(models.NewUser)
admin.site.register(models.Area)
admin.site.register(models.Log)
admin.site.register(models.Field, FieldAdmin)
admin.site.register(models.AcknowledgementField, AcknowledgementFieldAdmin)
admin.site.register(models.Category)
admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Acknowledgement, AcknowledgementAdmin)
