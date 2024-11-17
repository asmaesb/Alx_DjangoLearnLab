# bookshelf/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
        
class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)