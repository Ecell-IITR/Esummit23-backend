
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from user.models.role.proff import ProffUser
from user.models.role.student import StudentUser
from user.models.role.startup import StartupUser


class Services(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')


class EventCoordinator(models.Model):
    name = models.CharField(max_length=100, verbose_name="Coordinator Name")
    email = models.EmailField(max_length=100, verbose_name="Email Id")
    phone_number = models.IntegerField(verbose_name="Phone Number")

    class Meta:
        """
        Meta class for EventCoordinator
        """
        verbose_name_plural = 'Event Coordinators'

    def __str__(self):
        return self.name


class EventsFAQ(models.Model):
    question = models.TextField(
        verbose_name='Question', default="", max_length=1000)
   # answer = RichTextUploadingField(verbose_name='Answer')
    answer = models.TextField(verbose_name="answer",
                              default="", max_length=1000)

    def __str__(self):
        return self.question

    class Meta:
        """
        Meta class for EventRounds
        """
        verbose_name_plural = 'FAQs'


class EventsPartners(models.Model):
    title = models.CharField(verbose_name='Title', default="", max_length=100)
    image = models.ImageField(
        upload_to='event/partners/', verbose_name="Event Partner", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        """
        Meta class for Speaker
        """
        verbose_name_plural = 'Event Partners'


class EventPerks(models.Model):
    heading = models.CharField(default="", max_length=100)
    image = models.ImageField(upload_to='event/perks/',
                              verbose_name="Event's Perks image", blank=True)
    description = RichTextUploadingField()

    def __str__(self):
        return self.heading

    class Meta:
        """
        Meta class for Speaker
        """
        verbose_name_plural = 'Event Perks'


class EventRules(models.Model):
    rule = models.TextField(verbose_name="Event Rule")

    class Meta:
        """
        Meta class for Event Rules
        """
        verbose_name_plural = 'Event Rules'

    def __str__(self):
        return self.rule
class EventRounds(models.Model):
    round_name = models.CharField(max_length=100, verbose_name="Round Name")
    start_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    max_points = models.IntegerField(verbose_name="Maximum Points", blank=True)
    tasks = RichTextUploadingField(verbose_name="Tasks", blank=True)
    round_eligibility = RichTextUploadingField(
        verbose_name="Eligibility For Round", blank=True)
    StudentUser = models.ManyToManyField(StudentUser, verbose_name="Student User", blank=True)
    ProffUser = models.ManyToManyField(ProffUser, verbose_name="Proff User", blank=True)
    StartupUser = models.ManyToManyField(StartupUser, verbose_name="Startup User", blank=True)
    EmailMessage = RichTextUploadingField()
    class Meta:
      
        verbose_name_plural = 'Event Round'

    

    def __str__(self):
        return self.round_name




        