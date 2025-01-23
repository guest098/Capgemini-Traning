# print('Hello world')
# firstname="Peddireddy"
# lastname="Shanmukreddy"
# print(f"{firstname+" "+lastname}")
# firstname=input('Enter the first name')
# lastname=input('Enter the second name')
# print(f'my name is {firstname+" "+lastname}')
# Name=input('Enter the name:')
# Address=input('Enter the address:')
# Email=input('Enter the email:')
# Number=int(input('Enter the number'))
# print(f'My name is {Name}, and i am living in {Address} and my emailid is {Email} and my Number is {Number}')

def sum(a,b):
    return a+b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def subtract(a,b):
    if(a<b):
        return b-a
    else:
        return a-b
a=int(input('Enter the first number'))
b=int(input('Enter the second number'))
print(sum(a,b))
print(multiply(a,b))
print(subtract(a,b))
print(divide(a,b))