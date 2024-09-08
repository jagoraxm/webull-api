import uuid
from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    symbol = models.CharField(max_length=4)