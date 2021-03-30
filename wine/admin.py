from django.contrib import admin
from wine.models import Wine, Grape, Evaluation, Tag


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'producer', 'picture')
    list_filter = ('name', 'producer', 'grapes')
    filter_horizontal = ('grapes', 'types')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug')
    list_filter = ('name',)

@admin.register(Grape)
class GrapesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'picture')
    list_filter = ('name',)

@admin.register(Evaluation)
class EvaluationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'wine', 'description')
    list_filter = ('user', 'wine')
