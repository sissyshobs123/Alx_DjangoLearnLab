from django.db import models

# Author model to store information about book authors
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model linked to an Author
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
