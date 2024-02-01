from django.contrib import admin
from django.db.models import Count, Sum
from .models import Plan, Payment, Ticket,ReffealCode,StatisticsParticipants,App_download
from django.http import HttpResponse
from io import StringIO 
import csv

class Reffreal(admin.ModelAdmin):
    exclude = ( 'usage',)
    list_display = ('owner', 'code','usage')

class TicketsAdmin(admin.ModelAdmin):
    list_display = ('Person', 'name', 'quantity')
    search_fields = ('Person__email', 'name','Person__student__esummit_id','Person__startup__esummit_id','Person__proff__esummit_id')
    actions = ['download_csv']
    change_list_template = 'change_list.html'
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        qs=""
        
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        print(qs)
        metrics = {
            'total': Count('id'),
            'total_sales': Sum('quantity'),
        }

        response.context_data['summary'] = list(
            qs
            .values('Person', 'name', 'quantity')
            .annotate(**metrics)
        
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
   

        return response

class TicketsAdmin2(admin.ModelAdmin):
    list_display = ('Person', 'name', 'quantity')
    search_fields = ('Person__email', 'name',"Person__name")
    actions = ['download_csv']
    def download_csv(self, request, queryset):
    


        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["name", "email", "quanty", "phone","type","desc"])

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



admin.site.register(Plan)
admin.site.register(App_download)
admin.site.register(Payment)
admin.site.register(StatisticsParticipants)
admin.site.register(Ticket, TicketsAdmin2)
admin.site.register(ReffealCode,Reffreal)          

        
# Register your models here.
