from django.contrib import admin
from django.utils.html import format_html
from .models import GameAd
from .models import Genre
@admin.action(description="Установить состояние: Новая")
def make_new(modeladmin, request, queryset):
    queryset.update(condition='new')

@admin.action(description="Установить состояние: Б/у")
def make_used(modeladmin, request, queryset):
    queryset.update(condition='used')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(GameAd)
class GameAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'genre', 'condition', 'price', 'author', 'published')
    list_filter = ('platform', 'genre', 'condition', 'published')
    search_fields = ('title', 'description')
    list_editable = ('price', 'condition')
    readonly_fields = ('published',)
    fields = (
        'author', 'title', 'platform', 'genre', 'condition',
        'price', 'description', 'image', 'published'
    )
    actions = [make_new, make_used]
# Register your models here.
