from django.db import models
from datetime import datetime
from django.utils import timezone

class Tile(models.Model):
    """Tile model to represent data for main page
    """
    
    name = models.TextField(unique=True)
    file_name = models.TextField()
    description = models.TextField()
    size_x = models.IntegerField(default=1)
    size_y = models.IntegerField(default=1)
    created = models.DateTimeField(default=datetime.now(tz=timezone.get_current_timezone()))
    edited = models.DateTimeField(default=datetime.now(tz=timezone.get_current_timezone()))