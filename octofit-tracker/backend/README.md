# OctoFit Tracker — Backend (Local Run Instructions)

Quick instructions to run the Django backend locally for development.

## Prerequisites ✅
- Python 3.8+ installed and available on PATH (or the `py` launcher on Windows).
- The project venv at `octofit-tracker/backend/venv` (created in this repo).
- If you plan to use MongoDB (djongo): have a MongoDB server running on localhost:27017 or use Docker.

> Port notes: the dev server uses port **8000** by default and MongoDB uses **27017**. (Per project guidelines these ports are available.)

---

## Activate the venv

PowerShell (recommended):

```powershell
& .\octofit-tracker\backend\venv\Scripts\Activate.ps1
```

CMD:

```cmd
.\octofit-tracker\backend\venv\Scripts\activate.bat
```

Git Bash / WSL:

```bash
source octofit-tracker/backend/venv/Scripts/activate
```

## Install dependencies

(If you haven't already)

```bash
pip install -r octofit-tracker/backend/requirements.txt
```

## Database setup

This project supports `djongo` (MongoDB) via `pymongo` and `djongo`.

Option 1 — Use MongoDB (recommended if you need Mongo features):
- Start MongoDB (local service) or run via Docker:
  ```bash
  docker run -d -p 27017:27017 --name octofit-mongo mongo:6
  ```
- Ensure MongoDB is reachable at `localhost:27017`.

Option 2 — Use SQLite for quick local dev:
- Edit `octofit-tracker/backend/octofit_tracker/settings.py` and set `DATABASES` to SQLite if you prefer a lightweight dev DB:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## Run migrations

```bash
# from repo root (or adjust path)
python octofit-tracker/backend/manage.py makemigrations
python octofit-tracker/backend/manage.py migrate
```

## Create a superuser (optional)

```bash
python octofit-tracker/backend/manage.py createsuperuser
```

## Run the development server

```bash
# Bind to all interfaces (useful in Codespaces or Docker)
python octofit-tracker/backend/manage.py runserver 0.0.0.0:8000

# Or local-only
python octofit-tracker/backend/manage.py runserver
```

Then open: http://localhost:8000/ or (for the API) http://localhost:8000/api/

## Quick API test (curl)

```bash
curl http://localhost:8000/api/
```

(Or in PowerShell)

```powershell
Invoke-RestMethod http://localhost:8000/api/
```

## Deactivate venv

```bash
deactivate
```

---

## Notes & Tips 💡
- If `makemigrations` fails due to a MongoDB connection error, either start MongoDB or temporarily switch to SQLite as shown above to create migrations, then switch back to `djongo`.
- If you want, I can add a small `make` or `ps1` script to automate activation, migrate, and runserver.

---

If you'd like, I can also add a short section for running backend tests and an example `curl` request that creates an activity.
