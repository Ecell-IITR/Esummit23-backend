from django.contrib import admin
from .models.querry import Querry
from user.models.role.startup import StartupUser
from user.models.role.ca import CAUser
from user.models.role.student import StudentUser
from user.models.role.proff import ProffUser
from user.models.otp import OTP
from user.models.person import person
from user.models.teams import teams
from user.models.block import BlockMail,BlockNumber
from user.tasks import send_feedback_email_task
from user.models.teamecell import Teamecell
from io import StringIO 
import csv
from django.http import HttpResponse

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
    actions = ['send_EMAIL']
    def send_EMAIL(self, request, queryset):
        m="""Greeting from E-Cell IITR
This is to inform you that the orientation session for Mind The Product has been scheduled at 10:15 am  IST on 29th January 2023. You will get a first hand experience in product management with latest trends and best practices by senior product managers of MNCs in USA.<br>
This session is compulsory for all the participants of Mind The Product and also open for non-participants.<br>
Join the session  : meet.google.com/cri-ttym-hzi<br>
Date: 29th January <br>
Time: 10:15 AM<br>
Participants are requested to join this whatsapp group: https://chat.whatsapp.com/LrCz6v9BNVAGZdfGga3ehz<br>
<br>
Regards,<br>
Kunal, 9432810879<br>"""
        email_array = []
        for query in queryset:
            stp = query.leader.email
            

            email_array.append(stp)
        send_feedback_email_task.delay(
                email_array, m, 'E-Cell IITR: Orientation Session for Mind The Product')


    

class BlockMailAdmin(admin.ModelAdmin):
    list_filter = ('blockmail',)

class BlockNumberAdmin(admin.ModelAdmin):
    list_filter = ('blocknumber',)

class StartupUserAdmin(UserAdmin):
    actions = ['download_csv']
    def download_csv(self, request, queryset):
    


        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["full_name", "email", "startup_name","phone_number"])

        for querry in queryset:
            phone=""
            try:
                if querry.Person.student:
                    phone=querry.Person.student.phone_number
                elif querry.Person.ca:
                    phone=querry.Person.ca.phone_number
                elif querry.Person.proff:
                    phone=querry.Person.proff.phone_number
            except:
                pass
            writer.writerow([querry.Person,querry.Person.email,querry.quantity,phone,querry.name,querry.plan])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response

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
class PersonAdmin(admin.ModelAdmin):
    exclude = ('created', 'updated')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')

admin.site.register(StartupUser, StartupUserAdmin)
admin.site.register(CAUser, CAUserAdmin)
admin.site.register(StudentUser, StudentUserAdmin)
admin.site.register(ProffUser, ProffUserAdmin)
admin.site.register(OTP)
admin.site.register(Querry)
admin.site.register(person,PersonAdmin)
admin.site.register(teams,TeamAdmin)
admin.site.register(BlockMail,BlockMailAdmin)
admin.site.register(BlockNumber,BlockNumberAdmin)
admin.site.register(Teamecell)
