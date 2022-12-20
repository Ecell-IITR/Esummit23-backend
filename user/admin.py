from django.contrib import admin
from .models.querry import Querry
from user.models.role.startup import StartupUser
from user.models.role.ca import CAUser
from user.models.role.student import StudentUser
from user.models.role.proff import ProffUser
from user.models.otp import OTP
from user.models.person import person
from user.models.teams import teams

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    exclude = ('created', 'updated','authToken')
    list_filter = ('email',"esummit_id")
class TeeamAdmin(admin.ModelAdmin):
    exclude = ('created', 'updated')
    list_filter = ('name','event')
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
admin.site.register(OTP)
admin.site.register(Querry)
admin.site.register(person)
admin.site.register(teams)

