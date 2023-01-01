from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from user.models.role.proff import ProffUser
from user.models.role.student import StudentUser
from user.models.role.startup import StartupUser
from user.models.role.ca import CAUser


class Services(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    # default cost 0
    img = models.ImageField(upload_to='services/', blank=True)
    fixed_cost = models.IntegerField(default=0)
    varaible_cost = models.IntegerField(default=0)
    add_details = RichTextUploadingField(default="")
    questions = models.TextField(default=r"{}", max_length=1000)
    is_verified = models.BooleanField(default=False) 

    @classmethod
    def create(cls, name, desc, img, fixed_cost=0, varaible_cost=0, add_details=""):
        services = cls(name=name, desc=desc, fixed_cost=fixed_cost,
                       varaible_cost=varaible_cost, add_details=add_details, img=img)
        # do something with the book
        return services

    class Meta:
        """
        Meta class for Services
        """
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name


class EventCoordinator(models.Model):
    name = models.CharField(max_length=100, verbose_name="Coordinator Name")
    email = models.EmailField(max_length=100, verbose_name="Email Id")
    phone_number = models.IntegerField(verbose_name="Phone Number")
    image = models.ImageField(
        upload_to='event/coordinator/', verbose_name="Event Coordinator", blank=True)
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
    StudentUser = models.ManyToManyField(
        StudentUser, verbose_name="Student User", blank=True)
    ProffUser = models.ManyToManyField(
        ProffUser, verbose_name="Proff User", blank=True)
    StartupUser = models.ManyToManyField(
        StartupUser, verbose_name="Startup User", blank=True)
    CAUser = models.ManyToManyField(
        CAUser, verbose_name="CA User", blank=True)

    EmailMessage = RichTextUploadingField()
    class Meta:

        verbose_name_plural = 'Event Round'

    def __str__(self):
        return self.round_name


class EventSeo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    keywords = models.TextField(verbose_name="Keywords")
    hashtags = models.TextField(verbose_name="Hashtags")

    class Meta:
        """
        Meta class for Event Seo
        """
        verbose_name_plural = 'Event Seo'

    def __str__(self):
        return self.name


class AbstractEvent(models.Model):
    EVENT_STATUS_TYPE = (
        ('U', 'Upcoming'),
        ('L', 'Live'),
        ('O', 'Over'),

    )
    
    event_name = models.CharField(
        max_length=100, verbose_name="Event Name", db_index=True, unique=True)
    card_image = models.ImageField(
        upload_to='card/', verbose_name="Event's Card image", blank=True)
    background_image = models.ImageField(
        upload_to='background/', verbose_name="Event's background image", blank=True)
    tagline = models.CharField(max_length=255, verbose_name="Event Tagline")
    description = RichTextUploadingField(
        verbose_name="Event's Description", blank=True)
    card_description = RichTextUploadingField(
        verbose_name="Event's Card Description", blank=True)
    google_form = models.URLField(
        verbose_name="Event's Google Form", blank=True, null=True)
    event_priority = models.IntegerField(
        verbose_name="priority of event", default=1)
    event_status = models.CharField(
        max_length=1, choices=EVENT_STATUS_TYPE, default='U', verbose_name="Event Status")
    event_faqs = models.ManyToManyField(
        EventsFAQ, blank=True, related_name="%(app_label)s_%(class)s_faqs_of")
    events_coordinators = models.ManyToManyField(
        to=EventCoordinator, blank=True)
    mobile_background_image = models.ImageField(
        upload_to='event/main/background/', verbose_name="Event's Mobile background image", blank=True, null=True, default=None)
    logo_image = models.ImageField(
        upload_to='event/main/logo/', verbose_name="Event's logo image", blank=True, null=True, default=None)
    seo = models.OneToOneField(
        EventSeo, on_delete=models.CASCADE, blank=True, null=True, default=None)
    Type = models.CharField(max_length=100, verbose_name="Event Type",default="")
    registraion_start_date=models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    registraion_end_date=models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    class Meta:
        """
        Meta class for AbstractEvent
        """
        abstract = True

    def __str__(self):
        return self.event_name



class Event(AbstractEvent):
    """
    This class implements Event
    """
    event_eligibility = models.ManyToManyField(
        EventRules, blank=True, related_name="%(app_label)s_%(class)s_elgiblty_of", verbose_name="Elegiblity Rules")
    event_rounds = models.ManyToManyField(
        EventRounds, blank=True, related_name="%(app_label)s_%(class)s_rounds_of", verbose_name="Event Rounds")
    event_perks = models.ManyToManyField(
        EventPerks, blank=True, related_name="%(app_label)s_%(class)s_perks_of", verbose_name="Event Perks")
    event_rules = models.ManyToManyField(
        EventRules, blank=True, related_name="%(app_label)s_%(class)s_rule_of", verbose_name="Event Rules")
    event_partners = models.ManyToManyField(
        EventsPartners, related_name="%(app_label)s_%(class)s_partners_of", verbose_name="Partners/Sponsors Of Events")
    created_at = models.DateTimeField(default=timezone.now, editable=True)
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
            ser = Services.create(
                self.event_name, self.card_description, img=self.card_image)
            ser.save()
        return super(Event, self).save(*args, **kwargs)

    class Meta:
        """
        Meta class for Event
        """
        verbose_name_plural = 'Events'
