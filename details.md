PS C:\Projects\Resume projects\Task Management\task-management> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 3 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): tasks, users.
Run 'python manage.py migrate' to apply them.
July 22, 2025 - 23:39:47
Django version 5.1.4, using settings 'task_management.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

PS C:\Projects\Resume projects\Task Management\task-management> python manage.py migrate
Traceback (most recent call last):
File "C:\Projects\Resume projects\Task Management\task-management\manage.py", line 22, in <module>
main()
~~~~^^
File "C:\Projects\Resume projects\Task Management\task-management\manage.py", line 18, in main
execute_from_command_line(sys.argv)
~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
File "C:\Users\abdus\AppData\Local\Programs\Python\Python313\Lib\site-packages\django\core\management\_\_init**.py", line 442, in execute_from_command_line
utility.execute()
~~~~~~~~~~~~~~~^^
File "C:\Users\abdus\AppData\Local\Programs\Python\Python313\Lib\site-packages\django\core\management\_\_init**.py", line 436, in execute
self.fetch_command(subcommand).run_from_argv(self.argv)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^
File "C:\Users\abdus\AppData\Local\Programs\Python\Python313\Lib\site-packages\django\core\management\base.py", line 413, in run_from_argv
self.execute(*args, \*\*cmd_options)
~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\abdus\AppData\Local\Programs\Python\Python313\Lib\site-packages\django\core\management\base.py", line 459, in execute
output = self.handle(*args, **options)
File "C:\Users\abdus\AppData\Local\Programs\Python\Python313\Lib\site-packages\django\core\management\base.py", line 107, in wrapper
res = handle_func(\*args, **kwargs)
File "C:\Users\abdus\AppData\Local\Programs\Python\Python313\Lib\site-packages\django\core\management\commands\migrate.py", line 121, in handle
executor.loader.check_consistent_history(connection)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
File "C:\Users\abdus\AppData\Local\Programs\Python\Python313\Lib\site-packages\django\db\migrations\loader.py", line 327, in check_consistent_history
raise InconsistentMigrationHistory(
...<8 lines>...
)
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'.
PS C:\Projects\Resume projects\Task Management\task-management> python manage.py migrate
