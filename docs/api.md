# Firshop API

Base URL (local): `http://127.0.0.1:8000/api`
All requests and responses use JSON.

## Authentication

Protected endpoints need this header:

```
Authorization: Bearer <access token>
```

The access token lasts 5 minutes. Use the refresh endpoint to get a new one.

---

## Auth

### Register
`POST /auth/register/` (no token)

Request body:
```json
{
  "username": "client1",
  "email": "client1@test.com",
  "first_name": "Ali",
  "last_name": "Ben",
  "phone": "20123456",
  "password": "StrongPass#2026"
}
```
Response: `201 Created`

Errors: `400` if a field is missing, the username exists, or the password is too weak.

### Login
`POST /auth/login/` (no token)

Request body:
```json
{ "username": "client1", "password": "StrongPass#2026" }
```
Response: `200 OK`
```json
{ "refresh": "...", "access": "..." }
```
Errors: `401` for wrong credentials.

---

## Products

### List products
`GET /products/` (no token)

Response: `200 OK`, a list of products with their images.

### List categories
`GET /categories/` (no token)

Response: `200 OK`, a list of categories.