# def get_input():
#     n=int(input('Enter the size of an nay:'))
#     n=[]
#     for i in range(n):
#         x=int(input('Enter the elements of an nay:'))
#         n.append(x)
#     return n
# def main():
#     n=get_input()
#     print("Original nay:",n)
# main()
# import nay
# n=nay.nay('i',[1,2,3,4,5])
# print("Original nay:",n)
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# print('nay1:',l1)
# print('nay2:',l2)
# l3=["abc","def","ghi"]
# print('list3 first value:',l3[0])
# l4=[["abc","def","ghi"],["jkl","mno","pqr"],["stu","vwx","yz"]]
# print('list4 first value:',l4[0][0])
# print(list(range(0,4)))
# l5=list(range(6))
# print("l5 list :",l5)
# rows=int(input('ENTER THE NUMBER OF ROWS'))
# NESTEDLIST=[]
# for i in range(rows):
#     ROW=list(map(int,input().split()))
#     NESTEDLIST.append(ROW)
# print('Nested list:',NESTEDLIST)
# list1=[1,2,3,4,5]
# print("list1:",list1[1:4])
# print("list1 Length:",len(list1))
# list=["x",[10,20,30,40],"y"]
# print("list:",list[1][2])
# print("list1:",list[1][1:3])
# def sum_of_an_nay(n):
#     sum=0
#     for i in n:
#         sum+=i
#     return sum
# def max_and_min(n):
#     n.sort()
#     return n[0],n[-1]
# def max_and_min_without_inbuilt(n):
#     max=n[0]
#     min=n[0]
#     for i in n:
#         if i>max:
#             max=i
#         elif i<min:
#             min=i
#     return min,max
# def prime_or_not(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# def prime_numbers(n):
#     prime_numbers=[]
#     for i in range(2,n):
#         if prime_or_not(i):
#             prime_numbers.append(i)
#     min,max=prime_numbers[0],prime_numbers[-1]
#     return prime_numbers,min,max

def get_input():
    n=int(input('Enter the number of elements:'))
    listA=[]
    for i in range(n):
        listA.append(input('Enter the element: '))
    return listA
def palindrome_or_not(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
def palindrome_inlist():
    listb="madam"
    return palindrome_or_not(listb)
def palindrome_using_for_loop(ListA):
    for i in ListA:
        if palindrome_or_not(i):
            print(i,'is a palindrome')
        else:
            print(i,'is not a palindrome')
# def space_elimination_in_array(ListA):
#     ListB=[]
#     for i in ListA:
#         ListB.append(i.replace(' ',''))
#     return ListB
def space_elimination_in_array_without_inbuilit_functions(s):
    i=0
    ListA=list(s)
    while i<len(ListA):
        if ListA[i]==' ' and ListA[i+1]==' ':
            ListA.pop(i)
        else:
            i+=1
    return palindrome_or_not(''.join(ListA))
def main():
    listA=get_input()
    s=input('Enter the input')
    palindrome_using_for_loop(listA)
    print(palindrome_inlist())
    print(space_elimination_in_array_without_inbuilit_functions(s))
main()