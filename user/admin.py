from django.contrib import admin
from user.models.role.startup import StartupUser
from user.models.role.ca import CAUser
# Register your models here.
admin.site.register(StartupUser)
admin.site.register(CAUser)
