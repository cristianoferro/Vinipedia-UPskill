from django.contrib import admin
from producer.models import Producer, ProducerPicture, PictureAuthor


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'website')
    list_filter = ('name', 'address')


@admin.register(ProducerPicture)
class ProducerPictureAdmin(admin.ModelAdmin):
    list_display = ('pathname', 'producer')
    list_filter = ('producer',)


@admin.register(PictureAuthor)
class PictureAuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'img_code', 'picture_url')
    list_filter = ('author',)
