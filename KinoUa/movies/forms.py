from .models import Movie
from django.forms import ModelForm, TextInput, Textarea

class MovieCreateForm(ModelForm):
    class Meta:
        model = Movie

        fields = ["title", "description", "rating", "year", "category", "actors"]
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву '}),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис'}),
            'rating': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Рейтинг'}),
            'year': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть рік'}),
            'category': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть категорію'}),
            'actors': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Додайте акторів'})
            }


