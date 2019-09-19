from django.db import models
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    seller = models.CharField(max_length=100)

    def __str__(self):
        return self.title


