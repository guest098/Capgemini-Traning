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

# def sum(a,b):
#     return a+b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
# def subtract(a,b):
#     if(a<b):
#         return b-a
#     else:
#         return a-b
# def result(a):
#     return a//10*10
# a=255
# # b=int(input('Enter the second number'))
# # print(sum(a,b))
# # print(multiply(a,b))
# # print(subtract(a,b))
# # print(divide(a,b))
# print(result(a))
# import math
# def result(a,b,c):
#     d=b**2-4*a*c
#     if d<0:
#         return 0
#     root1=(-b+math.sqrt(d))/(2*a)
#     root2=(-b-math.sqrt(d))/(2*a)
#     return root1,root2
# a=1
# b=4
# c=5
# print(result(a,b,c))
# import math
# def absoulte(a,b):
#     return abs(a-b)
# def cosine(c):
#     return math.cos(math.radians(c))
# def sine(c):
#     return math.sin(math.radians(c))
# def tangent(c):
#     return math.tan(math.radians(c))
# def eluer():
#     return math.e
# def logrithmic(d):
#     return math.log10(d)
# def power(b,a):
#     return math.pow(b,a)
# def pivalue():
#     return math.pi
# def sqrtu(a):
#     return math.sqrt(a)
# def ceilnumber(e):
#     return math.ceil(e)
# def floornumber(e):
#     return math.floor(e)
# def factorial(d):
#     return math.factorial(d)
# def gcd(a,b):
#     return math.gcd(a,b)
# def abs1(f):
#     return abs(f)
# a=1
# b=2
# c=90
# d=10
# e=4.8
# f=-1
# print(absoulte(a,b))
# print(cosine(c))
# print(sine(c))
# print(tangent(c))
# print(eluer())
# print(logrithmic(d))
# print(power(b,a))
# print(pivalue())
# print(sqrtu(a))
# print(ceilnumber(e))
# print(floornumber(e))
# print(factorial(d))
# print(gcd(a,b))
# print(abs1(f))
#list 1:
# counter=["abc","efg"]
# print(counter[1])
# print(counter)
# print(counter[0])
# #area of rectangle:
# def rectangle(a,b):
#     return a*b
# a=int(input())
# b=int(input())
# print(rectangle(a,b))
def count_digits(text):
    count=[0]*10
    for ch in text:
        if ch.isdigit():
            count[int(ch)]+=1
    return count
def display(counts):
    for digit,count in enumerate(counts):
        print(f'{digit}:{count}')
text="12=34 1119" 
counts=count_digits(text)  
display(counts)