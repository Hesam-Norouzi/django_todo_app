# Django To-Do Project – Development Log

## Stage 1: Initial Project Setup
- Create the project using the command `django-admin startproject django_todo_project`
- Create an application named `tasks` using the command `python manage.py startapp tasks`
- Add the application to `INSTALLED_APPS` in `settings.py`
- Run `python manage.py migrate` to create the initial SQLite database

## Stage 2: Create Task model

We created a `Task` model inside the `tasks` app. This model represents individual to-do tasks linked to users. The model includes fields for the task title, optional description, completion status, creation date, and an optional due date.

Key choices:
- Each task is associated with a Django `User` using a ForeignKey.
- `auto_now_add=True` is used for `created_at` to automatically set the timestamp when a task is created.
- `is_completed` helps in toggling the completion state of a task.

## Step 2: Create and apply migrations

We generated and applied database migrations for the `Task` model using the following commands:

```python
python manage.py makemigrations tasks
python manage.py migrate
```
This creates the necessary database table to store Task records.

🚀 Status: Project is on progress