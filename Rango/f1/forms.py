from django import forms

from .models import SignUp, Contact

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['fullname','email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        return subject

    def clean_message(self):
        message = self.cleaned_data.get('message')
        return message
