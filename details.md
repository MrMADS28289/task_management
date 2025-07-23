✅ STEP 1: requirements.txt বানাও
bash
Copy
Edit
pip freeze > requirements.txt
✅ STEP 2: Procfile বানাও
📄 File name: Procfile (no extension)

bash
Copy
Edit
web: gunicorn your_project_name.wsgi
👉 your_project_name মানে যেই ফোল্ডারে settings.py, wsgi.py আছে (যেমন: mysite, tasknest, etc.)

✅ STEP 3: runtime.txt (optional)
txt
Copy
Edit
python-3.11.9
(তোমার Python version অনুযায়ী)

✅ STEP 4: settings.py আপডেট করো
🔹 DEBUG False + Allowed Hosts:
python
Copy
Edit
import os
DEBUG = False
ALLOWED_HOSTS = ['*'] # অথবা railway এর domain
🔹 Static Files:
python
Copy
Edit
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
🔹 PostgreSQL with Env Vars:
python
Copy
Edit
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': os.getenv('DB_NAME'),
'USER': os.getenv('DB_USER'),
'PASSWORD': os.getenv('DB_PASSWORD'),
'HOST': os.getenv('DB_HOST'),
'PORT': os.getenv('DB_PORT'),
}
}
