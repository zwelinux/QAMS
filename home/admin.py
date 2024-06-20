from django.contrib import admin
from .models import  Dr ,Attendance, Attendance_List, Leave, Leave_List, Subject


# @admin.register(Leave)
# class LeaveAdmin(admin.ModelAdmin):
#     list_display = ['dr', 'date', 'session']
#     prepopulated_fields = {'slug': ('session',)}
#     list_filter = ['session', 'date']
#     search_fields = ['session', 'date']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['dr', 'date', 'session']
    prepopulated_fields = {'slug': ('session',)}
    list_filter = ['session', 'date']
    search_fields = ['session', 'date']


@admin.register(Attendance_List)
class AttendanceListAdmin(admin.ModelAdmin):
    list_display = ['user', 'dr', 'loginid']
    list_filter = ['created_at', 'user', 'dr']
    search_fields = ['loginid'] # Search id

# @admin.register(Leave_List)
# class LeaveListAdmin(admin.ModelAdmin):
#     list_display = ['user', 'dr', 'loginid']
#     list_filter = ['created_at', 'user', 'dr']
#     search_fields = ['loginid'] # Search id


@admin.register(Dr)
class DrAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
