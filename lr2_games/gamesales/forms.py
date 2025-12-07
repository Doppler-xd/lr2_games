from django import forms
from .models import GameAd
from django.core.exceptions import ValidationError
class GameAdForm(forms.ModelForm):
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError("Цена должна быть положительной.")
        return price
    class Meta:
        model = GameAd
        fields = ['title', 'platform', 'genre', 'condition', 'price', 'description', 'image']
        labels = {
            'title': 'Название игры',
            'platform': 'Платформа',
            'genre': 'Жанр',
            'condition': 'Состояние',
            'price': 'Цена (₽)',
            'description': 'Описание',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }