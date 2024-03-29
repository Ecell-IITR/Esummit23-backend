from django.db import models
from user.models.person import person
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus
from django.utils import timezone


class Plan(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    price = models.IntegerField(default=0, verbose_name="Price")
    description = models.TextField(verbose_name="Description")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    name = models.CharField(
        _("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = models.CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"


class Ticket(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    quantity = models.IntegerField(default=1, verbose_name="Quantity")
    Person = models.ForeignKey(
        person, on_delete=models.CASCADE, verbose_name="Person",related_name="ticket")
    plan = models.CharField(max_length=100, verbose_name="Plan", default="")
    total_payment = models.IntegerField(
        default=0, verbose_name="Total Payment")
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, verbose_name="Payment", null=True, blank=True)
    verified = models.BooleanField(default=True, verbose_name="Verified")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name+"_"+str(self.Person)



    def __str__(self):
        return self.name+"_"+str(self.Person)

class ReffealCode(models.Model):
    owner = models.CharField(max_length=50, verbose_name="Owner")
    code = models.CharField(
        max_length=50, verbose_name="Code", blank=True, null=True)
    usage = models.IntegerField(default=0, verbose_name="Usage")

    def __str__(self):
        return self.code+"_"+self.owner+"_"+str(self.usage)

    def save(self, *args, **kwargs):
        if not self.code or self.code[:4] != "ESRF":
            unique_id = ReffealCode.objects.last()
            if unique_id:
                self.code = "ESRF"+self.owner[:3]+str(unique_id.id+1)
            else:
                self.code = "ESRF"+self.owner[:3]+"1"

        super().save(*args, **kwargs)


class StatisticsParticipants(models.Model):
    Type = models.CharField(max_length=30, blank=True, null=True)
    Name = models.CharField(max_length=60, blank=True, null=True)
    SummitId = models.CharField(max_length=50)
    PhoneNo = models.IntegerField(default=0,blank=True, null=True)
    Email = models.EmailField(max_length=50, blank=True, null=True)
    EventName = models.CharField(max_length=50, blank=True, null=True)
    TimeEntryExit = models.DateTimeField()

    def __str__(self):
        return self.Name+"_"+self.EventName+"_"+self.Type

    def save(self, *args, **kwargs):
        if not self.TimeEntryExit:
            self.TimeEntryExit = timezone.now()

        return super(StatisticsParticipants, self).save(*args, **kwargs)

    class Meta:
        """
        Meta class for StatisticsParticipants
        """
        verbose_name_plural = 'StatisticsParticipant'




