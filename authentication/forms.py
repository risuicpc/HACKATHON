from django import forms
from .models import *


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        exclude = ['last_login', 'password', 'is_admin', 'is_active']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            if User.objects.filter(email=email).exclude(user_name=self.cleaned_data['user_name']):
                raise forms.ValidationError("User with this Email already exists.")
        return email

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ZoneCreateForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=None, required=False)
    class Meta:
        model = Zone
        fields ='__all__'

class WeredaCreationForm(forms.ModelForm):
    zone = forms.ModelChoiceField(queryset=None, required=False)
    class Meta:
        model = Wereda
        fields ='__all__'

class KebeleCreationForm(forms.ModelForm):
    wereda = forms.ModelChoiceField(queryset=None, required=False)
    class Meta:
        model = Kebele
        fields ='__all__'
        

class UserCreationExel(forms.Form):
    exelfile = forms.FileField(label="Upload File", help_text="admin student teacher family")

    def clean_exelfile(self):
        exelfile = self.cleaned_data.get("exelfile")  
        
        if str(exelfile)[-4:] != '.csv':
            raise forms.ValidationError("This file was not exel(.csv).")
        return exelfile