import os
import sys
import django

# Add the Django project root directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Department, Employee, Project, Profile
from django.contrib.auth.models import User

# Create a department
dept = Department.objects.create(name="Engineering")

# Create an employee
emp = Employee.objects.create(name="Blessing Malik", department=dept)

# Create a project and assign employees
project = Project.objects.create(name="Django Revamp")
project.employees.add(emp)

# Create a user and profile
user = User.objects.create_user(username="blessing", password="admin123")
profile = Profile.objects.create(user=user, bio="Full-stack Django Developer")

print("Sample data created successfully.")
