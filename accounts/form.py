from django import forms
from .models import Account, UserProfile

class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name','phone_number', 'email', 'password']

    def __init__(self, *args, **kawrgs):
        super(RegistrationForm, self).__init__(*args, **kawrgs )
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone Number'
        for fields in self.fields:
            self.fields[fields].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match'
            )
        
class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')
    def __init__(self, *args, **kawrgs):
        super(UserForm, self).__init__(*args, **kawrgs )
        for fields in self.fields:
            self.fields[fields].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages={'Invalid':("Image file only")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')
    def __init__(self, *args, **kawrgs):
        super(UserProfileForm, self).__init__(*args, **kawrgs )
        for fields in self.fields:
            self.fields[fields].widget.attrs['class'] = 'form-control'