from django.contrib import admin
from django.utils.html import format_html
from .models import GameAd
from .models import Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
@admin.register(GameAd)
class GameAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'condition', 'price', 'published')
    list_filter = ('platform', 'condition', 'published')
    search_fields = ('title', 'description')
    fields = ('author', 'title', 'platform', 'genre', 'condition', 'price', 'description', 'image')
    readonly_fields = ('cover_preview',)
    list_editable = ('price', 'condition')
    def cover_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" />', obj.image.url)
        return "Нет обложки"
    cover_preview.short_description = "Обложка"
# Register your models here.
