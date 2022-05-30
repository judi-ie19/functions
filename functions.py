from tkinter.font import names
from unicodedata import name


def greet(name,age):
    year=2022-age
    print(f"hello {name} you were born in {year}")

def hello2(name):
    print(f"hello {name}")
    return
    print("welcome to Adalab")
def hello3(name):
    return f"hello {name}"

def my_country(name,country="Uganda"):
    return f"Hello {name} from {country}"

def hello_multi(*name):
     print(names)

def hello_sum(*args):
    sum=0
    for num in args:
        num+=sum
        return sum
    

  
def greet_multiple(**kwargs):
    keys=kwargs.keys()
    if "name" in keys():
        print("Hello{kwargs['name'}")
    elif "country" in keys():
        print("Hello from{kwargs['country'}")
    else:
        print("Hello anonymous")

def sum_and_greet(*args,**kwargs):
    print(args)
    print(kwargs)

