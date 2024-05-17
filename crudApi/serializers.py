from .models import *
from rest_framework import serializers, exceptions
from django.db import transaction
from .models import *
from datetime import datetime,timedelta
from rest_framework.validators import UniqueTogetherValidator
from django.core.exceptions import ValidationError


class TaskManagerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = TaskManager
        fields = ['user', 'title', 'description', 'start_date', 'end_date', 'status', 'created_at', 'updated_at']
        
        # checking to see that Task status is either of 'completed','active','pending'
        def validate_status(validated_data):
            if validated_data.get('status') not in ['completed','active','pending']:
                raise ValidationError("Task status can only be 'completed','active','pending' ")

        # checking to see that Task end_date is later than start_date
        def validate_dates(validated_data):
            if validated_data.get('start_date') > validated_data.get('end_date'):
                raise ValidationError("start_date cannot be later than end_date")

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
            ),
            validate_status,
            validate_dates,
        ]