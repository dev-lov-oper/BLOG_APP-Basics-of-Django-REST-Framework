# Django REST Framework Blog API

A RESTful Blog API built using **Django** and **Django REST Framework (DRF)**. This project demonstrates the implementation of core backend development concepts such as authentication, permissions, serialization, filtering, searching, ordering, and pagination.

## Features

* Create, Read, Update, and Delete (CRUD) blog posts
* RESTful API architecture
* Django REST Framework serializers
* Custom and built-in permissions
* Search and filtering functionality
* Ordering of API results
* Pagination support
* User authentication and authorization
* Clean and scalable project structure

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (can be replaced with PostgreSQL/MySQL)
* DRF Filters

## API Functionality

### Posts

* Create a blog post
* View all blog posts
* Retrieve a single blog post
* Update a blog post
* Delete a blog post

### Permissions

Implemented permissions to ensure:

* Authenticated users can create posts
* Only post authors can update or delete their posts
* Read access is available to all users

### Serialization

Used DRF Serializers to:

* Convert model instances into JSON responses
* Validate incoming request data
* Handle object creation and updates

### Filtering & Searching

Supports:

* Search blog posts by title/content
* Filter data using query parameters
* Order results based on fields such as creation date

Example:

```http
GET /api/posts/?search=django
GET /api/posts/?ordering=-created_at
```

### Pagination

Implemented DRF pagination to efficiently handle large datasets.


## Project Structure

```text
blog_api/
│
├── blog/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│
├── blog_api/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── requirements.txt
```

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/blog-api.git
cd blog-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Development Server

```bash
python manage.py runserver
```

Server will run at:

```text
http://127.0.0.1:8000/
```

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Django REST Framework
* API design principles
* Serializers and validation
* Authentication & permissions
* Filtering, searching, and ordering
* Pagination techniques
* Building scalable backend applications

## Future Improvements

* JWT Authentication
* Comments API
* Categories & Tags
* Likes and Reactions
* API Documentation with Swagger/OpenAPI
* Deployment using Docker and Cloud Services



Computer Science Student | Backend Development Enthusiast | Learning Django & REST APIs
