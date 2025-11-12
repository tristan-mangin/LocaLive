from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from .models import CustomUser

# Customize the admin site headers and titles
admin.site.site_header = getattr(settings, 'ADMIN_SITE_HEADER', 'Django Administration')
admin.site.site_title = getattr(settings, 'ADMIN_SITE_TITLE', 'Django Site Admin')
admin.site.index_title = getattr(settings, 'ADMIN_INDEX_TITLE', 'Site Administration')

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for our CustomUser model.
    Extends Django's built-in UserAdmin to include extra fields (bio, profile_image).

    http://127.0.0.1:8000/admin/users/customuser/
    """

    # Define how the user detail page looks in the admin panel
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_image')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Define what fields are shown when adding a new user via admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'bio', 'profile_image'),
        }),
    )

    # List view configuration (what columns show up in /admin/users/customuser)
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)

    def profile_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="40" height="40" style="border-radius: 50%;" />', obj.profile_image.url)
        return "-"
    profile_preview.short_description = "Profile Image"

    list_display = ('username', 'email', 'is_staff', 'profile_preview', 'date_joined')
