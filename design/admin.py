from django.contrib import admin
from .models import Colors

class DesignAdmin(admin.ModelAdmin):
    exclude = ('created', 'updated')

class ColorsAdmin(DesignAdmin):
    pass

admin.site.register(Colors,ColorsAdmin)