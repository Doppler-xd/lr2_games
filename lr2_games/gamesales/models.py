from django.db import models
from django.contrib.auth.models import User
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Жанр')
    
    class Meta:
        verbose_name_plural = 'Жанры'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class GameAd(models.Model):
    PLATFORM_CHOICES = [
        ('ps4', 'PlayStation 4'),
        ('ps5', 'PlayStation 5'),
        ('xbox_one', 'Xbox One'),
        ('xbox_sx', 'Xbox Series X|S'),
        ('pc', 'PC'),
    ]
    CONDITION_CHOICES = [
        ('new', 'Новая'),
        ('used', 'Б/у'),
    ]

    title = models.CharField(max_length=100, verbose_name='Название игры')
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, verbose_name='Платформа')
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, verbose_name='Состояние')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    genre = models.ForeignKey(Genre,on_delete=models.PROTECT,verbose_name='Жанр',null=True,blank=True )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='Автор')
    image = models.ImageField(upload_to='game_covers/', blank=True, null=True, verbose_name='Обложка')
    class Meta:
        verbose_name_plural = 'Объявления о продаже игр'
        ordering = ['-published']

    def __str__(self):
        return f'{self.title} ({self.get_platform_display()})'

# Create your models here.
