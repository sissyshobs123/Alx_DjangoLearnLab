# Task 1: Managing Permissions and Groups in Django

## Custom Permissions Defined
In `LibraryProject/bookshelf/models.py`, we defined custom permissions for the `Book` model as follows:

```python
class Meta:
    permissions = [
        ("can_view_books", "Can view book list"),
    ]
