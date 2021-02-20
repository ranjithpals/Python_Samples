
# Python provides a much more simpler way of performing this, which is called Decorator
# Refer to the Inner_function.py as a precursor for Decorator

# Decorator function
def print_msg(func):

    # Inner function
    def inner():
        print('Executing', func.__name__, 'function..')
        func()
        print('Finished Execution')

    return inner


# Main function performing the actual work
@print_msg
def printer():
    msg = 'Python'
    print(f'Hello, {msg}! How are you doing')


# printer()


# Decorators with Input parameters
def check_division_error(func):
    # Check if the divisor is zero
    def inner(a, b):
        if b == 0:
            return 'ZeroDivisionError'
        return func(a, b)
    return inner


# Divide two integers
@check_division_error
def divide(a, b):
    return a/b


print(divide(15, 3))

try:
    print(divide(15, 0))
except Exception as msg:
    print(msg)