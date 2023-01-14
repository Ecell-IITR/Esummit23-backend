from django.contrib import admin,messages
from .models import Task, Submission
from user.models.role.ca import CAUser


admin.site.register(Submission)



class TaskAdmin(admin.ModelAdmin):
   exclude = ('created', 'updated')
   actions=["addTask"]


   @admin.action(description='Add task to users')
   def addTask(self, request, queryset):
        for obj  in queryset:
          
          iterateList = CAUser.objects.all()
          for i in iterateList:
            i.taskAssigned.add(obj.pk)
           
               
               


admin.site.register(Task,TaskAdmin)               