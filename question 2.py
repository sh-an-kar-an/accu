import threading
from django.dispatch import Signal

my_signal = Signal()

def receiver(sender, **kwargs):
    print(f"Receiver thread: {threading.current_thread().name}")
    print("Receiver finished")

my_signal.connect(receiver)

def sender_function():
    print(f"Sender thread: {threading.current_thread().name}")
    my_signal.send(sender=None)
    print("Sender finished")

sender_function()