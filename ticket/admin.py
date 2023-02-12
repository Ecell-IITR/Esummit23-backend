from django.contrib import admin
from .models import Plan, Payment, Ticket
from user.tasks import send_link_email_task
from django.shortcuts import render
admin.site.register(Plan)
admin.site.register(Payment)


class ticketAdmin(admin.ModelAdmin):
   exclude = ('created', 'updated')
   actions=["sendMail"]


   def sendMail(self, request, queryset):
       print(request.POST)
       if 'submit' in request.POST :
         
         
         for query in queryset:
            email_address = query.Person.email
          
            mail_message= request.POST['message']
            attachment = request.POST['importData']
            mail_subject = request.POST['Subject']
            send_link_email_task.delay( email_address,mail_message,mail_subject,attachment
                )
       return render(request,
                      'mail.html')
        
admin.site.register(Ticket, ticketAdmin)
          

        
# Register your models here.
