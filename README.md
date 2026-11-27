# Firshop

Firshop is a full-stack e-commerce platform. Customers can browse products,
add them to a cart, and place orders with cash on delivery. Shop owners
manage products and orders from an admin panel.

## Tech stack

- Backend: Django, Django REST Framework, PostgreSQL
- Authentication: JWT (djangorestframework-simplejwt)
- Frontend: React (planned)
- DevOps: Docker, GitHub Actions, AWS (planned)

## Features

- User registration and JWT login
- Saved shipping addresses
- Product catalog with categories and images
- Shopping cart with stock validation
- Orders with checkout and automatic stock update
- Prices frozen at purchase time
- Cash on delivery (online payment planned)
- Admin panel to manage products and orders

## Project structure

```
Firshop/
├── backend/
│   ├── config/      # Django settings and main URLs
│   ├── users/       # Custom user, registration, login, addresses
│   ├── products/    # Categories, products, images
│   ├── cart/        # Cart and cart items
│   └── orders/      # Checkout, orders, order items, payment method
├── docs/            # API and project documentation
├── docker-compose.yml
└── README.md
```

## Getting started

### Requirements

- Python 3.13
- Docker Desktop
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USER/Firshop.git
   cd Firshop
   ```
2. Start the PostgreSQL database:
   ```bash
   docker compose up -d
   ```
3. Create and activate a virtual environment:
   ```bash
   cd backend
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```
6. Create an admin user:
   ```bash
   python manage.py createsuperuser
   ```
7. Start the server:
   ```bash
   python manage.py runserver
   ```

The API is available at `http://127.0.0.1:8000/api/` and the admin panel
at `http://127.0.0.1:8000/admin/`.

## Environment variables

Copy `.env.example` to `.env` and fill in your own values.
Never commit the `.env` file.

| Variable     | Description                         |
| ------------ | ----------------------------------- |
| `SECRET_KEY` | Django secret key                   |
| `DEBUG`      | `True` for development only         |

## API documentation

See [docs/api.md](docs/api.md) for the list of endpoints.

## Roadmap

- [x] Users and JWT authentication
- [x] Products and categories
- [x] Cart
- [x] Orders and cash on delivery
- [ ] Pagination, search and filtering
- [ ] Online payment (Konnect or Paymee)
- [ ] React frontend
- [ ] Docker images for backend and frontend
- [ ] CI with GitHub Actions
- [ ] Deployment on AWS