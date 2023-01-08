from django.contrib import admin
from .models import Speakers, Team


class PublicAdmin(admin.ModelAdmin):
    exclude = ('created', 'updated')
    
class SpeakersAdmin(PublicAdmin):
    pass
class TeamAdmin(PublicAdmin):
    pass
admin.site.register(Speakers,SpeakersAdmin)
admin.site.register(Team,TeamAdmin)
