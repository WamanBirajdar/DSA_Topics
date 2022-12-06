'''monkey patching is very intresting concept 
it s a process to altering the functionality of exiting classes or modules
or another way you can say piece of code in python to change behaviour of function or calsses modules at run time'''

#change function functionality

def add(a,b):
    print(f'addition of two  nubber is: {a+b}')

def sub(a,b):
    print(f'substraction of wo numbrs is: {a-b}')

add(2,3)
print(f'after monkey patching')
add=sub
add(2,3)
