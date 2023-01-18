from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from .person import person


class teams(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    number_of_members = models.IntegerField(default=1)
    members = models.ManyToManyField(person, verbose_name="Members")
    leader = models.ForeignKey(
        person, on_delete=models.CASCADE, verbose_name="Leader", related_name="leader",null=True)
    event = models.CharField(max_length=50, verbose_name="Event",null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    round_1 = models.BooleanField(default=True)
    round_2 = models.BooleanField(default=False)
    round_3 = models.BooleanField(default=False)
    submission_text = RichTextUploadingField(default="")
    submission_text2 = RichTextUploadingField(default="",blank=True)
    submission_file = models.FileField(
        upload_to='event/submission/', verbose_name="Submission File", blank=True)
    submission_link = models.URLField(default="",null=True)
    total_payment = models.IntegerField(default=0)
    razorpay_payment_id = RichTextUploadingField(default=" ")

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(teams, self).save(*args, **kwargs)

    def __str__(self):
        return self.name+" "+self.event

    class Meta:
        """
        Meta class for Teams
        """
        verbose_name_plural = "Teams"
