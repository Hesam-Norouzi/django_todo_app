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

## Step 3: Create and apply migrations

We generated and applied database migrations for the `Task` model using the following commands:

```python
python manage.py makemigrations tasks
python manage.py migrate
```
This creates the necessary database table to store Task records.

## Step 4: Create base template

We created a reusable base template for all pages at `tasks/templates/tasks/base.html`. This will ensure layout consistency and reduce duplication.

## Step 5: Display Task List

- Created `task_list` view to show only the authenticated user's tasks.
- Used `@login_required` decorator to restrict access.
- Added `task_list.html` template with Tailwind styling.
- Configured URLs to route `'/'` to the task list view.

## Step 6: Add Task Functionality

- Created `TaskForm` using `ModelForm` for task creation.
- Added `add_task` view to handle GET and POST requests.
- Built `add_task.html` template with a form.
- Linked to the add task page from the task list view.

### Step 7: Edit and Delete Tasks

- Created two new views: `edit_task` and `delete_task`, both restricted to the task owner.
- Added corresponding templates: `edit_task.html` and `delete_task.html`.
- Configured URLs for editing and deleting tasks.
- Updated task list UI to include "Edit" and "Delete" buttons next to each task.

These features allow users to manage their tasks more efficiently.

## Step 8: Mark Task as Completed

- Added `complete` BooleanField to `Task` model.
- Created `toggle_complete` view to switch task status.
- Added a toggle button to task list with dynamic style.
- Displayed completed tasks with strike-through and muted color.

## Step 9: Filter Tasks
- Updated task_list view to support filtering by completed status.
- Added filter buttons (All / Completed / Pending) to the template.
- Highlighted active filter with Bootstrap active class.

## Step 10: Task Filtering and Search
- Implemented filter by status (completed, pending, all)
- Added search functionality using `title__icontains`
- Combined filter and search into a single `task_list` view
- Ensured task visibility is limited to the logged-in user

## Step 11: Pagination

- Integrated Django’s `Paginator` to limit tasks per page (5 per page)
- Preserved search and filter query parameters across pages
- Updated template to include pagination controls with Bootstrap styling
- Improved UX for users with many tasks

🚀 Status: Project is on progress