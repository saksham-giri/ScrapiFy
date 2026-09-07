# Scrapify

Scrapify is a Django marketplace for buying and selling recyclable scrap. Sellers can create, edit and delete listings; buyers can browse available scrap and book a listing.

## Stack

- Python / Django
- Custom Django user model with buyer/seller roles
- PostgreSQL in production, SQLite for local development
- WhiteNoise for static files
- Gunicorn for production serving

## Local setup

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Render deployment

This repository includes `render.yaml` and `build.sh` for Render Blueprint deployment.

1. Push the repository to GitHub.
2. In Render, create a new Blueprint and select this repository.
3. Render reads `render.yaml`, creates the PostgreSQL database and web service, installs dependencies, runs migrations and collects static files.
4. Wait for the first deploy to finish, then open the generated `.onrender.com` URL.
5. Create a staff account if you need the Django admin: `python manage.py createsuperuser` is easiest to run from a local environment against a configured production database, or use Render's shell if available.

The production app reads `SECRET_KEY`, `DATABASE_URL`, `DEBUG`, and `RENDER_EXTERNAL_HOSTNAME` from the environment. Do not commit secrets or a production database to Git.
