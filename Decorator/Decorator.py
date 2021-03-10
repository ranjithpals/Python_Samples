
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
        print('Returning the Actual Function to be executed...')
        # This statement will just return the Function: divide(a, b) as an object,
        # It (statement/object) does not run the divide function as such.
        return func(a, b)
    return inner


# Divide two integers
@check_division_error
def divide(a, b):

    return a/b


# Before divide(15, 3) is executed, the Decorator is invoked.
# After the Decorator returns the Function Object, the print() function is going to execute the Function Object
# Executing the print() function will return the result of the divide() function
print(divide(15, 3))

try:
    print(divide(15, 0))
except Exception as msg:
    print(msg)