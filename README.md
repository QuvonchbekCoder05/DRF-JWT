# Blog API using Django Rest Framework and JWT Authentication

This is a simple blog API built with Django Rest Framework (DRF) and JWT (JSON Web Token) authentication. The API allows users to register, log in, create, update, and delete blogs, as well as comment on blogs. Only authenticated users can perform certain actions like commenting or managing their own blogs.

## Features

1. **User Registration and Login**: 
   - Users can sign up and log in using JWT authentication.
   - Tokens are used to authenticate users and allow them to access protected endpoints.
   
2. **Blog List with Filtering, Ordering, and Search**:
   - Users can list all blogs, filter by title, search for specific blogs, and order them.
   
3. **Blog Detail**:
   - Users can view detailed information about a specific blog.
   
4. **Profile List and Detail**:
   - Each user has a profile that lists all the blogs they have created.
   
5. **Comment on Blogs**:
   - Authenticated users can add comments to blogs. Comments are linked to both the blog and the user who posted them.
   
6. **My Blogs (CRUD)**:
   - Users can manage their own blogs with full CRUD functionality (Create, Read, Update, Delete). Only the owner of a blog can update or delete it.

## API Endpoints

### Authentication

- **Sign up**: `POST /api/signup/`
   - Allows users to create an account.
   - Requires `username` and `password` fields.
   
- **Login**: `POST /api/token/`
   - Allows users to log in and retrieve a JWT token.
   - Requires `username` and `password` fields.

- **Token Refresh**: `POST /api/token/refresh/`
   - Allows users to refresh their JWT tokens.

### Blogs

- **List Blogs**: `GET /api/blogs/`
   - Returns a list of all blogs.
   - Supports search by title: `GET /api/blogs/?search=<search_term>`.
   
- **Create Blog**: `POST /api/blogs/`
   - Allows authenticated users to create a new blog.
   - Requires `title` and `content` fields.

- **Blog Detail**: `GET /api/blogs/<id>/`
   - Returns detailed information about a specific blog.

- **Update Blog**: `PUT /api/blogs/<id>/`
   - Allows the owner of the blog to update it.
   
- **Delete Blog**: `DELETE /api/blogs/<id>/`
   - Allows the owner of the blog to delete it.

### User Profiles

- **User Blog List**: `GET /api/profile/<user_id>/blogs/`
   - Returns a list of blogs created by the specified user.

### Comments

- **Add Comment**: `POST /api/blogs/<id>/comment/`
   - Allows authenticated users to add a comment to a blog.
   - Requires `content` field.

### My Blogs (CRUD)

- **My Blogs**: `GET /api/my-blogs/`
   - Returns a list of blogs created by the currently authenticated user.
   
- **Create My Blog**: `POST /api/my-blogs/`
   - Allows the authenticated user to create a blog.
   
- **Update My Blog**: `PUT /api/my-blogs/<id>/`
   - Allows the authenticated user to update their own blog.
   
- **Delete My Blog**: `DELETE /api/my-blogs/<id>/`
   - Allows the authenticated user to delete their own blog.

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd blog_project
