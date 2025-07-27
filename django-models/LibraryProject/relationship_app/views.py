from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  # Use this version for the ALX checker
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

# Existing view to list all books
def list_books(request):
    books = Book.objects.all()  # Use this version for the ALX checker
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Existing class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ✅ NEW: Authentication views
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

from django.http import HttpResponseForbidden
from .models import UserProfile

def admin_dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Login required.")

    try:
        profile = request.user.userprofile
        if profile.role != 'Admin':
            return HttpResponseForbidden("Admins only.")
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("Profile not found.")

    return render(request, 'relationship_app/admin_dashboard.html')
