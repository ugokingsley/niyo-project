from django.db import models
from authApi.models import *

class TaskManager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=240, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(default='pending', max_length=240, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    
    # a toString method that returns the book title
    def __str__(self):
        return str(self.title)

    # default ordering by primary key (id) in descending order    
    class Meta:
        ordering = ["-pk"]