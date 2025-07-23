n run
WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]", prog=prog).run()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 235, in run
super().run()
~~~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 71, in run
Arbiter(self).run()
~~~~~~~^^^^^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 57, in **init**
self.setup(app)
~~~~~~~~~~^^^^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 117, in setup
self.app.wsgi()
~~~~~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 66, in wsgi
self.callable = self.load()
~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
return self.load_wsgiapp()
~~~~~~~~~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
return util.import_app(self.app_uri)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/util.py", line 370, in import_app
mod = importlib.import_module(module)
File "/usr/local/lib/python3.13/importlib/**init**.py", line 88, in import_module
return \_bootstrap.\_gcd_import(name[level:], package, level)
~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "<frozen importlib._bootstrap>", line 1387, in \_gcd_import
File "<frozen importlib._bootstrap>", line 1360, in \_find_and_load
File "<frozen importlib._bootstrap>", line 1331, in \_find_and_load_unlocked
File "<frozen importlib._bootstrap>", line 935, in \_load_unlocked
File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
File "<frozen importlib._bootstrap>", line 488, in \_call_with_frames_removed
File "/opt/render/project/src/tasknest/wsgi.py", line 16, in <module>
application = get_wsgi_application()
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/django/core/wsgi.py", line 12, in get_wsgi_application
django.setup(set_prefix=False)
~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/django/**init**.py", line 24, in setup
apps.populate(settings.INSTALLED_APPS)
~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/django/apps/registry.py", line 91, in populate
app_config = AppConfig.create(entry)
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/django/apps/config.py", line 193, in create
import_module(entry)
~~~~~~~~~~~~~^^^^^^^
File "/usr/local/lib/python3.13/importlib/**init**.py", line 88, in import_module
return \_bootstrap.\_gcd_import(name[level:], package, level)
~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "<frozen importlib._bootstrap>", line 1387, in \_gcd_import
File "<frozen importlib._bootstrap>", line 1360, in \_find_and_load
File "<frozen importlib._bootstrap>", line 1324, in \_find_and_load_unlocked
ModuleNotFoundError: No module named 'widget_tweaks'
==> Exited with status 1
==> Common ways to troubleshoot your deploy: https://render.com/docs/troubleshooting-deploys
==> Running 'gunicorn tasknest.wsgi'
Traceback (most recent call last):
File "/opt/render/project/src/.venv/bin/gunicorn", line 8, in <module>
sys.exit(run())
~~~^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 66, in run
WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]", prog=prog).run()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 235, in run
super().run()
~~~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 71, in run
Arbiter(self).run()
~~~~~~~^^^^^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 57, in **init**
self.setup(app)
~~~~~~~~~~^^^^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/arbiter.py", line 117, in setup
self.app.wsgi()
~~~~~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/base.py", line 66, in wsgi
self.callable = self.load()
~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
return self.load_wsgiapp()
~~~~~~~~~~~~~~~~~^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
return util.import_app(self.app_uri)
~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/gunicorn/util.py", line 370, in import_app
mod = importlib.import_module(module)
File "/usr/local/lib/python3.13/importlib/**init**.py", line 88, in import_module
return \_bootstrap.\_gcd_import(name[level:], package, level)
~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "<frozen importlib._bootstrap>", line 1387, in \_gcd_import
File "<frozen importlib._bootstrap>", line 1360, in \_find_and_load
File "<frozen importlib._bootstrap>", line 1331, in \_find_and_load_unlocked
File "<frozen importlib._bootstrap>", line 935, in \_load_unlocked
File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
File "<frozen importlib._bootstrap>", line 488, in \_call_with_frames_removed
File "/opt/render/project/src/tasknest/wsgi.py", line 16, in <module>
application = get_wsgi_application()
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/django/core/wsgi.py", line 12, in get_wsgi_application
django.setup(set_prefix=False)
~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/django/**init**.py", line 24, in setup
apps.populate(settings.INSTALLED_APPS)
~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/django/apps/registry.py", line 91, in populate
app_config = AppConfig.create(entry)
File "/opt/render/project/src/.venv/lib/python3.13/site-packages/django/apps/config.py", line 193, in create
import_module(entry)
~~~~~~~~~~~~~^^^^^^^
File "/usr/local/lib/python3.13/importlib/**init**.py", line 88, in import_module
return \_bootstrap.\_gcd_import(name[level:], package, level)
~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "<frozen importlib._bootstrap>", line 1387, in \_gcd_import
File "<frozen importlib._bootstrap>", line 1360, in \_find_and_load
File "<frozen importlib._bootstrap>", line 1324, in \_find_and_load_unlocked
ModuleNotFoundError: No module named 'widget_tweaks'
