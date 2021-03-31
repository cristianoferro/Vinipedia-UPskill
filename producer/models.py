from django.db import models
from django.urls import reverse


class PictureAuthor(models.Model):
    author = models.CharField(max_length=100, blank=True)
    author_url = models.URLField(max_length=200, blank=True)
    link_name = models.CharField(max_length=100, blank=True)
    picture_url = models.URLField(max_length=200, unique=True, blank=True)
    img_code = models.CharField(max_length=100, unique=True, blank=True)


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
    img_author = models.OneToOneField(
        PictureAuthor, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.producer.name

    class Meta:
        pass
