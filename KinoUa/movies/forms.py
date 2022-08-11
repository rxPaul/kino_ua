from .models import Movie
from django import forms


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie

        fields = ["title", "movie_poster", "description", "rating", "year", "categories", "actors", "slug"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter movie title:'}),
            'movie_poster': forms.ClearableFileInput(attrs={
                'class': 'btn btn-primary'}
            ),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description:'}),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose your rating between 0 and 10'}),
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
                    'placeholder': 'Enter actors:'}),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter slug:'}),
        }
        # slug = forms.SlugField(
        #             help_text="Slug is a field in autocomplete mode, but if you want you can modify its contents",
        #             widget=forms.TextInput(attrs={"class": "form-control form-control-sm", 'placeholder': 'Enter slug:'}),
        #             )

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
