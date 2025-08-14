"""
Unit tests for Book API endpoints.
Covers CRUD operations, filtering, searching, ordering, and permission enforcement.
"""

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        
        # Create sample books
        self.book1 = Book.objects.create(title="Python Basics", author="John Doe", publication_year=2020)
        self.book2 = Book.objects.create(title="Advanced Django", author="Jane Smith", publication_year=2021)

        # Endpoints
        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/update/{self.book1.id}/"
        self.delete_url = f"/api/books/delete/{self.book1.id}/"
        self.detail_url = f"/api/books/{self.book1.id}/"

    def test_list_books(self):
        """Test retrieving list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        """Test creating a book as an authenticated user"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "New Book", "author": "Author Name", "publication_year": 2022}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication (should fail)"""
        data = {"title": "Fail Book", "author": "Anon", "publication_year": 2023}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Test updating a book as an authenticated user"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Updated Python Basics", "author": "John Doe", "publication_year": 2020}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Python Basics")

    def test_delete_book_authenticated(self):
        """Test deleting a book as an authenticated user"""
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        """Test filtering books by title"""
        response = self.client.get(f"{self.list_url}?title=Python Basics")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """Test searching books by title or author"""
        response = self.client.get(f"{self.list_url}?search=Python")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year_desc(self):
        """Test ordering books by publication_year descending"""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
