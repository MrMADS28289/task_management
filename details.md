# Project Details: Task Management System

This document provides an in-depth technical overview of the Task Management System, covering its architecture, database schema, detailed setup, and development practices.

## 1. Project Architecture

The Task Management System is a web application built using the Django framework for the backend and leverages Tailwind CSS for styling on the frontend. It follows a standard Model-View-Controller (MVC) pattern (or Model-View-Template in Django's terminology).

-   **Backend (Django):** Handles data models, business logic, API endpoints, and serves HTML templates.
-   **Frontend (HTML/CSS/JS):** Primarily uses HTML templates rendered by Django, styled with Tailwind CSS. Minimal JavaScript is used for interactivity.
-   **Database:** PostgreSQL is used as the primary database for persistent storage.

## 2. Database Schema

The core entities and their relationships are as follows:

### `users` App

#### `CustomUser` Model
Extends Django's `AbstractUser` to include custom fields.

-   `id`: Primary Key (auto-incrementing)
-   `username`: (CharField) User's unique username.
-   `email`: (EmailField) User's email address.
-   `password`: (CharField) Hashed password.
-   `profile_image`: (ImageField) Path to user's profile picture (uploads to `media/profile_images/`).
-   `bio`: (TextField) Short biography of the user.
-   Standard `AbstractUser` fields (e.g., `first_name`, `last_name`, `is_active`, `is_staff`, `date_joined`).

### `tasks` App

#### `Project` Model
Represents a project that tasks belong to.

-   `id`: Primary Key (auto-incrementing)
-   `name`: (CharField) Name of the project.
-   `description`: (TextField) Optional description of the project.
-   `start_date`: (DateField) The date the project started.

#### `Task` Model
Represents an individual task within a project.

-   `id`: Primary Key (auto-incrementing)
-   `project`: (ForeignKey) Links to the `Project` model (on_delete=CASCADE).
-   `assigned_to`: (ManyToManyField) Links to `CustomUser` model (related_name='tasks'). A task can be assigned to multiple users.
-   `title`: (CharField) Title of the task.
-   `description`: (TextField) Detailed description of the task.
-   `due_date`: (DateField) The date the task is due.
-   `status`: (CharField) Current status of the task (choices: 'PENDING', 'IN_PROGRESS', 'COMPLETED').
-   `created_at`: (DateTimeField) Timestamp when the task was created (auto_now_add=True).
-   `updated_at`: (DateTimeField) Timestamp when the task was last updated (auto_now=True).

#### `TaskDetail` Model
Provides additional details for a `Task`.

-   `id`: Primary Key (auto-incrementing)
-   `task`: (OneToOneField) Links to the `Task` model (on_delete=DO_NOTHING, related_name='details'). Each task has one `TaskDetail`.
-   `asset`: (ImageField) Optional image related to the task (uploads to `media/tasks_asset/`).
-   `priority`: (CharField) Priority level (choices: 'H' for High, 'M' for Medium, 'L' for Low).
-   `notes`: (TextField) Additional notes for the task.

## 3. Detailed Setup and Installation

This section elaborates on the setup process, including specific configurations and troubleshooting.

### 3.1. Prerequisites

-   **Python 3.x:** Recommended Python version for Django 5.1.x.
-   **Node.js & npm:** Required for Tailwind CSS compilation.
-   **PostgreSQL:** Database server. Ensure it's running and accessible.

### 3.2. Environment Variables (`.env`)

The project uses `python-decouple` to manage environment variables. Create a `.env` file in the project root with the following:

```ini
SECRET_KEY=your_generated_secret_key
DEBUG=True
DB_PORT=5432
EMAIL_HOST=smtp.your-email-provider.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_app_password
```

-   `SECRET_KEY`: Crucial for Django's security. Generate using `python generate_secret_key.py`.
-   `DEBUG`: Set to `True` for development, `False` for production.
-   `DB_PORT`: Your PostgreSQL port (default is 5432).
-   `EMAIL_*`: SMTP settings for sending emails (e.g., password reset, account verification).

### 3.3. Database Configuration (`task_management/settings.py`)

Ensure your `DATABASES` setting is configured for PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'task_management',
        'USER': 'postgres',
        'PASSWORD': 'password', # Replace with your PostgreSQL password
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

### 3.4. Migrations Troubleshooting (`InconsistentMigrationHistory`)

If you encounter `InconsistentMigrationHistory` errors, it typically means your database's migration history is out of sync with your project's migration files. To resolve this:

1.  **Drop and Recreate Database:**
    ```bash
    # Connect to PostgreSQL as a superuser (e.g., postgres)
    psql -U postgres
    DROP DATABASE task_management;
    CREATE DATABASE task_management;
    \q
    ```
2.  **Delete Local Migration Files:** Remove all migration files (except `__init__.py`) from your app's `migrations` directories:
    ```bash
    rm tasks/migrations/0*.py
    rm users/migrations/0*.py
    ```
3.  **Remake and Apply Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## 4. Key Django Apps and Responsibilities

-   **`core`:** Contains core functionalities like the home page and error handling (e.g., `no_permission` view).
-   **`tasks`:** Manages all task-related logic, including `Task`, `TaskDetail`, and `Project` models, views for task creation/listing/updating, and associated URLs.
-   **`users`:** Handles user authentication and management, including the `CustomUser` model, user registration, login, logout, and profile management.

## 5. Frontend Technologies

-   **Tailwind CSS:** A utility-first CSS framework used for rapid UI development. The `package.json` defines scripts for building (`build:tailwind`) and watching (`watch:tailwind`) CSS changes.
    -   `static/css/tailwind.css`: Input file for Tailwind directives.
    -   `static/css/output.css`: Generated minified CSS output.

## 6. Development Workflow

### 6.1. Linting (Ruff)

`ruff` is used for fast Python linting. It helps enforce code style and identify potential errors.

-   **Installation:** `pip install ruff`
-   **Usage:** `ruff check . --fix` (to check and automatically fix issues).

### 6.2. Type Checking (Mypy)

`mypy` is used for static type checking of Python code, improving code reliability and maintainability.

-   **Installation:** `pip install mypy django-stubs`
-   **Configuration:** `mypy.ini` in the project root configures `mypy` to work with Django and ignore missing stubs for certain third-party libraries.
    ```ini
    [mypy]
    plugins = mypy_django_plugin.main

    [mypy.plugins.django-stubs]
    django_settings_module = task_management.settings

    [mypy-decouple.*]
    ignore_missing_imports = True

    [mypy-debug_toolbar.*]
    ignore_missing_imports = True
    ```
-   **Usage:** `mypy .`

## 7. Database Population

The `populate_db.py` script can be used to generate sample data for `Projects`, `CustomUsers`, `Tasks`, and `TaskDetails` for development and testing purposes.

-   **Usage:** `python populate_db.py`

## 8. Media Files

User profile images and task-related assets are stored in the `media/` directory, configured by `MEDIA_ROOT` and `MEDIA_URL` in `settings.py`.

-   `media/profile_images/`: Stores user profile pictures.
-   `media/tasks_asset/`: Stores images associated with tasks.

This detailed overview should provide a comprehensive understanding of the Task Management System's technical aspects.