from .models import EventCoordinator, EventsFAQ, EventsPartners, EventPerks, EventRules, EventRounds, EventSeo, Event,Services
from rest_framework import serializers


class EventCoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCoordinator
        fields = '__all__'


class EventFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsFAQ
        fields = '__all__'


class EventPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsPartners
        fields = '__all__'


class EventPerksSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPerks
        fields = '__all__'


class EventRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRules
        fields = '__all__'


class EventRoundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRounds
        exclude = ['StudentUser', "StartupUser", "ProffUser"]


class EventSeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSeo
        fields = '__all__'


class EventRoundsSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventRounds
        exclude = ['StudentUser', "StartupUser", "ProffUser","CAUser"]


class EventMiniSerializer(serializers.Serializer):
    event_name = serializers.CharField(max_length=100)
    card_image = serializers.ImageField()
    card_description = serializers.CharField(max_length=1000)

    class Meta:
        model = Event
        fields = '__all__'


class EventSerializer(serializers.Serializer):

    event_name = serializers.CharField(max_length=100)
    tagline = serializers.CharField(max_length=100)
    Type = serializers.CharField(max_length=100)
    registraion_start_date = serializers.DateField()
    registraion_end_date = serializers.DateField()
    card_image = serializers.ImageField()
    background_image = serializers.ImageField()
    description = serializers.CharField(max_length=1000)
    events_coordinators = EventCoordinatorSerializer(many=True)
    event_faqs = EventFAQSerializer(many=True)
    event_partners = EventPartnersSerializer(many=True)
    event_perks = EventPerksSerializer(many=True)
    event_rules = EventRulesSerializer(many=True)
    event_rounds = EventRoundsSerializer(many=True)
    event_eligibility = EventRulesSerializer(many=True)
    seo = EventSeoSerializer(many=True)


    class Meta:
        model = Event
        fields = '__all__'


class ServiceSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Services
        fields = '__all__'
