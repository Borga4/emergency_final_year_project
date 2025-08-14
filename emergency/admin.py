from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Staff, Case, EmergencyType

# Customize admin header
admin.site.site_header = "University of Ghana Emergency Response System"
admin.site.site_title = "University of Ghana Emergency Admin Portal"
admin.site.index_title = "Welcome to University of Ghana Emergency Admin"

# Staff Resources and Admin
class StaffResource(resources.ModelResource):
    class Meta:
        model = Staff
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at')
        export_order = fields

@admin.register(Staff)
class StaffAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = StaffResource
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at')
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name', 'email')

# Case Resources and Admin
class CaseResource(resources.ModelResource):
    class Meta:
        model = Case
        fields = ('id', 'title', 'description', 'reported_by', 'status', 'reported_at', 
                 'resolved_at', 'picture', 'latitude', 'longitude', 'emergency_type')
        export_order = fields

@admin.register(Case)
class CaseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CaseResource
    list_display = ('title', 'description', 'reported_by', 'status', 'reported_at', 'resolved_at', 'picture', 'latitude', 'longitude')
    list_filter = ('status', )
    search_fields = ('title', 'description')
    date_hierarchy = 'reported_at'

# EmergencyType Resources and Admin
class EmergencyTypeResource(resources.ModelResource):
    class Meta:
        model = EmergencyType
        fields = ('id', 'emergency_category', 'emergency_type')
        export_order = fields

@admin.register(EmergencyType)
class EmergencyTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EmergencyTypeResource
    list_display = ('emergency_category', 'emergency_type')
    search_fields = ('emergency_category', 'emergency_type')