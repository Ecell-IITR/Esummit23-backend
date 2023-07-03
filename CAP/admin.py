from django.contrib import admin,messages
from CAP.models.submission import Submission
from CAP.models.tasks import Task
from user.models.role.ca import CAUser


class SubmissionAdmin(admin.ModelAdmin):
  exclude=('points','created')




class TaskAdmin(admin.ModelAdmin):
   exclude = ('created', 'updated','task_id')
   actions=["addTask"]


   @admin.action(description='Assign task to users')
   def addTask(self, request, queryset):
        for obj  in queryset:
          
          iterateList = CAUser.objects.all()
          for i in iterateList:
            i.taskAssigned.add(obj.pk)
           
               
               


admin.site.register(Task,TaskAdmin)               
admin.site.register(Submission,SubmissionAdmin)