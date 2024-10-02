
 # Django signals are executed synchronously. When a signal is sent,
 # the code that sends the signal will wait for all connected receivers to finish executing before continuing.
 # This ensures that the signal is fully processed before the code that sent the signal continues to run.




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
