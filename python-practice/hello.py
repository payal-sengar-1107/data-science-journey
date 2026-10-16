print("payal sengar is my name")
print("my age is 19..")
print("payal sengae is my name.", "my age is 19")
print(2007)
print(2009)
print(2007+2009)

#variable

name="payal"  #string
age=19
price=25.99

age2=age

print(age2)

print("my name is :",name)
print("my age is :",age)

print(type(name))
print(type(age))
print(type(price))

# python data types

#print in single,doble and triple code
name1 ="ss"
name2 ='ss'
name3 ='''ss'''

print(name1)
print(name2)
print(name3)

age=19
old=True
a=None
print(type(age))
print(type(old))
print(type(a))

#python operators

#arithimetic operators

a=50
b=20 

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder
print(a**b) #a ki power


#relational operators
a=100
b=50

print(a==b)#False
print(a!=b)#True
print(a>=b)#True
print(a>b)#tTrue
print(a<=b)#True
print(a<b)#False

#assingment operators
num=10
num=num+10 #10+10 => 20
num*=10
print(num)

#logical operators
a=30
b=20
print(not False)
print(not(a>b))

val1=True
val2=True
print("And operators:",val1 and val2)
print("OR operator:",val1 or val2)
val1=True 
val2=False
print("And operators:",val1 and val2)
print("OR operator:",val1 or val2)

# type conversion
a=4
b=3.55

sum=a+b # 4.0+3.55=7.55
print(sum)

#input in python

input("enter youe name:")
name=input("enter your ege:")
print("you entered",name)

int("5")
val=float(input("enter some value:"))
print(type(val1),val)

name=input("enter name:")
age=input("enter age:")
marks=input("enter marks:")

# question 1 = write a program to input and print their sum

first=int(input("enter first : "))
second=int(input("enter second : "))

print("sum =", first + second)

#  question 2 = wap to input side of a square and print its area

side = float(input("enter square side :"))
print("area=", side** 2)

# question 3 = wap to input 2 floating point numbers and print their average

a= float(input("enter first : "))
b= float(input("enter second : "))

print("avg=", (a+b)/2)

# question 3 = wap to input 2 int numbers ,a andb. print true if a is greater than or equal to b. if not print false

a= int(input("enter first :"))
b= int(input("enter second :"))

print(a>=b)
            



