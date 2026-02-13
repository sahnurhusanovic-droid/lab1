"""#1
def is_valid_digit(n):
    s=str(n)
    for digit in s:
        if int(digit)%2!=0:
            return False
    return True
n=int(input())
if is_valid_digit(n):
    print("Valid")
else:
    print("Not valid")
    
#2
def isUsual(num):
    if num<=0:
        return False
    for prime in [2,3,5]:
        while num%prime==0:
            num//=prime
    return num==1
num=int(input())
if isUsual(num):
    print("Yes")
else:
    print("No")
    
#3
q=input()
if "+" in q:
    op="+"
elif "-" in q:
    op="-"
elif "*" in q:
    op="*"
parts=q.split(op)
a=parts[0]
b=parts[1]
def to_number(s):
    result=""
    for i in range(0,len(s),3):
        part=s[i:i+3]
        if part=="ZER":
            result+="0"
        elif part=="ONE":
            result+="1"
        elif part=="TWO":
            result+="2"
        elif part=="THR":
            result+="3"
        elif part=="FOU":
            result+="4"
        elif part=="FIV":
            result+="5"
        elif part=="SIX":
            result+="6"
        elif part=="SEV":
            result+="7"
        elif part=="EIG":
            result+="8"
        elif part=="NIN":
            result+="9"
    return int(result)
def to_words(num):
    num=str(num)
    answer=""
    for digit in num:
        if digit=="0":
            answer+="ZER"
        elif digit=="1":
            answer+="ONE"
        elif digit=="2":
            answer+="TWO"
        elif digit=="3":
            answer+="THR"
        elif digit=="4":
            answer+="FOU"
        elif digit=="5":
            answer+="FIV"
        elif digit=="6":
            answer+="SIX"
        elif digit=="7":
            answer+="SEV"
        elif digit=="8":
            answer+="EIG"
        elif digit=="9":
            answer+="NIN"
    return answer
num1=to_number(a)
num2=to_number(b)
if op=="+":
    result=num1+num2
elif op=="-":
    result=num1-num2
elif op=="*":
    result=num1*num2
print(to_words(result))

#4
class StringHandler:
    def getString(self):
        self.s=input()
    def printString(self):
        print(self.s.upper())
a=StringHandler()
a.getString()
a.printString()

#5
class Shape:
    def area(self):
        return 0
class Squere(Shape):
    def __init__(self,lenght):
        self.lenght=lenght
    def area(self):
        return self.lenght**2
a=int(input())
s=Squere(a)
print(s.area())

#6
class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
a,b=list(map(int,input().split()))
s=Rectangle(a,b)
print(s.area())

#7
import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self,new_x,new_y):
        self.x=new_x
        self.y=new_y
    def dist(self,other_point):
        dx=self.x-other_point.x
        dy=self.y-other_point.y
        return math.sqrt(dx**2+dy**2)
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
p1=Point(x1,y1)
p1.show()
p1.move(x2,y2)
p1.show()
p2=Point(x3,y3)
distance=p1.dist(p2)
print(f"{distance:.2f}")

#8
class Accaunt:
    def __init__(self, balance):
        self.balance = balance
    def deposite(self, amount):
        self.amount = amount
    def withdraw(self, amount):
        if amount>self.balance:
            return "Insufficient Funds"
        else:
            self.balance-=amount
            return self.balance
balance,amount=map(int,input().split())
acc=Accaunt(balance)
result=acc.withdraw(amount)
print(result)

#9
import math
class Circle:
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius
r=int(input())
r*=r
p=Circle(r)
print(f"{p.area():.2f}")

#10
class Person:
    def __init__(self, name):
        self.name=name
class Student(Person):
    def __init__(self,name,gpa):
        super().__init__(name)
        self.gpa=gpa
    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")
name,gpa=map(str,input().split())
s=Student(name,gpa)
s.display()

#11
class Pair:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,other):
        return Pair(self.a+other.a,self.b+other.b)
a1,b1,a2,b2=map(int,input().split())
p1=Pair(a1,b1)
p2=Pair(a2,b2)
result=p1.add(p2)
print(f"Result: {result.a} {result.b}")

#12
class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def total_salary(self):
            return self.base_salary
class Manager(Employee):
    def __init__(self,name,base_salary,bonus_persent):
        super().__init__(name,base_salary)
        self.bonus_persent=bonus_persent
    def total_salary(self):
        return self.base_salary+(self.base_salary*self.bonus_persent/100)
class Developer(Employee):
    def __init__(self,name,base_salary,completed_project):
        super().__init__(name,base_salary)
        self.completed_project=completed_project
    def total_salary(self):
        return self.base_salary+self.completed_project*500
class Intern(Employee):
    pass
data=input().split()
role=data[0]
if role=="Manager":
    name=data[1]
    base_salary = int(data[2])
    bonus_persent = int(data[3])
    emp=Manager(name,base_salary,bonus_persent)
elif role=="Developer":
    name=data[1]
    base_salary = int(data[2])
    completed_project = int(data[3])
    emp=Developer(name,base_salary,completed_project)
elif role=="Intern":
    name=data[1]
    base_salary=int(data[2])
    emp=Intern(name,base_salary)
print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")

#13
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
numbers=list(map(int,input().split()))
primes=list(filter(lambda x: is_prime(x),numbers))
if primes:
    print(*primes)
else:
    print("No primes")"""
    
#14
n=int(input())
arr=list(map(int,input().split()))
q=int(input())
operations=[input().split() for _ in range(q)]
for op in operations:
    if op[0]=="add":
        x=int(op[1])
        arr=list(map(lambda a:a+x, arr))
    elif op[0]=="multiply":
        x=int(op[1])
        arr=list(map(lambda a: a*x, arr))
    elif op[0]=="power":
        x=int(op[1])
        arr=list(map(lambda a:a**x, arr))
    elif op[0]=="abs":
        arr=list(map(lambda a:abs(a), arr))
print(*arr)