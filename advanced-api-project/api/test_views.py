from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(title="Sample Book", publication_year=2023, author=self.author)

    def test_create_book(self):
        response = self.client.post('/api/books/', {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        response = self.client.put(f'/api/books/{self.book.id}/', {
            "title": "Updated Title",
            "publication_year": 2023,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
