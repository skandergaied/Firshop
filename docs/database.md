# Database

Firshop uses PostgreSQL. Tables are created by Django migrations
(`python manage.py migrate`).

## Relationships

```mermaid
erDiagram
    USER ||--o{ ADDRESS : has
    USER ||--o| CART : owns
    CART ||--o{ CART_ITEM : contains
    PRODUCT ||--o{ CART_ITEM : "is in"
    CATEGORY ||--o{ PRODUCT : groups
    CATEGORY ||--o{ CATEGORY : "has subcategories"
    PRODUCT ||--o{ PRODUCT_IMAGE : has
    USER ||--o{ ORDER : places
    ORDER ||--o{ ORDER_ITEM : contains
    PRODUCT |o--o{ ORDER_ITEM : "referenced by"
```

## Tables

### User (`users`)
| Field | Type | Notes |
|---|---|---|
| username, email | text | email is unique |
| first_name, last_name | text | |
| phone | text | optional |
| is_staff | boolean | can access the admin |

### Address (`users`)
| Field | Type | Notes |
|---|---|---|
| user | FK to User | deleted with the user |
| full_name, phone, street, city, postal_code, country | text | |
| is_default | boolean | |

### Category (`products`)
...

### Product (`products`)
...

### ProductImage (`products`)
...

### Cart and CartItem (`cart`)
...

### Order and OrderItem (`orders`)
...
