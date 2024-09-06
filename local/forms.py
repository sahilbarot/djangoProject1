from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0] != "z":
#         raise forms.ValidationError("The letter should start with z")

class Formname(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.EmailField()
    v_email= forms.EmailField(label="Verify your email")
    phone = forms.CharField(max_length = 100)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data= super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['v_email']

        if email != v_email:
            raise forms.ValidationError("The email and v_email should match")