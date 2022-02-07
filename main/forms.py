from django.forms import ModelForm
from .models import QuoteModel

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

