from .models import EventCoordinator, EventsFAQ, EventsPartners, EventPerks, EventRules, EventRounds, EventSeo, Event
from rest_framework import serializers

class EventCoordinatorSerializer(serializers.Serializer):
    class Meta:
        model = EventCoordinator
        fields = '__all__'


class EventFAQSerializer(serializers.Serializer):
    class Meta:
        model = EventsFAQ
        fields = '__all__'


class EventPartnersSerializer(serializers.Serializer):
    class Meta:
        model = EventsPartners
        fields = '__all__'


class EventPerksSerializer(serializers.Serializer):
    class Meta:
        model = EventPerks
        fields = '__all__'


class EventRulesSerializer(serializers.Serializer):
    class Meta:
        model = EventRules
        fields = '__all__'


class EventRoundsSerializer(serializers.Serializer):
    class Meta:
        model = EventRounds
        fields = '__all__'
class EventSeoSerializer(serializers.Serializer):
    class Meta:
        model = EventSeo
        fields = '__all__'
class EventRoundsSerializer(serializers.Serializer):

    class Meta:
        model = EventRounds
        exclude = ['StudentUser',"StartupUser","ProffUser"]
class EventSerializer(serializers.Serializer):
    EventCoordinator=EventCoordinatorSerializer
    EventsFAQ=EventFAQSerializer
    EventsPartners=EventPartnersSerializer
    EventPerks=EventPerksSerializer
    EventRules=EventRulesSerializer
    EventRounds=EventRoundsSerializer
    EventSeo=EventSeoSerializer
    class Meta:
        model = Event
        fields = '__all__'