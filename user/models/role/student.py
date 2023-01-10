from user.models.abstarct import AbstractProfile
from django.db import models


class StudentUser(AbstractProfile):
    STUDENT_TYPE = (
        ('IITR', "IITR Student"),
        ('NONIITR', "Non IITR Student")
    )
    GENDER = (
        ('M', "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    student_type = models.CharField(
        choices=STUDENT_TYPE, max_length=10, default='NONIITR')
    enrollment_no = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Enrollment Number(If IITR Student)"
    )
    gender = models.CharField(max_length=10, blank=True,
                              null=True, verbose_name="Gender")
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    collage = models.CharField(max_length=200, verbose_name="Collage Name",default="IIT Roorkee")
    esummit_id = models.CharField(max_length=20, unique=True, db_index=True)
    referred_by = models.CharField(max_length=20,null=True,blank=True,default="")

    def save(self, *args, **kwargs):
        professional_tag = "STU"
        if self.enrollment_no!=None:
            self.student_type="IITR"
        if not self.esummit_id:
            
            # getting a non-repeating number
            unique_id = StudentUser.objects.last()
            if unique_id:
                unique_value = unique_id.id + 1
            else:
                unique_value = 0
            self.esummit_id = 'ES23'+professional_tag + \
                str((unique_value + 1) * 31)




        



          
        return super(StudentUser, self).save(*args, **kwargs)
    
