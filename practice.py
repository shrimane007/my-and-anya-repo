# s=[10,20,5000,4000,7000,6]
# for i in s :
#     if i >=7000:
#         print("cannot proceed",i)
#         continue
#     print(i)

# s=[10,20,30,0,40,50,0,70]
# for i in s:
#     if i==0:
#         print("cannot divisible by 0")
#         continue
#     print("100/{}={}".format(i,int(i/10)))

# b=30
# def fun(a,b=b):
#     return a+b
# print(fun(1))

# l=eval (input("enter list="))
# print(l)
# l=list(range(0,20,2))
# print(l)

# s=["shri","patya","anya","saurya"]
# x=len(s)
# for i in range(x):
#     print("char at {} position is {} and at negative index is{}".format(i,s[i],i-x))

# s=["shri","patya","anya","saurya"]
# print(s.count("shri"))

# s=["shri","patya","anya","saurya"]
# print(s.index("shri"))

# s=["shri","patya","anya","saurya"]
# s.append("shri")
# print(s)

# s=[]
# for x in range(101):
#     if x%2==0:
#         s.append(x)
# print(s)

# s=["shri","patya","anya","saurya"]
# print(s.insert(3,"shri"))
# print(s)

# s=["shri","patya","anya","saurya"]
# p=["my","name","is","007"]
# s.extend(p)
# print(s)

# s=["shri","patya","anya","saurya"]
# w="brother"
# s.extend(w)
# print(s)

# s=[10,20,30,40,50]
# print(s.pop())
# print(s)

# s=[10,20,30,40,50]
# print(s.pop(2))
# print(s)

# s=[10,20,30,40,50]
# print(s.pop(0))
# print(s)

# s=[10,20,30,40,50]
# print(s.pop(0) and s.pop(2))
# print(s)

# myList=['Bran', 11, 33, 'Stark', 22, 33, 11]
# del myList[1:4]
# print(myList)

# s=[10,20,30,40,50]
# del s[1:3]
# print(s)

# s=[10,20,90,40,50]
# print(s.sort(reverse=True))
# print(s)

# y=[10,20,30,40]
# x=y[:]
# x[1]=410
# print(x)
# print(y)

# y=[10,20,30,40]
# x=y.copy()
# x[1]=410
# print(x)
# print(y)

# s=[10,20,30,[40,50],60]
# print(s[3][0])

# s=[[10,20,30],[40,50,60],[70,80,90]]
# for i in range(len(s)):
#     for j in range(len(s[i])):
#         print(s[i][j],end=' ')
#     print()

# s=[x*x for x in range(20)]
# print(s)

# s=[x for x in range(50) if x%2==0]
# print(s)

# words=["Balaiah","Nag","Venkatesh","Chiranjeevi"] 
# i=[w[0] for w in words]
# print(i)

# s="shriyash is clever boy".split()
# w=[[x.upper(),len(s)] for x in s]

# my_string=("shriyash mane")
# str=""
# for i in my_string:
#     str=i+str
# print("Reversed string:",str)

# s="shriyash is clever boy".split()
# w=[[x.upper(),len(s)] for x in s]
# print(w)

# s=["a","e","i","o","u"]
# w=input("Enter str=")
# d=[]
# for x in w:
#     if x in s :
#         if x not in d:
#             d.append(x)
# print(d)

# print('G','F', sep='', end='')
# print('G')
#\n provides new line after printing the year
# print('09','12','2016', sep='-', end='\n')
# print('prtk','agarwal', sep='', end='@')
# print('geeksforgeeks')

# r="shri"
# e=""
# for i in r :
#     e=i+e
# print(e)

# s=22,554,66,661,4564
# print(min(s))

# a=10
# b=20
# c=30
# d=40
# t=a,b,c,d
# print(t) #(10, 20, 30, 40)

# t=10,20,30,40
# a,b,c,d=t
# print("a=",a,"b=",b,"c=",c,"d=",d)

# t= ( x**2 for x in range(1,6))
# for x in t:
#     print(x)

# s=eval(input("enter tuple="))
# sum=0
# f=len(s)
# for x in s:
#     sum=sum+x
#     d=sum/f
# print(sum)
# print(d)

# def smaller_num(x,y):

#     if x>y:
#         number= y
#     else:
#         number= x
#     return number


# x = input("Enter first number:-")

# y = input("Enter second number:-")

# smaller = smaller_num(x,y)
# print(str(smaller))

# import os
# print(os.path.dirname(os.path.abspath(__file__)))
# print(__file__)

# import os
# BASE_DIR=os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')
# print(TEMPLATE_DIR)












