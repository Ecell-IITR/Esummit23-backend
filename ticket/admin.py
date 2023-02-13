from django.contrib import admin
from django.db.models import Count, Sum, Min, Max, DateTimeField
from user.tasks import send_link_email_task
from django.shortcuts import render

from .models import Plan, Payment, Ticket,ReffealCode
from django.http import HttpResponse
from django import forms

from io import StringIO 
import csv
from django.contrib.admin.helpers import ActionForm

class Reffreal(admin.ModelAdmin):
    exclude = ( 'usage',)
    list_display = ('owner', 'code','usage')

class TicketsAdmin(admin.ModelAdmin):
    list_display = ('Person', 'name', 'quantity')
    search_fields = ('Person__email', 'name')
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

admin.site.register(Plan)
admin.site.register(Payment)
admin.site.register(Ticket, TicketsAdmin)
admin.site.register(ReffealCode,Reffreal)          

        
# Register your models here.
