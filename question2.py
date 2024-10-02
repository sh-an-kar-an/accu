#  Django signals are executed in the same thread as the caller.
#  When a signal is sent, the connected receivers are executed in the same thread that sent the signal. 
#  This means that the signal sending and receiving processes are blocking, 
#  and the code that sent the signal will wait for all connected receivers to finish executing before continuing.



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
