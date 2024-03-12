from apps.users.models import License, MasterConfig, Profile, StatusCode, StatusConfig, TeamLeader, User, UserRole, WorkflowConfig
from django.contrib import admin
from django.contrib.auth import admin as auth_admin

# Register your models here.
class UserAdmin(auth_admin.UserAdmin):
    list_display = (
        'email', 'username', 'role', 'date_joined', 'last_login', 'is_admin', 'is_staff'
        )
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserRoleAdmin(admin.ModelAdmin):        
    list_display = ('id','role_name')

admin.site.register(User, UserAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(Profile)
admin.site.register(TeamLeader)
admin.site.register(MasterConfig)
admin.site.register(License)
admin.site.register(StatusCode)
admin.site.register(StatusConfig)
admin.site.register(WorkflowConfig)