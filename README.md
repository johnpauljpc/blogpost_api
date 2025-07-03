# 📝 Blog Post API

A RESTful API built with Django and Django REST Framework to manage blog authors and their posts. It allows users to register, log in, and perform full CRUD operations on blog posts.

---

## 🚀 Features

> - ✅ User registration & login  
> - ✍️ Create, read, update, and delete blog posts  
> - 👥 View authors of posts  
> - 🔐 Authenticated access required for protected routes  
> - 📚 Swagger documentation for interactive API testing

---

## 📦 API Endpoints

### 🔐 Accounts

| Method | Endpoint               | Description           |
|--------|------------------------|-----------------------|
| POST   | `/accounts/login/`     | Log in a user         |
| POST   | `/accounts/register/`  | Register a new user   |

---

### 📝 Posts

| Method | Endpoint                | Description                          |
|--------|-------------------------|--------------------------------------|
| GET    | `/posts/`               | List all posts                       |
| POST   | `/posts/`               | Create a new post (auth required)    |
| GET    | `/posts/{id}/`          | Retrieve a single post               |
| PUT    | `/posts/{id}/`          | Full update of a post (auth required)|
| PATCH  | `/posts/{id}/`          | Partial update (auth required)       |
| DELETE | `/posts/{id}/`          | Delete a post (auth required)        |
| GET    | `/posts/authors/`       | List all post authors                |

---

## 🔐 Authentication

> Obtain tokens via:
>
> ```http
> POST /accounts/login/
> ```
>
> Then include in headers:
>
> ```http
> Authorization: Bearer <your-token> <br>
>omit Bearer when using the interactive Swagger UI, Just use the token alone.
> ```

---

## ⚙️ Tech Stack

> - Python 3  
> - Django  
> - Django REST Framework  
> - Simple JWT (for authentication)  
> - drf-spectacular (for Swagger UI)

---

## 📚 API Documentation

> Interactive Swagger docs available, explore and test the API interactively at:
> `http://127.0.0.1:8000/`
> 

---

## 🧪 Running Locally

```bash
# Clone the repository
git clone https://github.com/your-username/blog-post-api.git
cd blog-post-api

# Set up virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```
---

## 📬 Contact
Feel free to contribute or reach out:<br>
**GitHub:** *@johnpauljpc* <br>
**Email:** *jpcwork081@gmail.com* <br>
**X:** *@iam_johnpauljp*

>If you found this helpful, kindly give it a Star ⭐. THANKS 🤝
