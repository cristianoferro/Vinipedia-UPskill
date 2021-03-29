from django.db import models
from django.urls import reverse


class Producer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    website = models.URLField(max_length=200,
                              # db_index=True,
                              unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('producer:producer_detail',
                       args=[self.pk])

    class Meta:
        ordering = ("name",)

class ProducerPicture(models.Model):
    pathname = models.ImageField(upload_to='images/producers/', blank=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    def __str__(self):
        return self.producer.name

    class Meta:
        pass
