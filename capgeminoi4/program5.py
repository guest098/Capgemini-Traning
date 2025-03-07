# class Cat:
#     def sound(self):
#         print('Meow')
# class Dog:
#     def sound(self):
#         print('Bark')
# for animal in [Cat(), Dog()]:
#     animal.sound()
# class School:
#     school_name="ABC School"
#     def __init__(self, name):
#         self.name = name
#     def display(self):
#         return self.name
# p=School('Shanmuk')
# print(p.display())
# print(p.school_name)
# print(School.school_name)
# School.school_name="Ab"
# print(School.school_name)
# p.school_name="abcd"
# print(p.school_name)
# import dis
# dis.dis(School)
# class Employee:
#     def __init__(self,emp_id,name,age,department,salary):
#         self.emp_id=emp_id
#         self.name=name
#         self.age=age
#         self.department=department
#         self.salary=salary
#     def __str__(self):
#         return f"Employee ID: {self.emp_id}, Name: {self.name}, Age:{self.age}, Department: {self.department}, Salary: {self.salary}"
# employees=[]
# num=int(input('Enter the number of employees'))
# for i in range(num):
#     emp_id=int(input('Enter the employee id'))
#     name=input('Enter the name')
#     age=int(input('Enter the age'))
#     department=input('Enter the department')
#     salary=int(input('Enter the salary'))
#     employees.append(Employee(emp_id,name,age,department,salary))
# for employee in employees:
#     print(employee)
# class Example:
#     def __init__(self,name):
#         print(f'First constructer, Hello: {name}')
#     def __init__(self,age):
#         print(f'Second constructer, Age: {age}')
# obj1=Example(25)
# class Example1:
#     def __init__(self,*args):
#         if len(args)==1:
#             print(f'Hello: {args[0]}')
#         elif len(args)==2:
#             print(f'Hello: {args[0]}, Age: {args[1]}')
# obj2=Example1('shanmuk')
# obj3=Example1('Shanmuk',21)
# class Example2:
#     def __init__(self,**kwargs):
#         for key,value in kwargs.items():
#             print(f'{key}:{value}')
# obj4=Example2(name='Shanmuk',age=21)
# class DestructorExample:
#     def __init__(self,name):
#         self.name=name
#         print(f'First constructer, Hello: {self.name}')
#     def __del__(self):
#         print(f"Object {self.name} is destroyed")
# obj5=DestructorExample('Sample')
# del obj5
# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")
# class Man(Person):
#     def __init__(self, name, age,strength):
#         super().__init__(name, age)
#         self.strength=strength
#     def show_strength(self):
#         print(f"Strength: {self.strength}")
# class Woman(Person):
#     def __init__(self, name, age,intelligence):
#         super().__init__(name, age)
#         self.intelligence=intelligence
#     def show_beauty(self):
#         print(f"Beauty: {self.intelligence}")
# class SuperHuman(Man,Woman):
#     def __init__(self, name, age, strength, intelligence):
#         super().__init__(name=name,age=age,strength=strength)
#         self.intelligence=intelligence
#     def show(self):
#         print(f'{self.name} has strength:{self.strength} and Intelligence {self.intelligence}')
# superhuman=SuperHuman("Alex",30,100,200)
# superhuman.show()
# superhuman.display()
# superhuman.show_strength()
# superhuman.show_beauty()
# class Bird:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#     def fly(self):
#         print(f'{self.name} is flying')
# class Hunter:
#     def __init__(self, hunting_skill):
#         self.hunting_skill = hunting_skill
#     def hunt(self):
#         print(f'Hunting with skill level {self.hunting_skill}')
# class Eagle(Bird, Hunter):
#     def __init__(self, name, age, color, height, hunting_skill):
#         Bird.__init__(self, name, age, color)
#         Hunter.__init__(self, hunting_skill)
#         self.height = height
#     def fly(self):
#         print(f'{self.name} is flying at {self.height} meters')
# eagle = Eagle("Golden Eagle", 5, "Brown", 2000, "Expert")
# eagle.fly()  
# eagle.hunt()  
# print(eagle.name)
# class Shape:
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
# class Square(Shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side**2
# square=Square(4)
# circle=Circle(5)
# print(square.area())
# print(circle.area()) 
from datetime import date
class Order:
    def __init__(self,order_id,order_status,order_date,required_date,shipped_date,store_id,staff_id):
        self.order_id=order_id
        self.order_status=order_status
        self.order_date=order_date
        self.required_date=required_date
        self.shipped_date=shipped_date
        self.store_id=store_id
        self.staff_id=staff_id
        self.items=[]
    def add_item(self,item):
        self.items.append(item)
    def get_total_price(self):
        return sum(item.get_total() for item in self.items)
