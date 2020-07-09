from django import forms

from . import models

class CreateEntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('log')
        self.fields.pop('user')
        # Get field codes that are applied to Log
        field_codes = ['CF1', 'CF2',] # This is just a placeholder
        # Get all field codes
        FIELD_BANK = models.Field.FIELD_BANK
        field_codes_all = [fc[0] for fc in FIELD_BANK]
        # Remove unneeded field codes
        field_codes_to_pop = [fc for fc in field_codes_all if fc not in field_codes]
        for field_code_to_pop in field_codes_to_pop:
            self.fields.pop(field_code_to_pop)

        # # Get parameters from URL
        # area_pk = kwargs.pop('user', None)
        # log_pk = kwargs.pop('log_pk', None)
        # print("area_pk:", area_pk)
        # super(CreateEntryForm, self).__init__(*args, **kwargs)
        # log = models.Log.objects.filter(pk=log_pk)
        # # Get list of fields that pertain to this area and log
        # fields_qs = log.fields # ['position', '...']
        # # Get the field codes
        # field_codes = ['']
        # for field in fields_qs:
        #     field_code = models.Field.objects.filter(pk=field)
        #     self.fields += [field_code]
