# galvanize-snacks-api

An api using Python, Flask, SQLAlchemy

## Setup
1. Fork and clone this repository
1. `createdb galvanize-snacks-python-api/`
1. `PYTHONPATH=../ python snack_seeds.py`
1. `PYTHONPATH=../ python review_seeds.py`
1. `python app.py`

## Routes

**GET /snacks**

**GET /snacks/featured**

**GET /snacks/<int:id>**

**POST /api/snacks**
- required fields in body:
```
{
    name,           // STRING
    description,    // STRING
    price,          // FLOAT
    img,            // STRING
    is_perishable   // BOOLEAN
}
```

**POST /snacks/<int:id>/reviews**
- required fields in body:
```
{
    title,          // STRING
    text,           // STRING
    rating,         // INTEGER
}
```

**PATCH /snacks/<int:id>**
- at least one(1) of the following fields in body is required:
```
{
    name,           // STRING
    description,    // STRING
    price,          // FLOAT
    img,            // STRING
    is_perishable   // BOOLEAN
}
```

**PATCH /snacks/<int:snack_id>/reviews/:id**
- at least one(1) of the following fields in body is required:
```
{
    title,          // STRING
    text,           // STRING
    rating,         // INTEGER
}
```

**DELETE /snacks/<int:snack_id>**

**DELETE /snacks/<int:snack_id>/reviews/:id**
