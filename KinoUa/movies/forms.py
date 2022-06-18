from .models import Movie
from django import forms

class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie

        fields = ["title", "description", "rating", "year", "categories", "actors"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву '}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис'}),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Рейтинг'}),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть рік'}),
            'categories': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть категорію'}),
            'actors': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Додайте акторів'})
            }


