TemplateSyntaxError at /users/admin/dashboard/
Unclosed tag on line 4: 'block'. Looking for one of: endblock.
Request Method: GET
Request URL: http://127.0.0.1:8000/users/admin/dashboard/
Django Version: 5.2.4
Exception Type: TemplateSyntaxError
Exception Value:
Unclosed tag on line 4: 'block'. Looking for one of: endblock.
Exception Location: C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\base.py, line 590, in unclosed_block_tag
Raised during: users.views.admin_dashboard
Python Executable: C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\scripts\python.exe
Python Version: 3.13.5
Python Path:
['C:\\Projects\\Resume projects\\Task Management - 22.07.2025\\task-management',
'C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip',
'C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313\\DLLs',
'C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313\\Lib',
'C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313',
'C:\\Projects\\Resume projects\\Task Management - '
'22.07.2025\\task-management\\task_env',
'C:\\Projects\\Resume projects\\Task Management - '
'22.07.2025\\task-management\\task_env\\Lib\\site-packages']
Server time: Wed, 23 Jul 2025 18:35:45 +0600
Error during template rendering
In template C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\users\templates\admin\dashboard.html, error at line 4

Unclosed tag on line 4: 'block'. Looking for one of: endblock.
1 {% extends "base.html" %}
2 {% load static %}
3 {% block title %}Admin Dashboard{% endblock title %}
4 {% block content %}
5 <header class="bg-surface dark:bg-surface-dark shadow-md">
6 <nav class="container mx-auto px-6 py-3">
7 <div class="flex justify-between items-center">
8 <a href="{% url 'home' %}" class="text-xl font-bold text-text-primary dark:text-text-primary-dark flex items-center">
9 <svg width="120" height="30" viewBox="0 0 120 30" fill="none" xmlns="http://www.w3.org/2000/svg">
10 <rect width="120" height="30" fill="#F0F4F8"/>
11 <text x="5" y="22" font-family="Arial, sans-serif" font-size="20" font-weight="bold">
12 <tspan fill="#4299E1">Task</tspan><tspan fill="#667EEA">Nest</tspan>
13 </text>
14 <circle cx="105" cy="15" r="8" fill="#F6AD55"/>
Traceback Switch to copy-and-paste view
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\core\handlers\exception.py, line 55, in inner
response = get_response(request)
^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\core\handlers\base.py, line 197, in \_get_response
response = wrapped_callback(request, *callback_args, \*\*callback_kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\contrib\auth\decorators.py, line 59, in \_view_wrapper
return view_func(request, *args, \*\*kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\users\views.py, line 143, in admin_dashboard
return render(request, 'admin/dashboard.html', {"users": users})
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\shortcuts.py, line 25, in render
content = loader.render_to_string(template_name, context, request, using=using)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\loader.py, line 61, in render_to_string
template = get_template(template_name, using=using)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\loader.py, line 15, in get_template
return engine.get_template(template_name)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\backends\django.py, line 79, in get_template
return Template(self.engine.get_template(template_name), self)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\engine.py, line 177, in get_template
template, origin = self.find_template(template_name)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\engine.py, line 159, in find_template
template = loader.get_template(name, skip=skip)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\loaders\cached.py, line 57, in get_template
template = super().get_template(template_name, skip)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\loaders\base.py, line 28, in get_template
return Template(
…
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\base.py, line 154, in **init**
self.nodelist = self.compile_nodelist()
^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\base.py, line 196, in compile_nodelist
nodelist = parser.parse()
^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\base.py, line 518, in parse
raise self.error(token, e)
^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\base.py, line 516, in parse
compiled_result = compile_func(self, token)
^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\loader_tags.py, line 299, in do_extends
nodelist = parser.parse()
^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\base.py, line 518, in parse
raise self.error(token, e)
^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\base.py, line 516, in parse
compiled_result = compile_func(self, token)
^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\loader_tags.py, line 234, in do_block
nodelist = parser.parse(("endblock",))
^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\base.py, line 523, in parse
self.unclosed_block_tag(parse_until)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
C:\Projects\Resume projects\Task Management - 22.07.2025\task-management\task_env\Lib\site-packages\django\template\base.py, line 590, in unclosed_block_tag
raise self.error(token, msg)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
Local vars
Request information
USER
mads

GET
No GET data

POST
No POST data

FILES
No FILES data

COOKIES
Variable Value
csrftoken
'********\*\*\*\*********'
sessionid
'********\*\*\*\*********'
META
Variable Value
ALLUSERSPROFILE
'C:\\ProgramData'
APPDATA
'C:\\Users\\abdus\\AppData\\Roaming'
COMMONPROGRAMFILES
'C:\\Program Files\\Common Files'
COMMONPROGRAMFILES(X86)
'C:\\Program Files (x86)\\Common Files'
COMMONPROGRAMW6432
'C:\\Program Files\\Common Files'
COMPUTERNAME
'DESKTOP-9RBRKN6'
COMSPEC
'C:\\WINDOWS\\system32\\cmd.exe'
CONTENT_LENGTH
''
CONTENT_TYPE
'text/plain'
CSRF_COOKIE
'4OJbeoRcKYDQZqa774mpAfJ9UGIvhylV'
DJANGO_SETTINGS_MODULE
'task_management.settings'
DRIVERDATA
'C:\\Windows\\System32\\Drivers\\DriverData'
GATEWAY_INTERFACE
'CGI/1.1'
HOME
'C:\\Users\\abdus'
HOMEDRIVE
'C:'
HOMEPATH
'\\Users\\abdus'
HTTP_ACCEPT
'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,_/_;q=0.8,application/signed-exchange;v=b3;q=0.7'
HTTP_ACCEPT_ENCODING
'gzip, deflate, br, zstd'
HTTP_ACCEPT_LANGUAGE
'en-US,en;q=0.9'
HTTP_CONNECTION
'keep-alive'
HTTP_COOKIE
'********\*\*\*\*********'
HTTP_DNT
'1'
HTTP_HOST
'127.0.0.1:8000'
HTTP_REFERER
'http://127.0.0.1:8000/tasks/manager-dashboard/'
HTTP_SEC_CH_UA
'"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"'
HTTP_SEC_CH_UA_MOBILE
'?0'
HTTP_SEC_CH_UA_PLATFORM
'"Windows"'
HTTP_SEC_FETCH_DEST
'document'
HTTP_SEC_FETCH_MODE
'navigate'
HTTP_SEC_FETCH_SITE
'same-origin'
HTTP_SEC_FETCH_USER
'?1'
HTTP_UPGRADE_INSECURE_REQUESTS
'1'
HTTP_USER_AGENT
('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like '
'Gecko) Chrome/138.0.0.0 Safari/537.36')
LOCALAPPDATA
'C:\\Users\\abdus\\AppData\\Local'
LOGONSERVER
'\\\\DESKTOP-9RBRKN6'
NUMBER_OF_PROCESSORS
'12'
ONEDRIVE
'C:\\Users\\abdus\\OneDrive'
ONEDRIVECONSUMER
'C:\\Users\\abdus\\OneDrive'
OS
'Windows_NT'
PATH
('C:\\Projects\\Resume projects\\Task Management - '
'22.07.2025\\task-management\\task_env\\scripts;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program '
'Files\\Git\\cmd;C:\\Users\\abdus\\AppData\\Local\\Android\\Sdk\\platforms;C:\\Users\\abdus\\AppData\\Local\\Android\\Sdk\\platform-tools;C:\\Program '
'Files\\MySQL\\MySQL Server '
'8.0\\bin;C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;C:\\Program '
'Files\\nodejs\\;C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\;C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313\\;C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Launcher\\;C:\\Program '
'Files\\MySQL\\MySQL Shell '
'8.0\\bin\\;C:\\Users\\abdus\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Program '
'Files\\Git\\bin;C:\\MinGW\\bin;C:\\Users\\abdus\\AppData\\Local\\Programs\\Microsoft '
'VS '
'Code\\bin;C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;C:\\Users\\abdus\\AppData\\Roaming\\npm')
PATHEXT
'.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL'
PATH_INFO
'/users/admin/dashboard/'
PROCESSOR_ARCHITECTURE
'AMD64'
PROCESSOR_IDENTIFIER
'AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD'
PROCESSOR_LEVEL
'25'
PROCESSOR_REVISION
'5000'
PROGRAMDATA
'C:\\ProgramData'
PROGRAMFILES
'C:\\Program Files'
PROGRAMFILES(X86)
'C:\\Program Files (x86)'
PROGRAMW6432
'C:\\Program Files'
PSMODULEPATH
('C:\\Users\\abdus\\OneDrive\\Documents\\WindowsPowerShell\\Modules;C:\\Program '
'Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules')
PUBLIC
'C:\\Users\\Public'
QUERY_STRING
''
REMOTE_ADDR
'127.0.0.1'
REMOTE_HOST
''
REQUEST_METHOD
'GET'
RUN_MAIN
'true'
SCRIPT_NAME
''
SERVER_NAME
'DESKTOP-9RBRKN6'
SERVER_PORT
'8000'
SERVER_PROTOCOL
'HTTP/1.1'
SERVER_SOFTWARE
'WSGIServer/0.2'
SESSIONNAME
'Console'
SYSTEMDRIVE
'C:'
SYSTEMROOT
'C:\\WINDOWS'
TEMP
'C:\\Users\\abdus\\AppData\\Local\\Temp'
TMP
'C:\\Users\\abdus\\AppData\\Local\\Temp'
USERDOMAIN
'DESKTOP-9RBRKN6'
USERDOMAIN_ROAMINGPROFILE
'DESKTOP-9RBRKN6'
USERNAME
'abdus'
USERPROFILE
'C:\\Users\\abdus'
VBOX_HWVIRTEX_IGNORE_SVM_IN_USE
'1'
VIRTUAL_ENV
('C:\\Projects\\Resume projects\\Task Management - '
'22.07.2025\\task-management\\task_env')
VIRTUAL_ENV_PROMPT
'task_env'
WINDIR
'C:\\WINDOWS'
WSLENV
'WT_SESSION:WT_PROFILE_ID:'
WT_PROFILE_ID
'{61c54bbd-c2c6-5271-96e7-009a87ff44bf}'
WT_SESSION
'6a6bc2c4-dda7-450f-85ac-e2eda651ba74'
\_OLD_VIRTUAL_PATH
('C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program '
'Files\\Git\\cmd;C:\\Users\\abdus\\AppData\\Local\\Android\\Sdk\\platforms;C:\\Users\\abdus\\AppData\\Local\\Android\\Sdk\\platform-tools;C:\\Program '
'Files\\MySQL\\MySQL Server '
'8.0\\bin;C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;C:\\Program '
'Files\\nodejs\\;C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\;C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313\\;C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Launcher\\;C:\\Program '
'Files\\MySQL\\MySQL Shell '
'8.0\\bin\\;C:\\Users\\abdus\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Program '
'Files\\Git\\bin;C:\\MinGW\\bin;C:\\Users\\abdus\\AppData\\Local\\Programs\\Microsoft '
'VS '
'Code\\bin;C:\\Users\\abdus\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;C:\\Users\\abdus\\AppData\\Roaming\\npm')
\_\_PSLOCKDOWNPOLICY
'0'
wsgi.errors
<\_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
wsgi.file_wrapper
<class 'wsgiref.util.FileWrapper'>
wsgi.input
<django.core.handlers.wsgi.LimitedStream object at 0x000001CD29B69750>
wsgi.multiprocess
False
wsgi.multithread
True
wsgi.run_once
False
wsgi.url_scheme
'http'
wsgi.version
(1, 0)
Settings
Using settings module task_management.settings
Setting Value
ABSOLUTE_URL_OVERRIDES
{}
ADMINS
[]
ALLOWED_HOSTS
[]
APPEND_SLASH
True
AUTHENTICATION_BACKENDS
'********\*\*\*\*********'
AUTH_PASSWORD_VALIDATORS
'********\*\*\*\*********'
AUTH_USER_MODEL
'********\*\*\*\*********'
BASE_DIR
WindowsPath('C:/Projects/Resume projects/Task Management - 22.07.2025/task-management')
CACHES
{'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}
CACHE_MIDDLEWARE_ALIAS
'default'
CACHE_MIDDLEWARE_KEY_PREFIX
'********\*\*\*\*********'
CACHE_MIDDLEWARE_SECONDS
600
CSRF_COOKIE_AGE
31449600
CSRF_COOKIE_DOMAIN
None
CSRF_COOKIE_HTTPONLY
False
CSRF_COOKIE_NAME
'csrftoken'
CSRF_COOKIE_PATH
'/'
CSRF_COOKIE_SAMESITE
'Lax'
CSRF_COOKIE_SECURE
False
CSRF_FAILURE_VIEW
'django.views.csrf.csrf_failure'
CSRF_HEADER_NAME
'HTTP_X_CSRFTOKEN'
CSRF_TRUSTED_ORIGINS
[]
CSRF_USE_SESSIONS
False
DATABASES
{'default': {'ATOMIC_REQUESTS': False,
'AUTOCOMMIT': True,
'CONN_HEALTH_CHECKS': False,
'CONN_MAX_AGE': 0,
'ENGINE': 'django.db.backends.postgresql',
'HOST': 'localhost',
'NAME': 'task_management',
'OPTIONS': {},
'PASSWORD': '********\*\*\*\*********',
'PORT': '5432',
'TEST': {'CHARSET': None,
'COLLATION': None,
'MIGRATE': True,
'MIRROR': None,
'NAME': None},
'TIME_ZONE': None,
'USER': 'postgres'}}
DATABASE_ROUTERS
[]
DATA_UPLOAD_MAX_MEMORY_SIZE
2621440
DATA_UPLOAD_MAX_NUMBER_FIELDS
1000
DATA_UPLOAD_MAX_NUMBER_FILES
100
DATETIME_FORMAT
'N j, Y, P'
DATETIME_INPUT_FORMATS
['%Y-%m-%d %H:%M:%S',
'%Y-%m-%d %H:%M:%S.%f',
'%Y-%m-%d %H:%M',
'%m/%d/%Y %H:%M:%S',
'%m/%d/%Y %H:%M:%S.%f',
'%m/%d/%Y %H:%M',
'%m/%d/%y %H:%M:%S',
'%m/%d/%y %H:%M:%S.%f',
'%m/%d/%y %H:%M']
DATE_FORMAT
'N j, Y'
DATE_INPUT_FORMATS
['%Y-%m-%d',
'%m/%d/%Y',
'%m/%d/%y',
'%b %d %Y',
'%b %d, %Y',
'%d %b %Y',
'%d %b, %Y',
'%B %d %Y',
'%B %d, %Y',
'%d %B %Y',
'%d %B, %Y']
DEBUG
True
DEBUG_PROPAGATE_EXCEPTIONS
False
DECIMAL_SEPARATOR
'.'
DEFAULT_AUTO_FIELD
'django.db.models.BigAutoField'
DEFAULT_CHARSET
'utf-8'
DEFAULT_EXCEPTION_REPORTER
'django.views.debug.ExceptionReporter'
DEFAULT_EXCEPTION_REPORTER_FILTER
'django.views.debug.SafeExceptionReporterFilter'
DEFAULT_FROM_EMAIL
'webmaster@localhost'
DEFAULT_INDEX_TABLESPACE
''
DEFAULT_TABLESPACE
''
DISALLOWED_USER_AGENTS
[]
EMAIL_BACKEND
'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST
'smtp.gmail.com'
EMAIL_HOST_PASSWORD
'********\*\*\*\*********'
EMAIL_HOST_USER
'abduss.sobhan28@gmail.com'
EMAIL_PORT
'587'
EMAIL_SSL_CERTFILE
None
EMAIL_SSL_KEYFILE
'********\*\*\*\*********'
EMAIL_SUBJECT_PREFIX
'[Django] '
EMAIL_TIMEOUT
None
EMAIL_USE_LOCALTIME
False
EMAIL_USE_SSL
False
EMAIL_USE_TLS
True
FILE_UPLOAD_DIRECTORY_PERMISSIONS
None
FILE_UPLOAD_HANDLERS
['django.core.files.uploadhandler.MemoryFileUploadHandler',
'django.core.files.uploadhandler.TemporaryFileUploadHandler']
FILE_UPLOAD_MAX_MEMORY_SIZE
2621440
FILE_UPLOAD_PERMISSIONS
420
FILE_UPLOAD_TEMP_DIR
None
FIRST_DAY_OF_WEEK
0
FIXTURE_DIRS
[]
FORCE_SCRIPT_NAME
None
FORMAT_MODULE_PATH
None
FORMS_URLFIELD_ASSUME_HTTPS
False
FORM_RENDERER
'django.forms.renderers.DjangoTemplates'
FRONTEND_URL
'http://127.0.0.1:8000'
IGNORABLE_404_URLS
[]
INSTALLED_APPS
['django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'tasks',
'users',
'debug_toolbar',
'core']
INTERNAL_IPS
['127.0.0.1']
LANGUAGES
[('af', 'Afrikaans'),
('ar', 'Arabic'),
('ar-dz', 'Algerian Arabic'),
('ast', 'Asturian'),
('az', 'Azerbaijani'),
('bg', 'Bulgarian'),
('be', 'Belarusian'),
('bn', 'Bengali'),
('br', 'Breton'),
('bs', 'Bosnian'),
('ca', 'Catalan'),
('ckb', 'Central Kurdish (Sorani)'),
('cs', 'Czech'),
('cy', 'Welsh'),
('da', 'Danish'),
('de', 'German'),
('dsb', 'Lower Sorbian'),
('el', 'Greek'),
('en', 'English'),
('en-au', 'Australian English'),
('en-gb', 'British English'),
('eo', 'Esperanto'),
('es', 'Spanish'),
('es-ar', 'Argentinian Spanish'),
('es-co', 'Colombian Spanish'),
('es-mx', 'Mexican Spanish'),
('es-ni', 'Nicaraguan Spanish'),
('es-ve', 'Venezuelan Spanish'),
('et', 'Estonian'),
('eu', 'Basque'),
('fa', 'Persian'),
('fi', 'Finnish'),
('fr', 'French'),
('fy', 'Frisian'),
('ga', 'Irish'),
('gd', 'Scottish Gaelic'),
('gl', 'Galician'),
('he', 'Hebrew'),
('hi', 'Hindi'),
('hr', 'Croatian'),
('hsb', 'Upper Sorbian'),
('hu', 'Hungarian'),
('hy', 'Armenian'),
('ia', 'Interlingua'),
('id', 'Indonesian'),
('ig', 'Igbo'),
('io', 'Ido'),
('is', 'Icelandic'),
('it', 'Italian'),
('ja', 'Japanese'),
('ka', 'Georgian'),
('kab', 'Kabyle'),
('kk', 'Kazakh'),
('km', 'Khmer'),
('kn', 'Kannada'),
('ko', 'Korean'),
('ky', 'Kyrgyz'),
('lb', 'Luxembourgish'),
('lt', 'Lithuanian'),
('lv', 'Latvian'),
('mk', 'Macedonian'),
('ml', 'Malayalam'),
('mn', 'Mongolian'),
('mr', 'Marathi'),
('ms', 'Malay'),
('my', 'Burmese'),
('nb', 'Norwegian Bokmål'),
('ne', 'Nepali'),
('nl', 'Dutch'),
('nn', 'Norwegian Nynorsk'),
('os', 'Ossetic'),
('pa', 'Punjabi'),
('pl', 'Polish'),
('pt', 'Portuguese'),
('pt-br', 'Brazilian Portuguese'),
('ro', 'Romanian'),
('ru', 'Russian'),
('sk', 'Slovak'),
('sl', 'Slovenian'),
('sq', 'Albanian'),
('sr', 'Serbian'),
('sr-latn', 'Serbian Latin'),
('sv', 'Swedish'),
('sw', 'Swahili'),
('ta', 'Tamil'),
('te', 'Telugu'),
('tg', 'Tajik'),
('th', 'Thai'),
('tk', 'Turkmen'),
('tr', 'Turkish'),
('tt', 'Tatar'),
('udm', 'Udmurt'),
('ug', 'Uyghur'),
('uk', 'Ukrainian'),
('ur', 'Urdu'),
('uz', 'Uzbek'),
('vi', 'Vietnamese'),
('zh-hans', 'Simplified Chinese'),
('zh-hant', 'Traditional Chinese')]
LANGUAGES_BIDI
['he', 'ar', 'ar-dz', 'ckb', 'fa', 'ug', 'ur']
LANGUAGE_CODE
'en-us'
LANGUAGE_COOKIE_AGE
None
LANGUAGE_COOKIE_DOMAIN
None
LANGUAGE_COOKIE_HTTPONLY
False
LANGUAGE_COOKIE_NAME
'django_language'
LANGUAGE_COOKIE_PATH
'/'
LANGUAGE_COOKIE_SAMESITE
None
LANGUAGE_COOKIE_SECURE
False
LOCALE_PATHS
[]
LOGGING
{}
LOGGING_CONFIG
'logging.config.dictConfig'
LOGIN_REDIRECT_URL
'/tasks/dashboard/'
LOGIN_URL
'/users/sign-in/'
LOGOUT_REDIRECT_URL
'/'
MANAGERS
[]
MEDIA_ROOT
WindowsPath('C:/Projects/Resume projects/Task Management - 22.07.2025/task-management/media')
MEDIA_URL
'/media/'
MESSAGE_STORAGE
'django.contrib.messages.storage.fallback.FallbackStorage'
MIDDLEWARE
['debug_toolbar.middleware.DebugToolbarMiddleware',
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware']
MIGRATION_MODULES
{}
MONTH_DAY_FORMAT
'F j'
NUMBER_GROUPING
0
PASSWORD_HASHERS
'********\*\*\*\*********'
PASSWORD_RESET_TIMEOUT
'********\*\*\*\*********'
PREPEND_WWW
False
ROOT_URLCONF
'task_management.urls'
SECRET_KEY
'********\*\*\*\*********'
SECRET_KEY_FALLBACKS
'********\*\*\*\*********'
SECURE_CONTENT_TYPE_NOSNIFF
True
SECURE_CROSS_ORIGIN_OPENER_POLICY
'same-origin'
SECURE_HSTS_INCLUDE_SUBDOMAINS
False
SECURE_HSTS_PRELOAD
False
SECURE_HSTS_SECONDS
0
SECURE_PROXY_SSL_HEADER
None
SECURE_REDIRECT_EXEMPT
[]
SECURE_REFERRER_POLICY
'same-origin'
SECURE_SSL_HOST
None
SECURE_SSL_REDIRECT
False
SERVER_EMAIL
'root@localhost'
SESSION_CACHE_ALIAS
'default'
SESSION_COOKIE_AGE
1209600
SESSION_COOKIE_DOMAIN
None
SESSION_COOKIE_HTTPONLY
True
SESSION_COOKIE_NAME
'sessionid'
SESSION_COOKIE_PATH
'/'
SESSION_COOKIE_SAMESITE
'Lax'
SESSION_COOKIE_SECURE
False
SESSION_ENGINE
'django.contrib.sessions.backends.db'
SESSION_EXPIRE_AT_BROWSER_CLOSE
False
SESSION_FILE_PATH
None
SESSION_SAVE_EVERY_REQUEST
False
SESSION_SERIALIZER
'django.contrib.sessions.serializers.JSONSerializer'
SETTINGS_MODULE
'task_management.settings'
SHORT_DATETIME_FORMAT
'm/d/Y P'
SHORT_DATE_FORMAT
'm/d/Y'
SIGNING_BACKEND
'django.core.signing.TimestampSigner'
SILENCED_SYSTEM_CHECKS
[]
STATICFILES_DIRS
[WindowsPath('C:/Projects/Resume projects/Task Management - 22.07.2025/task-management/static')]
STATICFILES_FINDERS
['django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder']
STATIC_ROOT
None
STATIC_URL
'/static/'
STORAGES
{'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'}}
TEMPLATES
[{'APP_DIRS': True,
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [],
'OPTIONS': {'context_processors': ['django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages']}}]
TEST_NON_SERIALIZED_APPS
[]
TEST_RUNNER
'django.test.runner.DiscoverRunner'
THOUSAND_SEPARATOR
','
TIME_FORMAT
'P'
TIME_INPUT_FORMATS
['%H:%M:%S', '%H:%M:%S.%f', '%H:%M']
TIME_ZONE
'Asia/Dhaka'
USE_I18N
True
USE_THOUSAND_SEPARATOR
False
USE_TZ
True
USE_X_FORWARDED_HOST
False
USE_X_FORWARDED_PORT
False
WSGI_APPLICATION
'task_management.wsgi.application'
X_FRAME_OPTIONS
'DENY'
YEAR_MONTH_FORMAT
'F Y'
You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard page generated by the handler for this status code.
