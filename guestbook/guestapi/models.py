from django.db import models
from django.utils import timezone

class Entry(models.Model):
    nickname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


