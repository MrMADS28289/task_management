# Task Management System

This is a web-based Task Management System built with Django, designed to help users organize and manage their tasks efficiently. It includes user authentication, task creation, assignment, and various dashboards for different user roles.

## Features

-   **User Authentication:** Secure user registration, login, logout, password change, and profile management.
-   **Role-Based Access Control:** Different dashboards and permissions for regular users and managers/administrators.
-   **Task Management:** Create, view, update, and delete tasks.
-   **Task Assignment:** Assign tasks to specific users.
-   **User Profiles:** View and update user profile information, including profile images.
-   **Database Seeding:** Script to populate the database with sample data for quick setup.
-   **Responsive Design:** Styled with Tailwind CSS for a modern and responsive user interface.

## Technologies Used

**Backend:**
-   Python 3.x
-   Django (Web Framework)
-   SQLite (Default Database)
-   Pillow (for image processing)
-   Django Crispy Forms

**Frontend:**
-   HTML5
-   CSS3 (Tailwind CSS)
-   JavaScript
-   PostCSS
-   Autoprefixer

## Prerequisites

Before you begin, ensure you have the following installed on your system:

-   Python 3.x
-   pip (Python package installer)
-   Node.js and npm (Node Package Manager)

## Setup Instructions

Follow these steps to get the project up and running on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd task-management
    ```
    *(Replace `<repository_url>` with the actual URL of your Git repository)*

2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv task_env
    # On Windows
    .\task_env\Scripts\activate
    # On macOS/Linux
    source task_env/bin/activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Node.js dependencies:**
    ```bash
    npm install
    ```

5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (administrator account):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create your admin username, email, and password.

7.  **Optional: Populate the database with sample data:**
    ```bash
    python manage.py runscript populate_db
    ```
    This script will create some sample users, tasks, and groups.

8.  **Build Tailwind CSS:**
    To compile your Tailwind CSS, you can run:
    ```bash
    npm run build:css
    ```
    For development, you can run a watcher that rebuilds CSS on changes:
    ```bash
    npm run watch:css
    ```

9.  **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/` in your web browser.

## Project Structure (High-Level)

The project is organized into several Django applications:

-   `core/`: Contains core functionalities like base templates, home page, and general static files.
-   `users/`: Handles all user-related functionalities, including authentication (registration, login, logout), user profiles, and admin functionalities for managing users and groups.
-   `tasks/`: Manages all task-related operations, including creating, viewing, updating, and deleting tasks, as well as dashboards for task overview.
-   `task_management/`: The main Django project configuration, including `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`.

## Database Schema (Key Models)

-   `CustomUser`: Extends Django's default `AbstractUser` for custom user fields.
-   `Profile`: Stores additional user profile information, including profile images.
-   `Task`: Represents a task with details like title, description, due date, status, and assigned user.
-   `TaskDetail`: (If applicable, based on `tasks/models.py` content) Provides additional details or relationships for tasks.

## Usage

After starting the server, navigate to `http://127.0.0.1:8000/`.

-   **Register/Login:** Create a new account or log in with an existing one.
-   **Dashboard:** Access your personalized dashboard based on your user role.
-   **Manage Tasks:** Create new tasks, view existing ones, update their status, or assign them to other users.
-   **Profile:** Update your profile information and image.

## Contributing

Contributions are welcome! Please feel free to fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details. (If you have a LICENSE file, otherwise remove this section or specify your license.)

