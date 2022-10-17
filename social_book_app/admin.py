from dataclasses import field
from django.contrib import admin
from .models import UserDetails
from .forms import CustomUserChangeForm, NewUserCreation

# Register your models here.
@admin.register(UserDetails)
class Admin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'public_visibility', 'dob', 'age', 'account_type',
        'address', 'last_login', 'date_joined', 'is_active',
        'is_staff', 'is_admin', 'about'
    )

    search_fields = (
        'username', 'email', 'first_name', 'account_type',
    )

    readonly_fields = ('last_login', 'date_joined')

    list_filter = (
        'is_active', 'is_staff', 'is_admin', 'public_visibility',
    )

    filter_horizontal = ('groups', 'user_permissions')
    add_fieldsets = (None, {'fields': ( 'username', 'email', 'first_name', 'last_name', 'password1', 'password2')})
    model = UserDetails
    form = CustomUserChangeForm
    add_form = NewUserCreation

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        disabled_fields = set()

        if not request.user.is_superuser or not request.user.is_admin:
            disabled_fields |= {
                'is_superuser',
                'is_active',
                'is_staff',
                'is_admin',
                'groups',
                'user_permissions'
            }
            if (
                    (not request.user.is_superuser or not request.user.is_admin)
                    and obj is not None
                    and obj == request.user
            ):
                disabled_fields |= {
                    'is_superuser',
                    'is_staff',
                    'is_admin',
                    'groups',
                    'user_permissions'
                }

            for f in disabled_fields:
                if f in form.base_fields:
                    form.base_fields[f].disabled = True
        return form

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
