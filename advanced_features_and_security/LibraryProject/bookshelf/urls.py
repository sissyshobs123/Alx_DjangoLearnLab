from django.urls import path
from .views import editor_only_view
from .views import librarian_dashboard
from . import views 


urlpatterns = [
    path("editor-only/", editor_only_view, name="editor_only"),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('books/', views.book_list, name='book_list'),
]
