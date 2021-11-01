def outer(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@outer
def my_function():
    print("I am ordinary function")

my_function()