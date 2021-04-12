from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
        'last_login',
    ]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )


admin.site.register(User, CustomUserAdmin)
