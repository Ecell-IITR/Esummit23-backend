from django.contrib import admin
from .models import Services,EventCoordinator,EventsFAQ,EventsPartners,EventRounds

from django.core.mail import send_mail
class AdminRound(admin.ModelAdmin):
    exclude = ('created', 'updated')
    actions = ['send_EMAIL']


    def send_EMAIL(self, request, queryset):
        for query in queryset:
            stp = query.StudentUser
            for user in stp:
                send_mail('Subject here', query.EmailMessage, 'from@example.com',[user.email], fail_silently=False)
        # for i in queryset:
        #     if i.email:
        #         send_mail('Subject here', 'Here is the message.', 'from@example.com',[i.email], fail_silently=False)
            
        
    send_EMAIL.short_description = "Send an email to selected users"
# Register your models here.

admin.site.register(Services)
admin.site.register(EventCoordinator)
admin.site.register(EventRounds,AdminRound)