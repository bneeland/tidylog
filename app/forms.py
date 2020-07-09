from django import forms

from . import models

class CreateEntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.log_pk = kwargs.pop('log_pk', None)
        super().__init__(*args, **kwargs)
        self.fields.pop('user')
        self.fields.pop('log')
        # Get field codes that are applied to Log
        log_qs = models.Log.objects.filter(pk=self.log_pk)
        log = log_qs[0]
        log_fields_qs = log.fields.all()
        log_field_codes = [log_field.type for log_field in log_fields_qs]
        # Get all field codes
        FIELD_BANK = models.Field.FIELD_BANK
        field_codes_all = [fc[0] for fc in FIELD_BANK]
        # Remove unneeded field codes
        field_codes_to_pop = [fc for fc in field_codes_all if fc not in log_field_codes]
        for field_code_to_pop in field_codes_to_pop:
            self.fields.pop(field_code_to_pop)

    
