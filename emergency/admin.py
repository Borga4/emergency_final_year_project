# Register your models here.
from django.contrib import admin
from .models import Staff, Case, EmergencyType


admin.site.site_header = "University of Ghana Emergency Response System"
admin.site.site_title = "University of Ghana Emergency Admin Portal"
admin.site.index_title = "Welcome to University of Ghana Emergency Admin"

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at')
    
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'reported_by', 'status', 'reported_at', 'resolved_at', 'picture', 'latitude', 'longitude')

class EmergencyTypeAdmin(admin.ModelAdmin):
    list_display = ('emergency_category', 'emergency_type')

admin.site.register(Staff, StaffAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(EmergencyType, EmergencyTypeAdmin)

