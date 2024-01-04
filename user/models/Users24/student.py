from django.db import models
from user.models.abstarct import CommonDetails

class Student(CommonDetails):
    STUDENT_TYPE = (
        ('IITR', "IITR Student"),
        ('NONIITR', "Non IITR Student")
    )
    
    student_type = models.CharField(
        choices=STUDENT_TYPE, max_length=10, default='NONIITR')
    enrollment_no = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Enrollment Number(If IITR Student)"
    )
   
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=200, verbose_name="Country",default="India")
    pincode = models.CharField(max_length=200, verbose_name="Pin Code",default="")
    State = models.CharField(max_length=200, verbose_name="State",default="")
    college = models.CharField(max_length=200, verbose_name="Collage Name",default="IIT Roorkee")
    esummit_id = models.CharField(max_length=40, unique=True, db_index=True)
    referred_by = models.CharField(max_length=40,null=True,blank=True,default="")

    def save(self, *args, **kwargs):
        professional_tag = "STU"
        if self.enrollment_no!=None:
            self.student_type="IITR"
        if not self.esummit_id:
            
            # getting a non-repeating number
            unique_id = Student.objects.last()
            if unique_id:
                unique_value = unique_id.id + 1
            else:
                unique_value = 0
            self.esummit_id = 'ES24'+professional_tag + \
                str((unique_value + 1) * 31)

        return super(Student, self).save(*args, **kwargs)
    
