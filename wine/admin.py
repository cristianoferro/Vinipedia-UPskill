from django.contrib import admin
from wine.models import Wine, Grape, Evaluation

@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'producer', 'picture', 'type')
    list_filter = ('name', 'producer', 'grapes', 'type')
    filter_horizontal = ('grapes',)

@admin.register(Grape)
class GrapesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'picture')
    list_filter = ('name',)

@admin.register(Evaluation)
class EvaluationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'wine', 'description')
    list_filter = ('user', 'wine')
