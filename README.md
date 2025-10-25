Mini Blog 
---------

A simple Django project to create, view, edit, and delete posts — a basic CRUD app to learn Django framework.


---

### Setup Steps 

1. Create Virtual Environment
python3 -m venv venv


2. Activate Virtual Environment
source venv/bin/activate


3. Install Django
pip install django


4. Create Project and App
django-admin startproject myblog
python3 manage.py startapp posts


5. Add App
Adding 'posts' inside INSTALLED_APPS in myblog/settings.py


6. Run Migrations
python3 manage.py migrate


7. Create Superuser
python3 manage.py createsuperuser


8. Run Server
python3 manage.py runserver


9. Open in Browser
http://127.0.0.1:8000

10. Features

Add new posts
Edit existing posts
Delete posts
View all posts on homepage
Manage from Django Admin
