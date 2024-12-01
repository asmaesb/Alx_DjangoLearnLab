from django.shortcuts import render

# Create your views here.
import rest_framework.generics as generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
