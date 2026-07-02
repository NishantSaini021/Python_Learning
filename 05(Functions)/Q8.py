# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
def fun_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
fun_kwargs(Name = "Nishant", City = "Ajmer", Age = 19)