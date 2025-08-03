from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book
from .forms import ExampleForm


def is_editor(user):
    return user.groups.filter(name='Editors').exists()

@user_passes_test(is_editor)
def editor_only_view(request):
    return HttpResponse("Welcome, Editor! You have access to this page.")


def is_librarian(user):
    return user.groups.filter(name="Librarians").exists()

@login_required
@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'librarian_dashboard.html')

@permission_required('bookshelf.can_view_books', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})