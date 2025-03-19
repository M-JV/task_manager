# Tasku - The Task Manager Web Application

## Overview
This is a Task Manager web application built using Django. It allows users to create, view, and manage tasks with predefined categories. The system follows security best practices, ensuring safe and efficient task management.

## Features
- **Create Tasks:** Users can create tasks by selecting from predefined categories.
- **View Tasks:** Users can see all tasks and their details.
- **Task Categories:** Categories are predefined and managed by the admin panel. Users can only select existing categories when creating tasks.
- **Error Handling:** Custom 404 (Not Found) and 500 (Server Error) pages are in place.
- **Security:**
    - *CSRF protection enabled.*
    - *Admin panel access restricted to manage categories.*

## Requirements
1. Python 3.12.3 (or higher)
2. Django 4.2.11
3. Ubuntu 24 (or other OS with the required dependencies)

## Setup Instructions

### 1. Install Dependencies
Install Python 3.12 and Django 4.2.11:

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install django
```
### 2. Clone the Repository
Clone the repository and navigate to the project folder:
```bash
git clone <your-repository-url>
cd task_manager
```

### 3. Setup the Database
Apply database migrations to set up your database schema:

```bash
python3 manage.py migrate
```
### 4. Create a Superuser for Admin Access
Create a superuser to access the Django admin panel:

```bash
python3 manage.py createsuperuser
```

Follow the prompts to set up the superuser account.

### 5. Run the Development Server
To run the project locally:

```bash
python3 manage.py runserver
```
Access the application at http://127.0.0.1:8000.

# URL Structure
1. **Home Page:** `/` – Displays a welcome message and navigation.
2. **Task List:** `/tasks/` – List of all tasks.
3. **Task Detail:** `/tasks/<task_id>/` – Details of a specific task.
4. **Task Create:** `/tasks/create/` – Form to create a new task.
5. **Categories:** `/categories/` – List of all categories.
6. **Category Tasks:** `/categories/<category_id>/` – Tasks in a specific category.

# Admin Panel
You can manage the categories through the Django Admin Panel by accessing:

- **URL:** `/admin`
- Use the superuser credentials to log in.

# Error Handling
- **Custom 404 Page:** Shown for non-existent pages.
- **Custom 500 Page:** Shown for server errors.

# Security Best Practices
1. **CSRF Protection:** Enabled for all forms to prevent Cross-Site Request Forgery.
2. SQL Injection Prevention: All views use `get_object_or_404()` to prevent direct database queries.
