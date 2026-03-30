
# FastFood Delivery API

FastFood Delivery API is a RESTful service designed for restaurants to manage menu items, handle orders, and control user roles efficiently. This project is ideal for learning Django REST Framework, role-based permissions, and API best practices.

---

## Features

- Admin: Full access to manage all menu items, categories, and orders  
- Waiter: Can accept, update, and view orders  
- User: Can view menu items and place orders  
- JWT Authentication for secure access  
- CRUD operations for menu items and categories

---

## Tech Stack

- Backend: Python 3.x, Django 4.x, Django REST Framework  
- Database: PostgreSQL or SQLite  
- Authentication: JWT (JSON Web Tokens)  
- Tools: Postman for testing APIs

---

## Installation

```zsh
git clone https://github.com/ikromjonxursanov/Fastfood-delivery-platform-REST-API-project.git
cd Fastfood-delivery-platform-REST-API-project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
