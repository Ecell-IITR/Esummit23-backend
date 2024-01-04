from user.models.abstarct import CommonDetails

from django.db import models


class Proff(CommonDetails):

   
    organisation_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Organisation From")
    position = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="position")
    esummit_id = models.CharField(max_length=40, unique=True, db_index=True)
    referred_by = models.CharField(max_length=40,null=True,blank=True,default="")

    def save(self, *args, **kwargs):
        professional_tag = "PRF"

        if not self.esummit_id:
            # getting a non-repeating number
            unique_id = ProffUser.objects.last()
            if unique_id:
                unique_value = unique_id.id + 1
            else:
                unique_value = 0
            self.esummit_id = 'ES24'+professional_tag + \
                str((unique_value + 1) * 31)
        return super(ProffUser, self).save(*args, **kwargs)
