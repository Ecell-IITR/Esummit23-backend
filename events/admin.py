from django.contrib import admin
from .models import Services, EventCoordinator, EventsFAQ, EventsPartners, EventRounds, EventRules, Event, EventPerks
from .models import EventSeo
from django.core.mail import send_mail


class RoundStartupsInline(admin.TabularInline):
    model = EventRounds.StartupUser.through
    extra = 3


class RoundStudentInline(admin.TabularInline):
    model = EventRounds.StudentUser.through
    extra = 3


class RoundProffInline(admin.TabularInline):
    model = EventRounds.ProffUser.through
    extra = 3


class RoundCAInline(admin.TabularInline):
    model = EventRounds.CAUser.through
    extra = 3


class AdminRound(admin.ModelAdmin):
    exclude = ('created', 'updated', "ProffUser",
               "StudentUser", "StartupUser", "CAUser")

    inlines = [RoundStartupsInline, RoundStudentInline,
               RoundProffInline, RoundCAInline]

    actions = ['send_EMAIL']

    def send_EMAIL(self, request, queryset):

        for query in queryset:
            stp = query.StudentUser.all()
            for user in stp:
                send_mail('message from esummit', "", 'from@example.com', [
                          user.email], fail_silently=False, html_message=query.EmailMessage)
            prf = query.ProffUser.all()
            for user in prf:
                send_mail('message from esummit', "", 'from@example.com', [
                          user.email], fail_silently=False, html_message=query.EmailMessage)
            stu = query.StudentUser.all()
            for user in stu:
                send_mail('message from esummit', "", 'from@example.com', [
                          user.email], fail_silently=False, html_message=query.EmailMessage)
            ca = query.CAUser.all()
            for user in ca:
                send_mail('message from esummit', "", 'from@example.com', [
                          user.email], fail_silently=False, html_message=query.EmailMessage)
        # for i in queryset:
        #     if i.email:
        #         send_mail('message from esummit', 'Here is the message.', 'from@example.com',[i.email], fail_silently=False)


# Register your models here.

@admin.register(EventCoordinator)
class CoordinatorList(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number"]


@admin.register(Services)
class ServicesList(admin.ModelAdmin):
    list_display = ["name", "desc", "fixed_cost", "varaible_cost"]

@admin.register(EventPerks)
class EventPerksList(admin.ModelAdmin):
    list_display = ["heading", "description", "image"]

class EventFAQInlines(admin.TabularInline):
    model = Event.event_faqs.through
    verbose_name_plural = "FAQS"
    extra = 2


class EventCoordinatorInlines(admin.TabularInline):
    model = Event.events_coordinators.through
    verbose_name_plural = "Event Coordinators"
    extra = 2


class EventRuleInlines(admin.TabularInline):
    model = Event.event_rules.through
    verbose_name_plural = "Event Rules"
    extra = 2


class EventPartnerInlines(admin.TabularInline):
    model = Event.event_partners.through
    verbose_name_plural = "Event Partners / Sponsors"
    extra = 3


class EventRoundInlines(admin.TabularInline):
    model = Event.event_rounds.through
    verbose_name_plural = "Event Rounds"
    extra = 2


class EventPerksInlines(admin.TabularInline):
    model = Event.event_perks.through
    verbose_name_plural = "Event Perks"
    extra = 2


class EventAdmin(admin.ModelAdmin):
    list_display = ["event_name", "tagline", "event_priority"]
    search_fields = ["event_name", "tagline", ]
    list_filter = ["event_status", ]
    inlines = [EventFAQInlines, EventCoordinatorInlines, EventRuleInlines,
               EventPartnerInlines, EventRoundInlines, EventPerksInlines]
    exclude = ['event_faqs', 'event_rules', 'events_coordinators', 'event_partners', 'event_perks',
               'event_rounds']


# admin.site.register(Services)
# admin.site.register(EventCoordinator)
admin.site.register(EventsFAQ)
admin.site.register(EventsPartners)
admin.site.register(EventRules)
admin.site.register(EventRounds, AdminRound)
admin.site.register(Event, EventAdmin)
admin.site.register(EventSeo)
