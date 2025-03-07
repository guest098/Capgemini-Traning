#tuples
# def get_input():
#     n=()
#     return n
# def get_input1():
#     n=(0,)
#     return n
# def get_input2():
#     n=(0,'NI',1.2,3)
#     return n
# def get_input3():
#     r=0,'Ni',1.2,3
#     return r
# def get_input4():
#     t=('abc',('def','ghi'))
#     return t
# def get_input5():
#     t=tuple('spam')
#     return t
# def get_input6():
#     t=(1,2,3,4,5)
#     for i in t:
#         return t[i]
# def get_input7():
#     t=(1,2,3,4,5)
#     return t[1:3]
# def get_input8():
#     t=('abc',('efg','hij'))
#     return  t[0][1:3]
# def main():
#     n = get_input()
#     n1=get_input1()
#     n2=get_input2()
#     n3=get_input3()
#     n4=get_input4()
#     n5=get_input5()
#     n6=get_input6()
#     n7=get_input7()
#     n8=get_input8()
#     print(n)
#     print(n1)
#     print(n2)
#     print(n3)
#     print(n4)
#     print(n5)
#     print(n6)
#     print(n7)
#     print(n8)
# main()
#sets
# empty_set=set()
# print(empty_set)
# #set with elements
# s={1,2,3,4,5}
# print(s)
# #set with duplicate elements
# s={1,2,2,3,3,4,4,5,5}
# print(s)
# #union
# s={1,2,3,4,5}
# t={4,5,1,6,7,8}
# print('Union',s.union(t))
# print('Union using or:',s|t)
# #intersection
# s={1,2,3,4,5}
# t={4,5,1,6,7,8}
# print('Intersection',s.intersection(t))
# print('Internsection using and:',s&t)
# #difference
# s={1,2,3,4,5}
# t={4,5,1,6,7,8}
# print('Difference',s-t)
# print('Difference using inbuilt:',s.difference(t))
# #list into tuple:
# list=[1,2,3]
# tuple=tuple(list)
# print(tuple)
# # Convert a tuple into a list
# tuple1 = (1, 2, 3)  # Use a variable name other than 'tuple' to avoid confusion
# list1 = list(tuple1)
# print(list1)  # Output: [1, 2, 3]
# class Employee:
#     def __init__(self,employee_id,name, age,salary,postion):
#         self.employee_id=employee_id
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.postion = postion
        
#     def display(self):
#         print(f"Employee_id:{self.employee_id} ,Name: {self.name}, Age: {self.age}, Salary: {self.salary} , Position: {self.postion}") 
#     def salary_update(self):
#         self.salary = self.salary + 1000
# if __name__=='__main__':
#     emp1=Employee(1,'John',30,5000,'Software Engineer')
#     emp1.display()
#     emp1.salary_update()
#     emp1.display()
# class Employee:
#     def __init__(self,name,age,gender,position,base_salary,food_allowance,travel_allowance):
#         self.name = name
#         self.age=age
#         self.gender=gender
#         self.position=position
#         self.__basesalary=base_salary
#         self.__bonus=0
#         self.__deductions=0
#         self.__food_allowance=food_allowance
#         self.__travel_allowance=travel_allowance
#         self.__tax=0
#     def get_base_salary(self):
#         return self.__basesalary
#     def set_base_salary(self,salary):
#         if salary>=0:
#             self.__basesalary=salary
#         else:
#             print("Invalid salary")
#     def get_bonus_salary(self):
#         return self.__bonus
#     def set_bonus_salary(self,bonus):
#         if bonus>=0:
#             self.__bonus=bonus
#         else:
#             print("Invalid bonus")
#     def get_deductions(self):
#         return self.__deductions
#     def set_deductions(self,deductions):
#         if deductions>=0:
#             self.__deductions=deductions
#         else:
#             print("Invalid deductions")
#     def get_food_allowance(self):
#         return self.__food_allowance
#     def set_food_allowance(self,food_allowance):
#         if food_allowance>=0:
#             self.__food_allowance=food_allowance
#         else:
#             print("Invalid food allowance")
#     def get_travel_allowance(self):
#         return self.__travel_allowance
#     def set_travel_allowance(self,travel_allowance):
#         if travel_allowance>=0:
#             self.__travel_allowance=travel_allowance
#         else:
#             print("Invalid travel allowance")
#     def get_tax(self):
#         return self.__tax
#     def set_tax(self,tax):
#         if tax>=0:
#             self.__tax=tax
#         else:
#             print("Invalid tax")
#     def calculate_tax(self,tax_rate):
#         gross_salary=self.calculate_gross_salary()
#         self.__tax=(gross_salary)*(tax_rate/100)
#         return self.__tax
#     def calculate_net_salary(self,tax_rate):
#         gross_salary=self.calculate_gross_salary()
#         tax_rate1=self.calculate_tax(tax_rate)
#         return gross_salary-tax_rate1

