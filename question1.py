import time
from django.dispatch import Signal

my_signal = Signal()

def receiver(sender, **kwargs):
    print("Receiver started")
    time.sleep(5)  # Simulate some long-running task
    print("Receiver finished")

my_signal.connect(receiver)

def sender_function():
    print("Sender started")
    my_signal.send(sender=None)
    print("Sender finished")

sender_function()