from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
from .models import Book, Comment
from .serializers import BookSerializer
from .serializers import CommentSerializer
from .permissions import IsSpecialUser

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []  # public list (or set IsAuthenticated for protected)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Example: keep it public for reads but require auth for writes using DjangoModelPermissions
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]  # requires add/change/delete/view perms

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSpecialUser]