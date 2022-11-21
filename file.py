# try:
#     print(10/0) 
# except Exception as s:
#     print("my nme is khan")
#     print(5/0)
# except (Exception) as f:
    
#     print("i am hero",f)
# s=set("shri")
# print(s)
# s=input("Enter str=")
# w=set(s)
# e={"a","e","i","o","u"}
# a=w.difference(e)
# print(a)

# s="shriyashmane"
# print(s[len(s)-9:])

# import pymysql
# con=pymysql.connect(host='localhost',database='self',user='root',password='shri1234')
# cursor=con.cursor()    ## used to make the connection for executing SQL queries
# cursor.execute('select * from shri')
# records=cursor.fetchall()
# for x in records:
#     print(x)

# def add(x):
#     if x%2==0:
#         print("even no",x)
#     else:
#         print("odd no",x)
# add(20)

# def add(lst):
#     count=0
#     for i in lst:
#         s=i+lst[count]
#         count=count+1
#     return s
# lst=[20,50,80]
# l=add(lst)
# print(l)

# def mult(x):
#     count=1
#     for i in x:
#         res=i*x[count]
#         count=count+1
#     return res
# x=[10,50,40,70,80]
# c=mult(x)
# print(c)

# def mul(lst):
#     res=1
#     for i in lst:
#         res=i*res
#     print(res)
# lst=[10,20,30] 
# mul(lst)       

# t=int(input("number="))
# if t%3==0 and t%5==0:
#     print("shriyash mane")
# elif t%3==0:
#     print("shriyash")
# elif t%5==0:
#     print("mane")
# else:
#     print("sorry")

# def fact(i):
#     result=1
#     while i>=1:
#         result=i*result
#         i=i-1
#     return result
# e=fact(10)
# print(e)

# def vla(*n):
#     total=1
#     for x in n:
#         total=total*x
#     print(total)
# vla(10,20,30)

# def fact(x):
#     if x==0:
#         res=1
#     else:
#         res=x*fact(x-1)
#     return res
# s=fact(4)
# print(s)

# s=lambda x:x*x
# print(s(4))

# s=lambda x:1 if x==0 else x*(s(x-1))
# print(s(4))

# def ise(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# h=[10,20,30,77,88,97]
# l1=list(filter(ise,h))
# print(l1)

# i=[10,20,30,47,49]
# s=list(filter(lambda x:x%2==0,i))
# print(s)

# s=[10,20,60,80]
# e=list(map(lambda x:x+2,s))
# print(e)

# i=[14,15,16]
# def double(x):
#     return 2*x
# w=list(map(double,i))
# print(w)

# r=[10,20,30]
# t=[50,60,40]
# s=list(map(lambda x,y:x+y,r,t))
# print(s)

# from functools import reduce
# r=[10,20,30,40]
# s=reduce(lambda x,y:x*y,r)
# print(s)

# from functools import reduce
# w=reduce(lambda x,y:x+y,range(1,50))
# print(w)

# sum=0
# for x in range(1,50):
#     sum=x+sum
#     sum+=1
# print(sum)

# mult=1
# for x in range(1,10):
#     mult=x*mult
# print(mult)

# def outer():
#     print("outer fun")
#     def inner():
#         print("Hii inner")
#     print("outer inner")
#     return inner
# f=outer()
# f()
# f()
# f()

# def decor(func):
#     def inner(name):
#         if name=="Bobby":
#             print("hello bobby bad morning")
#         else:
#             func(name)
#     return inner
# @decor
# def wish(name):
#     print("hello",name,"good morning")
# wish("ram")
# wish("sita")
# wish("Bobby")

# def sum(x):
#     def inner(add):
#         if add%2!=0:
#             print("plss provide sum value")
#         else:
#             x(add)
#     return inner
# @sum
# def divide(add):
#     w=add+10
#     print(w)
# divide(15)
# divide(10)

# def decor(x):
#     def mydecor(a,b):
#         if b==0:
#             print("sorry cant divide")
#         else:
#             return x(a,b)
#     return mydecor

# @decor
# def division(a,b):
#     return a/b
# print(division(20,2))
# print(division(10,0))

# def outer3(c):
#     print("Hii i am outer3")
#     def inner(x):
#         j=c(x)
#         return 30*j
#     return inner
# def outer2(w):
#     print("Hii i am outer2")
#     def inner(x):
#         g=w(x)
#         return 10*g
#     return inner
# def outer(f):
#     print("Hii i am outer")
#     def inner(u):
#         o=f(u)
#         return 2+o
#     return inner
# @outer3
# @outer2
# @outer
# def num(x):
#     print("Hii i am num")
#     return 10+x
# print(num(5))

# def veryoutside(x):
#     print("Hii i am veryoutside")
#     def inner(first):
#         x(first)
#     return inner
# def outside(x):
#     print("Hii i am outside")
#     def inner(first):
#         x(first)
#     return inner
# def inside(x):
#     print("Hii i am inide")
#     def inner(first):
#         x(first)
#     return inner
# @inside
# @outside
# @veryoutside
# def mai(first):
#     print("Hii i am main",first)
# mai("shri")

# def gen(x):
#     h=1
#     while h<=x:
#         yield x
#         x=x-1
# s=gen(10)
# for i in s:
#     print(i,end=' ')

# def add(x):
#     d=1
#     while d<=x:
#         yield d
#         d=d+1
# w=add(10)
# for i in w:
#     print(i,end=' ')

# def renew(x):
#     k=0
#     while k<=x:
#         yield k
#         k=k+1
# q=renew(5)
# for e in q:
#     print(e,end=' ')

# The next is the sum of previous 2 numbers ( Fibonacci Numbers)
## 0,1,1,2,3,5,8....

# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for x in fib():
#     if x>100:
#         break
#     print(x,end=' ')

# g=[x*x for x in range(10)]
# print(g)


# print(__name__)

# w=open("eef.py","r")
# # w.write("shri\n")
# # w.write("maneee\n")
# g=w.read()
# print(g)
# w.close()

# import os
# o=os.getcwd()
# print(o)

# try:
#     print(10/0)
#     print("hello")
# except ZeroDivisionError:
#     print("not ok")
# finally:
#     print("ggg")

# class Python:
#     def __init__(s,name,rollno,add):
#         s.x=name
#         s.y=rollno
#         s.z=add

#     def mohan(self,id):
#         print("batch name is:",self.x)
#         print("batch rollno is:",self.y)
#         print("batch add is:",id)

# l=Python("shri",101,"pune")
# l.mohan(2)

# class ss:
#     def __init__(self) :
#         self.ename="shri"
#         self.eno=100
#         self.eadd="pali"
#     def m1(s,j):
#         s.d=100
#         print("hello",j)
# w=ss()
# w.m1(100)
# w.e=200
# print(w.__dict__)


# class Employee:
#     def __init__(self,eno,ename,esal):
#          self.eno=eno
#          self.ename=ename
#          self.esal=esal
#     def display(self):
#          print('Employee Number:',self.eno)
#          print('Employee Name:',self.ename)
#          print('Employee Salary:',self.esal)
# class Test:
#     def modify(emp):
#          emp.esal=emp.esal+10000
#          emp.display()
# e=Employee(100,'Durga',10000)
# Test.modify(e)

# class Person: 
#     def __init__(self): 
#         self.name='durga' 
#         self.db=self.Dob() 
#     def display(self):  
#         print('Name:',self.name) 
#     class Dob: 
#         def __init__(self): 
#             self.dd=10 
#             self.mm=5 
#             self.yy=1947 
#         def dis(self): 
#             print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy)) 
# p=Person() 
# p.display() 
# x=p.db 
# x.dis()

# a = [1,2,3]
# d = ['a','b','c']
# c = {}
# for i in range(len(a)):
#     c[a[i]] = d[i]
#     #  d.remove(j)
#     # break
# print(c)

# d = []
# for i in a:
#     if i in d:
#         continue
#     else:
#         d.append(i)
# print(d)

# a = [1,2,3, 2, 3, 1]
# s={}
# for i in range(len(a)):
#     s[a[i]]=s.get(a[i],0)+1
# print(s)
# class Test: 
#  def __init__(self,a=None,b=None,c=None): 
#     print('Constructor with 0|1|2|3 number of arguments',a,b) 

# t1=Test() 
# t2=Test(10) 
# t3=Test(10,20) 
# t4=Test(10,20,30)
# class P:
#     def property(self):
#         print("heii")
#     def marry(self):
#         print("marry me")
# class S(P):
#     def marry(self):    
#         print("not me")
# o=S()
# o.property()
# o.marry()
# import re 
# matcher=re.finditer("j","a7b@k9z") 
# for match in matcher: 
#     print(match.start(),"......",match.group()) 

# c=[1,2,3]
# d=["shri","pushpa","Rana"]
# a= {c[i]:d[i] for i in range(len(c))}
# print(a)

# c=[1,2,3]
# d=["shri","pushpa","Rana"]
# w=dict(zip(c,d))
# print(w)
# input_password=int(input("enter password:"))
# password=1234
# while input_password!=password:
#     input_password=int(input("enter password"))
# else:
#     print("congo")
# for i in range(5):
#     for j in range(i+1):
#         print("* ",end="")
#     print()

