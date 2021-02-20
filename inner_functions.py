# Decorator(s)) function is a function which takes in a function (as an arguement)
# Adds more functionality to it,
# Additional functionality is added before and after execution of the function taken as an arguement
def printer():
    print("Hello world!")


def print_msg(func):

    def inner():
        print('Executing!', func.__name__, 'function')
        func()
        print('End Execution')

    return inner


decorated_func = print_msg(printer)
decorated_func()

# Instead of creating an additional variable which holds the function executing the inner function
# Python makes it one step easier