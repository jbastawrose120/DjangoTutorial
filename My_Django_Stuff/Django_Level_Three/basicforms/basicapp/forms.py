from django import forms
from django.core import validators

# We can do it better still if we want a validator that cleans an entire form!
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify your Email: ')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Emails do not match!")

    #botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,
    #                            validators=[validators.MaxLengthValidator(0)])

    #Never actually going to use this method of form validation
    #use validators from django.core
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
