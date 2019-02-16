from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from authentication.models import *


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        exclude = ['last_login', 'password', 'is_admin',]

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


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        exclude = ['last_login', 'password', 'is_admin']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            if User.objects.filter(email=email).exclude(user_name=self.cleaned_data['user_name']):
                raise forms.ValidationError("User with this Email already exists.")
        return email

    # def clean_password(self):
    #     Regardless of what the user provides, return the initial value.
    #     This is done here, rather than on the field, because the
    #     field does not have access to the initial value
    #     return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('full_name', 'user_name', 'sex', 'mother_name', 'email', 'phone_number', 'educationl_level',
     'is_active', 'is_admin')
    list_filter = ('is_admin', 'is_active', 'sex',)
    fieldsets = (
        (None, {'fields': ('user_name', 'email',)}),
        ('Personal info', {'fields': ('first_name', 'middel_name', 'last_name', 'mother_name', 'place_of_birth', 
        'date_of_birth', 'sex', 'imgage', 'blood_type', 'educationl_level', 'licence_number', 'medical_status', 'career', 
        'marital_status', 'religion', 'disablity','issue_date')}),
        ('Address info', {'fields': ('nationality', 'region',
          'zone', 'wereda', 'kebele', 'home_number', 'phone_number', 'emergency_contact')}),
        ('Permissions', {'fields': ('role',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'middel_name', 'last_name', 'mother_name', 'place_of_birth', 'date_of_birth', 'sex', 
            'imgage', 'blood_type', 'educationl_level', 'licence_number', 'nationality', 'region', 'zone', 'wereda', 'kebele', 
            'home_number', 'phone_number', 'emergency_contact', 'medical_status', 'career', 'marital_status', 'religion', 
            'disablity', 'issue_date', 'role', 'user_name', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('full_name',)
    ordering = ('first_name', 'middel_name')
    filter_horizontal = ('role',)

admin.site.site_title  = 'CID Administraion'
admin.site.site_header = 'Complete ID Digitalization administration'
admin.site.index_title = 'CID administration'
 
# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(Region)
admin.site.register(Zone)
admin.site.register(Wereda)
admin.site.register(Kebele)
admin.site.register(Orgenizaion)
# admin.site.register(Role)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
