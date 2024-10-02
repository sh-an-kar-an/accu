import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.db import models
from django.db import transaction
from django.dispatch import Signal

# Configure Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Create a settings module
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

# Create the tables
from django.db import connection
connection.creation.create_all()

# Define the signal and receiver
my_signal = Signal()

def receiver(sender, **kwargs):
    print("Receiver started")
    # Simulate some database operation
    MyModel.objects.create(name="Test")
    print("Receiver finished")

my_signal.connect(receiver)

class MyModel(models.Model):
    name = models.CharField(max_length=255)

# Define the sender function
def sender_function():
    print("Sender started")
    with transaction.atomic():
        try:
            # Simulate some database operation
            MyModel.objects.create(name="Sender")
            my_signal.send(sender=None)
            print("Sender finished")
        except Exception as e:
            print(f"Exception caught: {e}")

# Run the sender function
sender_function()