# for i in range(1,4):
#     print(" "*(4-i)+"* "*i)

# for i in range(5,0,-1):
#     print(i*"* ")

# for i in range(5):
#     for j in range(i,5):
#         print("* ",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(6,i,-1):
#         print("* ",end="")
#     print()
# for i in range(1,6):
#     for j in range(i,5):
#         print("  ",end='')
#     for j in range(i):    
#         print('* ',end='')
#     print()

# for i in range(1,11):
#     if i<=5:
#         print(" "*(5-i),"* "*i)
#     elif i>5:
#         print(" "*(i-5),"* "*(10-i))

# for i in range(1,11):
#     if i<=5:
#         print("* "*i)
#     elif i>5:
#         print("* "*(10-i))

# for i in range(10):
#     if i<5:
#         print((5-(i+1))*'  ',(i+1)*'* ')
#     if i>5:
#         print((i-5)*'  ',(10-i)*'* ')
# char_=65
# for i in range(1,9):
#     print(i*chr(char_))
#     char_=char_+1

# Python program to demonstrate
# Creation of Array

# importing "array" for array creations
# import array as arr

# # creating an array with integer type
# a = arr.array('i', [1, 2, 3])

# # printing original array
# print ("The new created array is : ", end =" ")
# for i in range (0, 3):
# 	print (a[i], end =" ")
# print()

# # creating an array with double type
# b = arr.array('d', [2.5, 3.2, 3.3])

# # printing original array
# print ("The new created array is : ", end =" ")
# for i in range (0, 3):
# 	print (b[i], end =" ")
	
# for i in range(11,0,-1):
#     print("* "*i)

# for i in range(1,4):
#     print(" "*(3-i),i*1)
    


# num=int(input("Enter a number:")) 
# for i in range(1,num+1): 
#     print(" "*(num-i),end="") 
#     for j in range(1,i+1): 
#         print(i,end=" ") 
#     print()

# print(10%6)
# x=int(input("print no"))
# print("even") if x%2==0 else print("odd")
# from functools import reduce
# x=int(input("Enter First Number:")) 
# y=int(input("Enter First Number:")) 
# sum=reduce(lambda x,y:x+y,(x,y))
# print(sum)
# print("sum of {} and {} is {}".format(x,y,sum(x,y)))

# for x in range (1,6):
#     print(" "*(5-x),"* "*x)
# for k in range(6,9):
#     print("* "*(9-k)," "*(k-5))
# a=int(input("enter no:"))
# b=int(input("enter no:"))
# print(a if a>b else b) 

# def fact(num):
#     return 1 if (num==1 or num==0) else num*fact(num-1)
# num=5
# print(fact(num))

# t=123
# r=len(str(t))
# print(r)

# num=int(input("enter no:"))
# if sum([int(i)**len(str(num)) for i in str(num)])==num:
#     print("yes")
# else:
#     print("no")

# num=int(input("enter no:"))
# if sum([int(i)**len(str(num)) for i in str(num)])==num:
#     print("Yes,armstrong no.")
# else:
#     print("no,armstrong no.")

# def area(r):
#     pi=3.143
#     return pi*(r*r)
# radius=4
# print(area(radius))

# arr=[3,1,2,10,1]
# # ou=[3,4,6,16,17]
# # a=arr[0]
# sum=0
# for i in arr:
#     sum=sum+i
#     print(sum,end=' ')

# from functools import reduce

# lst = [1, 2, 3, 4, 5]
# op = reduce(lambda x, y: x + [x[-1] + y], lst, [0])[1:]
# print(op)

# h = eval(input("Enter diamond's height: "))

# for x in range(h):
#     print(" " * (h - x), "*" * (2*x + 1))
# for x in range(h - 2, -1, -1):
#     print(" " * (h - x), "*" * (2*x + 1))

# h = eval(input("Enter diamond's height: "))
# for x in range(h):
#     print(" "*(h-x),"*"*(2*x+1))
# for x in range(h-2,-1,-1):
#     print(" "*(h-x),"*"*(2*x+1))

# lst = [1, 2, 3, 40, 50, 10, 20, 3, 40, 50, 96]

# for i in lst:
#     lst.pop()
# print(lst)
# for i in lst:
#     lst.pop()
# print(lst)
# for i in lst:
#     lst.pop()
# print(lst)
# for i in lst:
#     lst.pop()
# print(lst)

# l=[[10,20,30],[40,50,60],[70,80,90]]
# lis=[x for y in l for x in y]
# print(lis)

# for num in range(2,10):
#     if all(num%i!=0 for i in range(2,num)):
#         print(num)

for i in range(2,10):
    for j in range(2,i):
        if (i%j)==0:
            break
    else:
        print(i)







