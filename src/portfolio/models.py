from django.db import models
from datetime import datetime
from django.utils import timezone

class Tile(models.Model):
    """Tile model to represent data for main page
    """
    
    name = models.TextField(unique=True)
    file_name = models.TextField(default="")
    description = models.TextField(default="")
    size_x = models.IntegerField(default=100)
    size_y = models.IntegerField(default=100)
    created = models.DateTimeField(default=datetime.now(tz=timezone.get_current_timezone()))
    edited = models.DateTimeField(default=datetime.now(tz=timezone.get_current_timezone()))