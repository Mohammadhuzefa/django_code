from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact = models.CharField(max_length=15,blank=True, null=True)
    tel=models.IntegerField(null=True,blank=True)
    quali=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    img=models.ImageField()
    Document=models.FileField()
    extra=models.CharField(max_length=20,null=True)
    # audio=models.FileField()
    # video=models.FileField()

    # without str method()
    # <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>, <Student: Student 
    # with str
    # 098@gmail.com 57>, <Student:   diyyaa098@gmail.com 57>, <Student: DIYA NA diyyaa098@gmail.com 57>, <Student: jatin diyyaa098@gmail.com 96>]>
    # def __str__(self):
    #     return self.name +" "+self.email+" "+str(self.contact)
    

# same as all

# termainal


#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\models\base.py", line 966, in save_base
#     updated = self._save_table(
#         raw,
#     ...<4 lines>...
#         update_fields,
#     )
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\models\base.py", line 1167, in _save_table
#     results = self._do_insert(
#         cls._base_manager, using, insert_fields, returning_fields, raw
#     )
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\models\base.py", line 1218, in _do_insert
#     return manager._insert(
#            ~~~~~~~~~~~~~~~^
#         [self],
#         ^^^^^^^
#     ...<3 lines>...
#         raw=raw,
#         ^^^^^^^^
#     )
#     ^
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\models\query.py", line 1918, in _insert
#     return query.get_compiler(using=using).execute_sql(returning_fields)
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\models\sql\compiler.py", line 1925, in execute_sql
#     cursor.execute(sql, params)
#     ~~~~~~~~~~~~~~^^^^^^^^^^^^^
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\backends\utils.py", line 122, in execute
#     return super().execute(sql, params)
#            ~~~~~~~~~~~~~~~^^^^^^^^^^^^^
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\backends\utils.py", line 79, in execute
#     return self._execute_with_wrappers(
#            ~~~~~~~~~~~~~~~~~~~~~~~~~~~^
#         sql, params, many=False, executor=self._execute
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\backends\utils.py", line 92, in _execute_with_wrappers
#     return executor(sql, params, many, context)
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\backends\utils.py", line 100, in _execute
#     with self.db.wrap_database_errors:
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\utils.py", line 94, in __exit__
#     raise dj_exc_value.with_traceback(traceback) from exc_value
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
#     return self.cursor.execute(sql, params)
#            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\db\backends\mysql\base.py", line 78, in execute
#     return self.cursor.execute(query, args)
#            ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\MySQLdb\cursors.py", line 179, in execute
#     res = self._query(mogrified_query)
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\MySQLdb\cursors.py", line 330, in _query
#     db.query(q)
#     ~~~~~~~~^^^
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\MySQLdb\connections.py", line 280, in query
#     _mysql.connection.query(self, query)
#     ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
# django.db.utils.IntegrityError: (1048, "Column 'gender' cannot be null")
# [13/Jan/2026 21:41:03] "POST /data HTTP/1.1" 500 191620
# jatin,diyyaa098@gmail.com,96,65,['10'],,male
# None
# <class 'str'> <class 'str'> <class 'str'> <class 'str'> <class 'list'> <class 'str'> <class 'str'> <class 'NoneType'>     
# Internal Server Error: /data
# Traceback (most recent call last):
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
#     response = get_response(request)
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\core\handlers\base.py", line 205, in _get_response
#     self.check_response(response, callback)
#     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Lib\site-packages\django\core\handlers\base.py", line 333, in check_response
#     raise ValueError(
#     ...<2 lines>...
#     )
# ValueError: The view myapp.views.data didn't return an HttpResponse object. It returned None instead.
# [13/Jan/2026 21:41:13] "POST /data HTTP/1.1" 500 71505

#  *  History restored 

# PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform> cd .\env\     
# PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env> cd .\Scripts\
# PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Scripts> ./activate
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Scripts> cd ..
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env> cd ..
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform> cd .\myprject\
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python manage.py runserver
# Watching for file changes with StatReloader
# Performing system checks...

# System check identified no issues (0 silenced).
# January 15, 2026 - 10:43:10
# Django version 6.0.1, using settings 'myprject.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.

# WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
# For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python mange.py shell
# C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Scripts\python.exe: can't open file 'C:\\Users\\DELL\\OneDrive\\Desktop\\djangoprogit\\12 form\\registrationform\\myprject\\mange.py': [Errno 2] No such file or directory 
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python manage.py shell
# 13 objects imported automatically (use -v 2 for details).

# Ctrl click to launch VS Code Native REPL
# Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from myapp import Student
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# ImportError: cannot import name 'Student' from 'myapp' (C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject\myapp\__init__.py)
# >>> from myapp.models import Student
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.

# WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
# For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python mange.py shell
# C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Scripts\python.exe: can't open file 'C:\\Users\\DELL\\OneDrive\\Desktop\\djangoprogit\\12 form\\registrationform\\myprject\\mange.py': [Errno 2] No such file or directory 
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python manage.py shell
# 13 objects imported automatically (use -v 2 for details).

# Ctrl click to launch VS Code Native REPL
# Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from myapp import Student as s
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# ImportError: cannot import name 'Student' from 'myapp' (C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject\myapp\__init__.py)
# >>> from myapp.models import Student
# data=me bhi ho skta he Student.objects.all()
# <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>, <Student: Student object (4)>, <Student: Student object (5)>, <Student: Student object (6)>]>
# >>>
# C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Scripts\python.exe: can't open file 'C:\\Users\\DELL\\OneDrive\\Desktop\\djangoprogit\\12 form\\registrationform\\myprject\\mange.py': [Errno 2] No such file or directory 
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python manage.py shell
# 13 objects imported automatically (use -v 2 for details).

# Ctrl click to launch VS Code Native REPL
# Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from myapp import Student
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# ImportError: cannot import name 'Student' from 'myapp' (C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject\myapp\__init__.py)
# >>> from myapp.models import Student
# >>> from myapp import Student
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# ImportError: cannot import name 'Student' from 'myapp' (C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject\myapp\__init__.py)
# >>> from myapp.models import Student
# rm\myprject\myapp\__init__.py)
# >>> from myapp.models import Student
# >>> Student.objects.all()
# <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>, <Student: Student object (4)>, <Student: Student object (5)>, <Student: Student object (6)>]>
# >>>








# >>> Student.objects.all()
# <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>, <Student: Student object (4)>, <Student: Student object (5)>, <Student: Student object (6)>]>
# >>> Student.objects.all()
# <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>, <Student: Student >>> Student.objects.all()
# >>> Student.objects.all()
# <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>, <Student: Student object (3)>, <Student: Student object (4)>, <Student: Student object (5)>, <Student: Student object (6)>]>
# >>> exit(
# ... exit()
# ... exit()
#   File "<console>", line 1
#     exit(
#         ^
# SyntaxError: '(' was never closed
# >>> Exit()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'Exit' is not defined. Did you mean: 'exit'?
# >>> exit()
# now exiting InteractiveConsole...
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python mange.py shell 
# C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Scripts\python.exe: can't open file 'C:\\Users\\DELL\\OneDrive\\Desktop\\djangoprogit\\12 form\\registrationform\\myprject\\mange.py': [Errno 2] No such file or directory 
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python manage.py shell
# 13 objects imported automatically (use -v 2 for details).

# Ctrl click to launch VS Code Native REPL
# Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from myapp.models import Student
# >>> Student.objects.all()
# <QuerySet [<Student: DIYA NA>, <Student: DIYA NA>, <Student: DIYA NA>, <Student:  >, <Student: DIYA NA>, <Student: jatin>]>
# >>> exit()               
# now exiting InteractiveConsole...
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python mange.py shell 
# C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Scripts\python.exe: can't open file 'C:\\Users\\DELL\\OneDrive\\Desktop\\djangoprogit\\12 form\\registrationform\\myprject\\mange.py': [Errno 2] No such file or directory
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python manage.py shell
# 13 objects imported automatically (use -v 2 for details).

# Ctrl click to launch VS Code Native REPL
# Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> Student.objects.all()
# <QuerySet [<Student: DIYA NA>, <Student: DIYA NA>, <Student: DIYA NA>, <Student:  >, <Student: DIYA NA>, <Student: jatin>]>
# >>> exit()
# now exiting InteractiveConsole...
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python mange.py shell
# C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\env\Scripts\python.exe: can't open file 'C:\\Users\\DELL\\OneDrive\\Desktop\\djangoprogit\\12 form\\registrationform\\myprject\\mange.py': [Errno 2] No such file or directory 
# (env) PS C:\Users\DELL\OneDrive\Desktop\djangoprogit\12 form\registrationform\myprject> python manage.py shell
# 13 objects imported automatically (use -v 2 for details).

# Ctrl click to launch VS Code Native REPL
# Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> Student.objects.all()
# Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> Student.objects.all()
# >>> Student.objects.all()
# <QuerySet [<Student: DIYA NA diyyaa098@gmail.com 565>, <Student: DIYA NA diyyaa098@gmail.com 57>, <Student: DIYA NA diyyaa098@gmail.com 57>, <Student:   diyyaa098@gmail.com 57>, <Student: DIYA NA diyyaa098@gmail.com 57>, <Student: jatin diyyaa098@gmail.com 96>]>
# >>>