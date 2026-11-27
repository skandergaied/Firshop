# Decisions

A short log of important choices and the reasons behind them.

## 1. Django admin for product management
- **Date:** 2026-11-13
- **Context:** The shop owner needs a way to add products, categories, and images.
- **Decision:** Use the built-in Django admin for the MVP. The public API is read-only for products.
- **Why:** It works with no extra code, which saves weeks. A custom React dashboard can come later.
- **Trade-off:** The admin looks generic and is not built for customers.

## 2. Monorepo
- **Context:** The project has a Django backend and a React frontend.
- **Decision:** One Git repository with `backend/` and `frontend/` folders.
- **Why:** Simpler for one developer, and Docker and CI can see both parts.

## 3. JWT authentication
- **Context:** A React app on another origin needs to log users in.
- **Decision:** Use JWT (djangorestframework-simplejwt) with a short-lived access token and a refresh token.
- **Why:** Works well with a separate frontend and with Postman.
- **Trade-off:** Where the frontend stores tokens needs care. HttpOnly cookies are safer than localStorage.

## 4. Cash on delivery first
- **Date:** 2026-11-18
- **Context:** Stripe is not available in Tunisia.
- **Decision:** Launch with cash on delivery. Add an online provider (Konnect or Paymee) later.
- **Why:** COD is common in Tunisia and needs no provider approval. The `payment_method` field lets us add online payment without changing the cart or checkout flow.
- **Trade-off:** The owner must collect and confirm payment manually.

## 5. Delivery status and payment status are separate
- **Decision:** `Order.status` tracks delivery, and `Order.payment_status` tracks payment.
- **Why:** A COD order is delivered before it is paid, and an online order can be paid but not yet shipped.

## 6. Logged-in users only for the cart
- **Decision:** Guest carts are not supported yet.
- **Why:** Keeps the first version simple.
- **Trade-off:** Guests must register before adding items. We may add guest carts later.

## 7. Redis and Celery postponed
- **Decision:** Not added yet.
- **Why:** There is no performance problem, and the core shop is not finished. They add services to run and pay for.
- **Revisit when:** Order confirmation emails, caching, or rate limiting are needed.

## 8. PostgreSQL from the start
- **Decision:** Use PostgreSQL in Docker for development, not SQLite.
- **Why:** Development matches production (AWS RDS), which avoids surprises later.