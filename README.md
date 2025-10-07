# Python_Projects

This repository contains small example web projects in Flask, FastAPI (with a React frontend), and a Django habit-tracker.

Projects
- FastAPI To-Do (backend): [FastAPI/todo_list/main.py](FastAPI/todo_list/main.py) — FastAPI app instance [`app`](FastAPI/todo_list/main.py). See database and models: [`database.py`](FastAPI/todo_list/database.py), [`models.py`](FastAPI/todo_list/models.py), request/response schemas: [`schemas.py`](FastAPI/todo_list/schemas.py), and routes: [`routes/tasks.py`](FastAPI/todo_list/routes/tasks.py) (e.g. [`create_task`](FastAPI/todo_list/routes/tasks.py), [`get_tasks`](FastAPI/todo_list/routes/tasks.py)).
- FastAPI To-Do (frontend): React app in [FastAPI/todo-frontend](FastAPI/todo-frontend). Main UI: [FastAPI/todo-frontend/src/App.js](FastAPI/todo-frontend/src/App.js), styles: [FastAPI/todo-frontend/src/App.css](FastAPI/todo-frontend/src/App.css), package file: [FastAPI/todo-frontend/package.json](FastAPI/todo-frontend/package.json).
- URL Shortener (FastAPI): [FastAPI/URL_Shortner/main.py](FastAPI/URL_Shortner/main.py) — endpoints [`shorten_url`](FastAPI/URL_Shortner/main.py) and [`redirect_url`](FastAPI/URL_Shortner/main.py).
- Flask To-Do: [Flask/todo_app/app.py](Flask/todo_app/app.py) — Flask app instance [`app`](Flask/todo_app/app.py). Local JSON store: [Flask/todo_app/todos.json](Flask/todo_app/todos.json), dependencies: [Flask/todo_app/requirements.txt](Flask/todo_app/requirements.txt).
- Django Habit Tracker: Django project at [Habit_Tracker/habit_tracker](Habit_Tracker/habit_tracker). Entry: [`manage.py`](Habit_Tracker/habit_tracker/manage.py). App `track_it` code: views [`track_it/views.py`](Habit_Tracker/habit_tracker/track_it/views.py), models [`track_it/models.py`](Habit_Tracker/habit_tracker/track_it/models.py), forms [`track_it/forms.py`](Habit_Tracker/habit_tracker/track_it/forms.py), urls [`track_it/urls.py`](Habit_Tracker/habit_tracker/track_it/urls.py). Templates: [habit_tracker/templates/track_it/register.html](Habit_Tracker/habit_tracker/templates/track_it/register.html), [habit_tracker/templates/track_it/login.html](Habit_Tracker/habit_tracker/templates/track_it/login.html). Initial migration: [track_it/migrations/0001_initial.py](Habit_Tracker/habit_tracker/track_it/migrations/0001_initial.py). Settings: [habit_tracker/settings.py](Habit_Tracker/habit_tracker/habit_tracker/settings.py).

Quick start (per project)

## FastAPI backend
```sh
# from repository root
cd FastAPI/todo_list
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
# run backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
Backend main: [FastAPI/todo_list/main.py](FastAPI/todo_list/main.py). The app creates the SQLite tables on startup using database.py.
API routes live in: [`routes/tasks.py`](FastAPI/todo_list/routes/tasks.py).

## React frontend (for FastAPI)
```sh
cd FastAPI/todo-frontend
npm install
npm start
```
Frontend expects the backend at http://127.0.0.1:8000 (CORS configured in [FastAPI/todo_list/main.py](FastAPI/todo_list/main.py)).

## Flask To-Do
```sh
cd Flask/todo_app
python -m venv .venv
# activate venv
pip install -r requirements.txt
# set FLASK_APP and run
# Windows:
#   set FLASK_APP=app.py
#   flask run
# macOS/Linux:
#   export FLASK_APP=app.py
#   flask run
```

App entry: Flask/todo_app/app.py. Todos are persisted to Flask/todo_app/todos.json.

## Django Habit Tracker
```sh
cd Habit_Tracker/habit_tracker
python -m venv .venv
# activate venv
pip install django
# update DATABASES in settings if you don't have the configured Postgres
# run migrations and start dev server
python manage.py migrate
python manage.py runserver
```

Project settings: [habit_tracker/settings.py](Habit_Tracker/habit_tracker/habit_tracker/settings.py).

App views and models: [`track_it/views.py`](Habit_Tracker/habit_tracker/track_it/views.py), [`track_it/models.py`](Habit_Tracker/habit_tracker/track_it/models.py).

Notes
- Inspect route implementations before running: see FastAPI/todo_list/routes/tasks.py and FastAPI/URL_Shortner/main.py.
- Adjust database settings in the Django settings file if you do not have the provided PostgreSQL configuration: [habit_tracker/settings.py](Habit_Tracker/habit_tracker/habit_tracker/settings.py).
- The React frontend and FastAPI backend are configured to run on ports 3000 and 8000 respectively.