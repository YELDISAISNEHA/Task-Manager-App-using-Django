# Task Manager App Using Django
### 1. Create a Project Folder
       - mkdir my_django_project
       - cd my_django_project
### 2. Create virtual environment and Install Dependencies
       - python -m venv .venv 
       - .venv\Scripts\activate
       - pip install django
### 3. Create Django Project
       - django-admin startproject task_manager
### 4. Create static & templates folder
       - static: Place all the .css, .js, .img and files here
       - templates: Place all the .html files here
### 5. Settings.py setup
       - "DIRS": [BASE_DIR / 'templates'] <- Add this in TEMPLATES List
       - STATICFILES_DIRS = [BASE_DIR / 'static'] <- Add this immediate below to the (STATIC_URL = "static/")
### 6. Run the Server
       - python manage.py runserver
       - Open the browser -> http://127.0.0.1:8000/