#     def calculate_gross_salary(self):
#         return self.__basesalary+self.__bonus-self.__deductions+self.__food_allowance+self.__travel_allowance
#     def display(self,tax_rate):
#         print(f'Name:{self.name}')
#         print(f'Age:{self.age}')
#         print(f'Gender:{self.gender}')
#         print(f'Position:{self.position}')
#         print(f'Base Salary:{self.__basesalary}')
#         print(f'Bonus Salary:{self.__bonus}')
#         print(F'Deductions Salary:{self.__deductions}')
#         print(f'Food Allowance:{self.__food_allowance}')
#         print(f'Travel Allowances:{self.__travel_allowance}')
#         print(f'Tax charged:{self.__tax}')
#         print(f'Calculated tax:{self.calculate_tax(tax_rate)}')
#         print(f'Net Salary:{self.calculate_net_salary(tax_rate)}')
#         print(f'Calculate Gross Salary:{self.calculate_gross_salary()}')
# if __name__=='__main__':
#     name=input('Enter the name:')
#     age=int(input('Enter the age:'))
#     gender=input('Enter the gender:')
#     position=input('Enter the position:')
#     salary=int(input('Enter the salary:'))
#     food_allowance=int(input('Enter the food allowance:'))
#     travel_allowance=int(input('Enter the travel allowance:'))
#     tax=int(input('Enter the tax rate'))
#     emp=Employee(name,age,gender,position,salary,food_allowance,travel_allowance)
#     emp.display(tax)
#     bonus=int(input('Enter the bonus:'))
#     deductions=int(input('Enter the deductions:'))
#     emp.set_bonus_salary(bonus)
#     emp.set_deductions(deductions)
#     emp.set_tax(tax)
#     emp.display(tax)
#inheritance concept:
# class Parent:
#     def display_parent_class(self):
#         print("This is parent class")
# class Child(Parent):
#     def display_child_class(self):
#         print('This is the child class')
# if __name__=='__main__':
#     child=Child()
#     child.display_parent_class()
# class Parent:
#     def __init__(self):
#         self.bignose="20cm"
#     def display_patent_class(self):
#         print('THis is the parent class')
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.smallnose="10cm"
#     def display_child_class(self):
#         print('This is the child class')
# if __name__=='__main__':
#     child=Child()
#     child.display_child_class()
#     child.display_patent_class()
#     print(child.bignose)
#     print(child.smallnose)

class School:
    def __init__(self,name,age,grade,schoolname):
        self.name=name
        self.age=age
        self.grade=grade
        self.schoolname=schoolname
    def school_details(self):
        print(f'The name of the student:{self.name}')
        print(f'The age of the student:{self.age}')
        print(f'The grade of the student:{self.grade}')
        print(f'The name of the school:{self.schoolname}')
class UnderGradute(School):
    def __init__(self,name,age,grade,schoolname,universityname,ug_course,ug_cgpa):
        super().__init__(name,age,grade,schoolname)
        self.grade=self.grade
        self.age=self.age+2
        self.universityname=universityname
        self.ugcourse=ug_course
        self.ugcgpa=ug_cgpa
    def ug_details(self):
        print(f'The name of the student:{self.name}')
        print(f'The age of the student:{self.age}')
        print(f'The grade of the student:{self.grade}')
        print(f'The name of the school:{self.schoolname}')
        print(f'The name of the university:{self.universityname}')
        print(f'The ug course of the student:{self.ugcourse}')
        print(f'The ug cgpa of the student:{self.ugcgpa}')
class Postgraduate(UnderGradute):
    def __init__(self,name,age,grade,schoolname,universityname,ug_course,ug_cgpa,pg_course,pgunviersityname,pg_cgpa):
        super().__init__(name,age,grade,schoolname,universityname,ug_course,ug_cgpa)
        self.pg_course=pg_course
        self.grade=self.grade
        self.age=self.age+4
        self.pguniversityname=pgunviersityname
        self.pg_cgpa=pg_cgpa
        def pg_details(self):
            print(f'The name of the student:{self.name}')
            print(f'The age of the student:{self.age}')
            print(f'The grade of the student:{self.grade}')
            print(f'The name of the school:{self.schoolname}')
            print(f'The name of the university:{self.universityname}')
            print(f'The ug course of the student:{self.ugcourse}')
            print(f'The ug cgpa of the student:{self.ugcgpa}')
            print(f'The pg course of the student:{self.pg_course}')
            print(f'The pg university of the student:{self.pguniversityname}')
            print(f'The pg cgpa of the student:{self.pg_cgpa}')
if __name__ == "__main__":
    print('School details:')
    school=School('Rahul',18,'A','ABC school')
    school.school_details()
    print('UnderGraduate details:')
    