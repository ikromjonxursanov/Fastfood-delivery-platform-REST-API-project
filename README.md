
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

---

### Environment variables

`.env` fayl yarating:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### Database & run
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📁 Project Structure
```
├── config/          # Settings, main URLs
├── user/            # Auth, profile management
├── ofitsiant/       # Menu items and categories
├── orders/          # Orders and order items
└── manage.py
```

---

## 🔑 Authentication

Barcha so'rovlar uchun JWT token kerak:
```
POST /api/user/register/      — Ro'yxatdan o'tish
POST /api/user/token/         — Token olish
POST /api/user/token/refresh/ — Tokenni yangilash
```

So'rovda header:
```
Authorization: Bearer <access_token>
```

---

## 📌 API Endpoints

###  User
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/user/register/` | Register |
| POST | `/api/user/token/` | Login (get token) |
| POST | `/api/user/token/refresh/` | Refresh token |
| GET | `/api/user/user/` | My profile |

### 🍕 Menu (Ofitsiant)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/ofitsiant/taomlar/` | All menu items |
| POST | `/api/ofitsiant/taomlar/` | Add item (Admin only) |
| GET | `/api/ofitsiant/category/` | All categories |
| POST | `/api/ofitsiant/category/` | Add category (Admin only) |

### 📦 Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/orders/order/` | My orders |
| POST | `/api/orders/order/` | Place order |
| GET | `/api/orders/orderitem/` | Order items |
| POST | `/api/orders/orderitem/` | Add order item |

---

## 📖 API Documentation

Server ishga tushgandan keyin:

- **Swagger UI:** http://localhost:8000/swagger/
- **Redoc:** http://localhost:8000/redoc/

---

##  Author

**Ikromjon Xursanov**
- GitHub: [@ikromjonxursanov](https://github.com/ikromjonxursanov)
