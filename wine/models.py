from django.db import models
from producer.models import Producer

# Create your models here.

# Wines app
class Wine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

class Grapes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='images/grapes/', blank=True)


# Evaluations app
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
class Evaluations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    description = models.TextField()
    score = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)])