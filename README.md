# Django Signals and Python Rectangle Class

This repository contains examples and explanations for **Django signals** and a **Python Rectangle class**.

## Django Signals

Django signals are a way to notify other parts of an application when certain events occur. They are executed synchronously, meaning that the code that sends the signal will wait for all connected receivers to finish executing before continuing.

### Key Points
- Django signals are executed synchronously.
- Django signals run in the same thread as the caller.
- Django signals run within the same database transaction as the caller.

### Example Code

The directory contains example code that demonstrates the concepts:

- **question1.py**: Demonstrates that Django signals are executed synchronously.
- **question2.py**: Demonstrates that Django signals run in the same thread as the caller.
- **questiion3.py**: Demonstrates that Django signals run within the same database transaction as the caller.

## Python Rectangle Class

The Python Rectangle class is a custom class that meets the following requirements:

- An instance of the Rectangle class requires length and width to be initialized.
- The class is iterable, yielding dictionaries with the length and width attributes.

### Example Code

- **question4.py**: The implementation of the Rectangle class


