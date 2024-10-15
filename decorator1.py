print("script for decorators")

def decorator_function(fun):
    def wrapper_function():
        print("wash hands and wash face ")
        fun()
        print("Bartan dona bartan dona")
    return wrapper_function

@decorator_function
def khana_banana():
    print("Cook food Cook Nice food !!!!!")
khana_banana()