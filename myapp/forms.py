from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import ContactMessage

class ContactForm(forms.ModelForm):  # Using ModelForm instead of Form
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    helper = FormHelper()
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Submit'))
