from relationship_app.models import Author, Book, Library, Librarian

# --- Query all books by a specific author ---
author_name = "CharField"  # Replace with actual author name
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

# Optional print for debugging
for book in books_by_author:
    print(f"By Author: {book}")


# --- List all books in a specific library ---
library_name = "Central Library"  # Replace with actual library name
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# Optional print for debugging
for book in books_in_library:
    print(f"In Library: {book}")


# --- Retrieve the librarian for a library ---
librarian = Librarian.objects.get(library__name=library_name)

# Optional print for debugging
print(f"Librarian: {librarian}")
