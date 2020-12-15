from django.db import models
from datetime import datetime
from django.utils import timezone

class Tile(models.Model):
    """Tile model to represent data for main page
    """
    
    name = models.TextField(unique=True)
    file_name = models.TextField(default="")
    description = models.TextField(default="")
    created = models.DateTimeField(default=datetime.now(tz=timezone.get_current_timezone()))
    edited = models.DateTimeField(default=datetime.now(tz=timezone.get_current_timezone()))