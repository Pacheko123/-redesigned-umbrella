from django.db import models


# Create your models here.
class Subscription(models.Model):
    email = models.CharField(max_length=42)


