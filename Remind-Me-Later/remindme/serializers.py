# serializers.py
from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'date', 'time', 'message', 'notification_method']
        extra_kwargs = {
            'date': {'required': True},
            'time': {'required': True},
            'message': {'required': True},
            'notification_method': {'required': True},
        }