from django.forms import ModelForm
from .models import QuoteModel,Drivers

#my forms

class QuoteModelForms(ModelForm):
    class Meta:
        model = QuoteModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'name'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['tel'].widget.attrs['placeholder'] = '+1(__)-__-__'
        self.fields['company_name'].widget.attrs['placeholder'] = 'company name'
        self.fields['mc'].widget.attrs['placeholder'] = 'mc#'

class RegisterModelForms(ModelForm):
    class Meta:
        model = Drivers
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['driver_license'].widget.attrs['placeholder'] = 'Driver license number'
        self.fields['state'].widget.attrs['placeholder'] = 'State'
        self.fields['driving_information'].widget.attrs['placeholder'] = 'Driving information'
        self.fields['how_many_years'].widget.attrs['placeholder'] = 'How many years of verifiable commercial truck driving experience do you have?'