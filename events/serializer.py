from .models import EventCoordinator, EventsFAQ, EventsPartners, EventPerks, EventRules, EventRounds, EventSeo
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
