Property-Decorator in Python

https://pybit.es/property-decorator.html

PyTest-Fixtures

https://pybit.es/pytest-fixtures.html

In order to understand about decorators, we must first know a few basic things in Python.

We must be comfortable with the fact that everything in Python (Yes! Even classes), are objects. Names that we define are simply identifiers bound to these objects. Functions are no exceptions, they are objects too (with attributes). Various different names can be bound to the same function object.

Here is an example.

def first(msg): print(msg)

first("Hello")

second = first second("Hello")
