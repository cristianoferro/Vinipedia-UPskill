from datetime import datetime

from model_utils import Choices
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from producer.models import Producer, PictureAuthor
from django.db.models import Q, Avg, Count


class Grape(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='images/grapes/', blank=True)
    img_author = models.OneToOneField(
        PictureAuthor, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)

    def get_similar_objs(self):
        return self.wines.all()


class Wine(models.Model):
    PRICE_CHOICES = (
        ('unknown', 'Unknown'),
        ('economic', 'Economic'),
        ('reasonable', 'Reasonable'),
        ('expensive', 'Expensive')
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    grapes = models.ManyToManyField(Grape)
    picture = models.ImageField(upload_to='images/wines/', blank=True)
    img_author = models.OneToOneField(
        PictureAuthor, null=True, on_delete=models.SET_NULL, blank=True)
    pageviews = models.IntegerField(default=0)
    price = models.CharField(max_length=255, choices=Choices(
        *PRICE_CHOICES), default="unknown")
    types = models.ManyToManyField(Tag, blank=True, related_name="wines")

    # Sem o método 'str' aparece object no site do admin
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wine:wine_detail',
                       args=[self.pk])

    def get_similar_wines(self):
        # wines = []
        # for type in self.types.all():
        #     wines.append(type.get_similar_objs())
        return Wine.objects.filter(types__in=self.types.all()).exclude(pk=self.pk)

    def get_wines_by_grape(self):
        return Wine.objects(grapes__in=self.grapes.all()).exclude(pk=self.pk)

    def get_avg_score(self):
        return self.evaluations.aggregate(Avg('score'))

    def trending_rank(self):
        aggregate = Wine.objects.filter(
            pageviews__gt=self.pageviews).aggregate(trending_rank=Count('pageviews'))
        return aggregate['trending_rank']+1

    class Meta:
        ordering = ("name",)


class Evaluation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="evaluations")
    date = models.DateTimeField(auto_now_add=True)
    wine = models.ForeignKey(
        Wine, on_delete=models.CASCADE, related_name="evaluations")
    description = models.TextField()
    score = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        ordering = ("-date",)
