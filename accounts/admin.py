from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account 

from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin

# Unregister the existing Group model
admin.site.unregister(Group)

# Custom GroupAdmin if needed
class CustomGroupAdmin(GroupAdmin):
    pass

# Register Group model again
admin.site.register(Group, CustomGroupAdmin)

class AccountAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'student','is_admin', 'is_active']
    readonly_fields = ['date_joined', 'last_login', ]
    ordering = ('-date_joined_for_format',)
    list_filter = ['student','is_admin', 'is_active']


    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

