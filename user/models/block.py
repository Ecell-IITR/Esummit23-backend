from django.db import models


class BlockMail(models.Model):
   blockmail=models.CharField( db_index=True, max_length=100, unique=True, verbose_name="Email")
   user = models.CharField(default="",max_length=100)
   class Meta:
        """
        Meta class for BlockMail
        """
        verbose_name_plural = 'BlockMail'

   def __str__(self):
        return self.blockmail

class BlockNumber(models.Model):
   blocknumber=models.CharField( db_index=True, max_length=100, unique=True, verbose_name="Number")
   user = models.CharField(default="",max_length=100)
   class Meta:
        """
        Meta class for BlockNumber
        """
        verbose_name_plural = 'BlockNumber'

   def __str__(self):
        return self.blocknumber