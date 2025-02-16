def my_decorator(func):
    def wrapper():
        print('Before the function')
        func()
        print('After the function')
    return wrapper

@my_decorator
def say_hello():
    print('Hello!')

say_hello()

#############################################
def greet_decorator(func):
    def wrapper(name):
        print('welcome!')
        func(name)
        print('have a great day!')
    return wrapper

@greet_decorator
def greet(name):
    print(f'Hello {name}!')

greet('siberbot88')

##############################################

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments {args}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a+b

add(3,5) 
