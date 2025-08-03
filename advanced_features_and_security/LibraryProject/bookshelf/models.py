# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    # Remove the username field and make email the unique identifier
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default

    objects = CustomUserManager()

    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.email
    

class Book(models.Model):
    # your existing fields here
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class Meta:
        permissions = [
            ("can_view_books", "Can view list of books"),
        ]

    def __str__(self):
        return self.title

