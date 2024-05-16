from .models import *
from rest_framework import serializers, exceptions
from django.db import transaction
from .models import *
from datetime import datetime,timedelta


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['user', 'title', 'description', 'author', 'publisher', 'pages', 'created_at', 'updated_at']
        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': True},
            'author': {'required': True},
            'pages': {'required': True}
        } 
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=['title', 'author']
            )
        ]