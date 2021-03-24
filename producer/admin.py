from django.contrib import admin
from producer.models import Producer, ProducerPicture

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'website')
    list_filter = ('name', 'address')

@admin.register(ProducerPicture)
class ProducerPictureAdmin(admin.ModelAdmin):
    list_display = ('pathname', 'producer')
    list_filter = ('producer',)
