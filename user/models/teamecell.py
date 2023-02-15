from django.db import models

class Teamecell(models.Model):
  Email = models.EmailField()
  Otp = models.CharField(max_length=15,null=True, blank=True)
  Name= models.CharField(max_length=30)
  
  def __str__(self):
        return self.Name
  
  class Meta:
        """
        Meta class for Teamecell
        """
        verbose_name_plural = "Teamecell"