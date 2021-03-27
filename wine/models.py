from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from producer.models import Producer

class Grape(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='images/grapes/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name", )

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        pass

class Wine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    grapes = models.ManyToManyField(Grape)
    picture = models.ImageField(upload_to='images/wines/', blank=True)
    # TODO: Retirar o blank quando se popular a BD
    type = models.ManyToManyField(Tag, blank=True)

    # Sem o método 'str' aparece object no site do admin
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/detail/%i/" % self.id

    class Meta:
        ordering = ("name", )

class Evaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="evaluations")
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name="evaluations")
    description = models.TextField()
    score = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)])

    class Meta:
        pass
