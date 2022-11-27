from .models import EventCoordinator, EventsFAQ, EventsPartners, EventPerks, EventRules, EventRounds, EventSeo, Event
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
        fields = '__all__'
class EventSeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSeo
        fields = '__all__'
class EventRoundsSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventRounds
        exclude = ['StudentUser',"StartupUser","ProffUser"]
class EventSerializer(serializers.Serializer):
    EventCoordinator=EventCoordinatorSerializer(many=True)
    EventsFAQ=EventFAQSerializer(many=True)
    EventsPartners=EventPartnersSerializer(many=True)
    EventPerks=EventPerksSerializer(many=True)
    EventRules=EventRulesSerializer(many=True)
    EventRounds=EventRoundsSerializer(many=True)
    EventSeo=EventSeoSerializer(many=True)
    class Meta:
        model = Event
        fields = '__all__'