from user.models.abstarct import CommonDetails

from django.db import models


class Startup(CommonDetails):
    startup_name = models.CharField(max_length=50, verbose_name="Startup Name")
    domain = models.CharField(max_length=50, verbose_name="Domain")
    esummit_id = models.CharField(max_length=40, unique=True, db_index=True)
    referred_by = models.CharField(max_length=40,null=True,blank=True,default="")

    def save(self, *args, **kwargs):
        professional_tag = "STP"

        if not self.esummit_id:
            # getting a non-repeating number
            unique_id = Startup.objects.last()
            if unique_id:
                unique_value = unique_id.id + 1
            else:
                unique_value = 0
            self.esummit_id = 'ES24'+professional_tag + \
                str((unique_value + 1) * 31)
        return super(Startup, self).save(*args, **kwargs)