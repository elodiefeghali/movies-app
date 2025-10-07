# Movies App

This is a Django project called *Movies App*.  
It lets you manage a list of movies and related information.  

The code includes:
- `videostore/` → the main project files (settings, urls, etc.)
- `videos/` → the app where movies are created and displayed
- `manage.py` → used to run the project
- `requirements.txt` → the dependencies needed

## How to run
1. Create a virtual environment
2. Install requirements with: `pip install -r requirements.txt`
3. Run database migrations: `python manage.py migrate`
4. Start the app: `python manage.py runserver`
