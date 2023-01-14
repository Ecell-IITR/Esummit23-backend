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


class Members(admin.TabularInline):
    model = teams.members.through
    extra = 3


class UserAdmin(admin.ModelAdmin):
    exclude = ('created', 'updated', 'authToken')
    list_filter = ('email', "esummit_id")


class TeamAdmin(admin.ModelAdmin):
    exclude = ('created', 'updated',"members")
    list_filter = ('name', 'event')
    inlines = [Members]


class StartupUserAdmin(UserAdmin):
    pass

class StudentUserAdmin(UserAdmin):
    pass

class ProffUserAdmin(UserAdmin):
    pass

class CaTaskCompletedInlines(admin.TabularInline):
    model = CAUser.taskCompleted.through
    verbose_name_plural = "Task Completed"
    extra = 2

class CaTaskAssignedInlines(admin.TabularInline):
    model = CAUser.taskAssigned.through
    verbose_name_plural = "Task Assigned"
    extra = 1
class CAUserAdmin(UserAdmin):
    
    inlines = [CaTaskCompletedInlines,CaTaskAssignedInlines]
    exclude = ['created', 'updated', 'authToken','taskCompleted','taskAssigned']
    extra=2


admin.site.register(StartupUser, StartupUserAdmin)
admin.site.register(CAUser, CAUserAdmin)
admin.site.register(StudentUser, StudentUserAdmin)
admin.site.register(ProffUser, ProffUserAdmin)
admin.site.register(OTP)
admin.site.register(Querry)
admin.site.register(person)
admin.site.register(teams,TeamAdmin)
