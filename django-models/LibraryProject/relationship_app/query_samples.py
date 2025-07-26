from relationship_app.models import Author, Book

# Example: Query all books by a specific author
author_name = "CharField"  # Replace with actual author name
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

# Print results (optional for debugging)
for book in books_by_author:
    print(book)
