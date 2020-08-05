from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from model.models.user import User, Customer, VendorOwner, Cook, Manager


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'date_of_birth', 'user_type')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            user_type = user.user_type
            if user_type == 1:
                Customer.objects.set_user(user=user, user_type=user_type)
            elif user_type == 2:
                Cook.objects.set_user(user=user, user_type=user_type)
            elif user_type == 3:
                VendorOwner.objects.set_user(user=user, user_type=user_type)
            elif user_type == 4:
                Manager.objects.set_user(user=user, user_type=user_type)
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'user_type', 'is_admin', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'user_type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'user_type', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class CustomerAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('user', 'balance')
    fieldsets = (
        (None, {'fields': ('user', 'balance')}),
        # ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'balance'),
        }),
    )
    # search_fields = ('user',)
    ordering = ('user',)
    filter_horizontal = ()


class CookAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('user', 'work_for')
    fieldsets = (
        (None, {'fields': ('user', 'work_for')}),
        # ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'work_for'),
        }),
    )
    # search_fields = ('user',)
    ordering = ('user',)
    filter_horizontal = ()


class VOAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('user',)
    fieldsets = (
        (None, {'fields': ('user',)}),
        # ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user',),
        }),
    )
    # search_fields = ('user',)
    ordering = ('user',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cook, CookAdmin)
admin.site.register(VendorOwner, VOAdmin)
# admin.site.register(Manager)

admin.site.unregister(Group)
