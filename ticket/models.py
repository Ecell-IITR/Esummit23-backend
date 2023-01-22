from django.db import models
from user.models.person import person
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus


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
    quantity = models.IntegerField(default=0, verbose_name="Quantity")
    Person = models.ForeignKey(
        person, on_delete=models.CASCADE, verbose_name="Person")
    plan = models.CharField(max_length=100, verbose_name="Plan",default="ssp")
    total_payment = models.IntegerField(
        default=0, verbose_name="Total Payment")
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,verbose_name="Payment")
    verified = models.BooleanField(default=True, verbose_name="Verified")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
