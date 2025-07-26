# LibraryProject

This is the initial setup for the Django project named **LibraryProject**, created as part of the **ALX Django Learn Lab**.


## Setup Steps

1. Installed Django using pip: pip install django


2. Created the Django project: django-admin startproject LibraryProject


3. Ran the development server: python manage.py runserver


4. Accessed the app at: http://127.0.0.1:8000/

Django Model Relationships
This project demonstrates the use of Django’s model relationships:

Relationships Used
OneToOneField – Links one model to exactly one other (e.g. Author → Profile)

ForeignKey – Links many items to one (e.g. Post → Author)

ManyToManyField – Links many items to many (e.g. Student ↔ Course)

 Models Created
Author

Post (linked to Author)

Profile (one-to-one with Author)

Student and Course (many-to-many)

query_samples.py
This script creates sample data and runs Django ORM queries to test relationships.

Run with:

bash:
python relationship_app/query_samples.py



