from .models import *
from rest_framework import serializers, exceptions
from django.db import transaction
from .models import *
from datetime import datetime,timedelta
from rest_framework.validators import UniqueTogetherValidator


class BookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Book
        fields = ['user', 'title', 'description', 'author', 'publisher', 'pages', 'created_at', 'updated_at']
        extra_kwargs = {
            'title': {'required': True,'allow_blank':False},
            'description': {'required': True,'allow_blank':False},
            'author': {'required': True, 'allow_blank':False},
            'pages': {'required': True,}
        } 
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=['title', 'author']
            )
        ]