from .models import Movie, Category, Actor
from django import forms


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie

        fields = ["title", "movie_poster", "description", "rating", "year", "categories", "actors"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter movie title:'}),
            'movie_poster': forms.ClearableFileInput(),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description:'}),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rating:'}),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Year:'}),
            'categories': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter category:'
                }),
            'actors': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter actors:'})
        }

# class CreateUserForm(UserCreationForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#     password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         widgets = {
#             'username': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Username:'}),
#             'email': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Email:'}),
#             'password1': forms.PasswordInput(attrs={
#                 'class': 'form-input',
#                 'placeholder': 'Password:'}),
#             'password2': forms.PasswordInput(attrs={
#                 'class': 'form-input',
#                 'placeholder': 'Confirm your password:'})
#             }
