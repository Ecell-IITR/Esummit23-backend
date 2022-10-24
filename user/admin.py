from django.contrib import admin
from user.models.role.startup import StartupUser
from user.models.role.ca import CAUser
from user.models.role.student import StudentUser
from user.models.role.proff import ProffUser
# Register your models here.
admin.site.register(StartupUser)
admin.site.register(CAUser)
admin.site.register(StudentUser)
admin.site.register(ProffUser)