from django.contrib import admin
from user.models.role.startup import StartupUser
from user.models.role.ca import CAUser
from user.models.role.student import StudentUser
from user.models.role.proff import ProffUser
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    exclude = ('created', 'updated', 'password','authToken')
    list_filter = ('email',"esummit_id")
class StartupUserAdmin(UserAdmin):
    pass
class CAUserAdmin(UserAdmin):
    pass  
class StudentUserAdmin(UserAdmin):
    pass
class ProffUserAdmin(UserAdmin):
    pass

admin.site.register(StartupUser, StartupUserAdmin)
admin.site.register(CAUser, CAUserAdmin)
admin.site.register(StudentUser, StudentUserAdmin)
admin.site.register(ProffUser, ProffUserAdmin)