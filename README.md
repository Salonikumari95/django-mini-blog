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

****Author.
Saloni kumari
Made on Mac for Django CRUD learning project.

###SCREENSORTS
HOME PAGE
<img width="559" height="372" alt="create" src="https://github.com/user-attachments/assets/f6535bac-f3b5-441b-82b8-6e51a8215bc4" />
Home Post: Lists all posts. Shows title, short content, and links to view, edit, or delete each post.


<img width="566" height="466" alt="create-page" src="https://github.com/user-attachments/assets/fe1d9927-fa00-4d65-b229-69142b707959" />
Create Post:	Form to add a new post. Fill title and content, then submit to see it on homepage.


<img width="1365" height="389" alt="blog-created" src="https://github.com/user-attachments/assets/471c4a83-86ad-4f0f-8628-5acff64bc365" />
Blog Created:		Shows the full content of a single post. Includes options to edit or delete the post.

<img width="569" height="517" alt="edit-page" src="https://github.com/user-attachments/assets/139f0c51-d6b5-4d54-95b9-9ba2942fd71d" />
Edit Post:		Form to update an existing post. Pre-filled fields make editing easy.


<img width="927" height="265" alt="delete-page" src="https://github.com/user-attachments/assets/43f7a486-f4ad-45c3-a5bb-37b178494fb4" />
Delete Post	:	Confirms if you want to delete a post. After confirmation, the post is removed.








