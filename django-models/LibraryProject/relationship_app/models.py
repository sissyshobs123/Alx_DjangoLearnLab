# Create your models here.

from django.db import models

# One-to-One Relationship
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


# Many-to-One (ForeignKey) Relationship
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Many-to-Many Relationship
class Project(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee)

    def __str__(self):
        return self.name
