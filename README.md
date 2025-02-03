# My First Django Site

This is a simple blog project built with Django. The backend was coded by me, and the frontend is based on a free-to-download template. This project was created for learning purposes.

## Features

- User authentication (login, logout, register)
- Create, read, update, and delete blog posts
- Comment on blog posts
- Responsive design

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ariwsb14/my-first-django-site.git
   cd my-first-django-site
   
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Apply migrations:
   ```bash
   python manage.py migrate
   
5. Create a superuser:
   ```bash
   python manage.py createsuperuser

6. Run the development server:
   ```bash
   python manage.py runserver

7. Open your browser and go to http://127.0.0.1:8000/ to see the site in action
