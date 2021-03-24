from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    website = models.URLField(max_length = 200,
        # db_index=True,
        unique=True, blank=True
    )


class ProducerPicture(models.Model):
    pathname = models.ImageField(upload_to='images/producers/', blank=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
