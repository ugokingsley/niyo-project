from .models import *
from rest_framework import serializers, exceptions
from django.db import transaction
from .models import *
from datetime import datetime,timedelta
from rest_framework.validators import UniqueTogetherValidator


class TaskManagerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = TaskManager
        fields = ['user', 'title', 'description', 'start_date', 'end_date', 'status', 'created_at', 'updated_at']
        
        # validate the task oject
        # Make all fields required, dont allow submittion of empty fields
        extra_kwargs = {
            'title': {'required': True,'allow_blank':False},
            'description': {'required': True,'allow_blank':False},
            'start_date': {'required': True},
            'end_date': {'required': True},
            'status': {'required': True, 'allow_blank':False},
        } 

        # validate the task object, make it unique to avoid repetition.
        # No two tasks should have same title and start_date 
        validators = [
            UniqueTogetherValidator(
                queryset=TaskManager.objects.all(),
                fields=['title', 'start_date']
            )
        ]