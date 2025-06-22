from django.contrib import admin
from .models import Order, Service, Comment, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)

admin.site.register(Order)
admin.site.register(Service)
admin.site.register(Comment)
