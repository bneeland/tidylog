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
        self.fields.pop('status')

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

        # Set field labels
        for code in log_field_codes:
            self.fields[code].label = models.Field.objects.filter(type=code)[0].name

    def save(self):
        entry = super(CreateEntryForm, self).save(commit=False)
        entry.user = self.user
        entry.log = models.Log.objects.filter(pk=self.log_pk)[0]
        entry.status = 'UR'
        entry.save()
        return entry

class CreateAcknowledgementForm(forms.ModelForm):
    class Meta:
        model = models.Acknowledgement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.log_pk = kwargs.pop('log_pk', None)
        self.group = kwargs.pop('group', None)

        super().__init__(*args, **kwargs)

        self.fields.pop('user')
        self.fields.pop('log')
        self.fields.pop('group')

        # Get field codes that are applied to Acknowledgement
        log_qs = models.Log.objects.filter(pk=self.log_pk)
        log = log_qs[0]

        if self.user.groups.all()[0].name == 'Unit lead':
            acknowledgement_fields_qs = log.unit_lead_acknowledgement_fields.all()
        elif self.user.groups.all()[0].name == 'Superintendent':
            acknowledgement_fields_qs = log.superintendent_acknowledgement_fields.all()
        elif self.user.groups.all()[0].name == 'Engineering':
            acknowledgement_fields_qs = log.engineering_acknowledgement_fields.all()
        elif self.user.groups.all()[0].name == 'Operator':
            acknowledgement_fields_qs = log.new_shift_acknowledgement_fields.all()
            
        acknowledgement_field_codes = [acknowledgement_field.type for acknowledgement_field in acknowledgement_fields_qs]

        # Get all field codes
        FIELD_BANK = models.AcknowledgementField.FIELD_BANK
        field_codes_all = [fc[0] for fc in FIELD_BANK]

        # Remove unneeded field codes
        field_codes_to_pop = [fc for fc in field_codes_all if fc not in acknowledgement_field_codes]
        for field_code_to_pop in field_codes_to_pop:
            self.fields.pop(field_code_to_pop)

        # Set field labels
        for code in acknowledgement_field_codes:
            self.fields[code].label = models.AcknowledgementField.objects.filter(type=code)[0].name

    def save(self):
        entry = super(CreateAcknowledgementForm, self).save(commit=False)
        entry.user = self.user
        entry.log = models.Log.objects.filter(pk=self.log_pk)[0]
        entry.group = self.user.groups.all()[0]
        entry.save()
        return entry
