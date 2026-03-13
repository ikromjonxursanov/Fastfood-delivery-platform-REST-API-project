Last login: Thu Mar 12 20:30:38 on console
azizkhan@MacBook-Pro--Bunyod-908591089 ~ % cd django-darslari
azizkhan@MacBook-Pro--Bunyod-908591089 django-darslari % cd fastfood_delivery
azizkhan@MacBook-Pro--Bunyod-908591089 fastfood_delivery % cd apps
azizkhan@MacBook-Pro--Bunyod-908591089 apps % pwd
/Users/azizkhan/django-darslari/fastfood_delivery/apps
azizkhan@MacBook-Pro--Bunyod-908591089 apps % touch README.md
azizkhan@MacBook-Pro--Bunyod-908591089 apps % nano README.md






















































  UW PICO 5.09                                                                                                  File: README.md                                                                                                   Modified  
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

```bash
git clone https://github.com/ikromjonxursanov/Fastfood-delivery-platform-REST-API-project.git
cd Fastfood-delivery-platform-REST-API-project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
