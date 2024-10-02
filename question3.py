# Django signals are executed within the same database transaction as the caller. 
# When a signal is sent, the connected receivers are executed within the same database transaction that sent the signal.
# This means that if the signal handling code performs any database operations, 
# they will be part of the same transaction as the code that sent the signal.




import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.db import models
from django.db import transaction
from django.dispatch import Signal


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')


settings.configure(
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test.db',
        }
    }
)


from django.db import connection
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mymodel (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255)
    )
''')


my_signal = Signal()

def receiver(sender, **kwargs):
    print("Receiver started")
    
    cursor.execute('INSERT INTO mymodel (name) VALUES (%s)', ['Test'])
    print("Receiver finished")

my_signal.connect(receiver)


def sender_function():
    print("Sender started")
    with transaction.atomic():
        try:
            
            cursor.execute('INSERT INTO mymodel (name) VALUES (%s)', ['Sender'])
            my_signal.send(sender=None)
            print("Sender finished")
        except Exception as e:
            print(f"Exception caught: {e}")


sender_function()
