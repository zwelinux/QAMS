from django.contrib import admin
from .models import  Dr ,Attendance, Attendance_List, Leave, Leave_List, Subject, Calculation


admin.site.site_header = 'QAMS'
admin.site.site_title = 'QAMS'

from accounts.models import Account

from .models import Student, Percentage

class PercentageInline(admin.TabularInline):
    model = Percentage
    extra = 1
class CalculationAdmin(admin.ModelAdmin):

    list_display = ['student_name', 'present_date', 'total_date', 'rollcall']

admin.site.register(Calculation, CalculationAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'attendance_percentage')
    inlines = [PercentageInline]

    def attendance_percentage(self, obj):
        return f"{obj.attendance_percentage:.2f}%"
    attendance_percentage.short_description = 'Attendance Percentage'

admin.site.register(Student, StudentAdmin)
# admin.site.register(Percentage)


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
    
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superadmin:
            return qs
        return qs.filter(responsibility=request.user.id)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.responsibility = request.user
        obj.save()

    def has_view_permission(self, request, obj=None):
        has_class_permission = super().has_view_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superadmin:
            return obj.responsibility == request.user
        return True
    
    def has_change_permission(self, request, obj=None):
        has_class_permission = super().has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superadmin:
            return obj.responsibility == request.user
        return True
    
    def has_delete_permission(self, request, obj=None):
        has_class_permission = super().has_delete_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superadmin:
            return obj.responsibility == request.user
        return True
    
    list_display = ['date', 'session']
    prepopulated_fields = {'slug': ('session',)}
    list_filter = ['session', 'date']
    search_fields = ['session', 'date']


@admin.register(Attendance_List)
class AttendanceListAdmin(admin.ModelAdmin):
    list_display = ['user', 'dr', 'loginid', 'qrcode']
    list_filter = ['created_at', 'user', 'dr', 'realated_subject__name']
    search_fields = ['loginid'] # Search id

# @admin.register(Leave_List)
# class LeaveListAdmin(admin.ModelAdmin):
#     list_display = ['user', 'dr', 'loginid']
#     list_filter = ['created_at', 'user', 'dr']
#     search_fields = ['loginid'] # Search id


@admin.register(Dr)
class DrAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}