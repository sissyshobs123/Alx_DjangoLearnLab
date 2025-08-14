"""
Views for managing Book API endpoints using Django REST Framework.
Includes both read-only and write operations, with appropriate permissions applied.
"""

from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
import logging

logger = logging.getLogger(__name__)

class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books in the system with filtering, searching, and ordering.
    - Method: GET
    - Permissions: Public (read-only)
    - Filtering: filter by title, author, publication_year
    - Searching: search in title and author's name
    - Ordering: order by title or publication_year
    Example:
        /api/books/?search=Python
        /api/books/?ordering=title
        /api/books/?title=SomeTitle
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Add filtering/searching/ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by its ID.
    - Method: GET
    - Permissions: Public (no authentication required)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    - Method: POST
    - Permissions: Authenticated users only
    - Custom behavior: Logs book data before saving
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        logger.info(f"Creating book with data: {serializer.validated_data}")
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    - Method: PUT/PATCH
    - Permissions: Authenticated users only
    - Custom behavior: Logs updated book data before saving
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        logger.info(f"Updating book with data: {serializer.validated_data}")
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    - Method: DELETE
    - Permissions: Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
