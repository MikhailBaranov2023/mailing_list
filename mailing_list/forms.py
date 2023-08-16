from django import forms
from mailing_list.models import MailingList


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FormMailingList(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingList
        fields = '__all__'
