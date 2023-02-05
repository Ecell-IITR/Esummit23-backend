from django.contrib import admin
from .models import Plan, Payment, Ticket,ReffealCode

class Reffreal(admin.ModelAdmin):
    exclude = ( 'usage',)
    list_display = ('owner', 'code','usage')


admin.site.register(Plan)
admin.site.register(Payment)
admin.site.register(Ticket)
admin.site.register(ReffealCode,Reffreal)


# Register your models here.
