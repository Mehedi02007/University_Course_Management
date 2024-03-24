# University Management System

This Django-based web application is designed to manage students and courses within the School of Computer Science at a university. It allows for tracking of courses offered, student enrollments, and provides a clear interface for managing both student and course data.

## Features

- **Manage Courses**: Add, update, and delete courses including details like course name, coordinator, and capacity.
- **Manage Students**: Add, update, and delete student records, including their enrollment in courses.
- **View Enrollments**: Easily view which students are enrolled in each course, along with basic student details.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.10 or higher
- Django 3.2
- pip (Python package manager)

### Installation

0. **Open a terminal window and navigate to the directory where you want to store the project files.**

1. **Clone the repository**

   ```bash
   git clone https://github.com/Mehedi02007/University_Course_Management-main.git
   ```

   ```bash
   cd University_Course_Management
   ```

2. **Set up a virtual environment** (Optional but recommended)

   ```bash
   python -m venv venv
   ```

   - Activate the virtual environment

     - **Windows**

       ```bash
       venv\Scripts\activate
       ```

     - **Linux/MacOS**

       ```bash
       source venv/bin/activate
       ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations to create the database schema**

   ```bash
   python manage.py makemigrations
   ```

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser account**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
    python manage.py runserver
   ```

7. **Visit http://127.0.0.1:8000 in your web browser** to view the application.

### Usage

- Access the Django admin panel at `http://127.0.0.1:8000/admin` using the superuser credentials you created.
- Manage courses and students through the admin panel.
- Use the application's UI to navigate between the list of students, list of courses, and detailed views for each.

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [SQLite](https://www.sqlite.org/index.html) - The database engine
