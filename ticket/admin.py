from django.contrib import admin
from .models import Plan, Payment, Ticket,ReffealCode

class Reffreal(admin.ModelAdmin):
    exclude = ( 'usage',)
    list_display = ('owner', 'code','usage')

class TicketsAdmin(admin.ModelAdmin):
    list_display = ('Person', 'name', 'quantity')

    search_fields = ('Person__email', 'name')

admin.site.register(Plan)
admin.site.register(Payment)
admin.site.register(Ticket,TicketsAdmin)
admin.site.register(ReffealCode,Reffreal)


# Register your models here.
