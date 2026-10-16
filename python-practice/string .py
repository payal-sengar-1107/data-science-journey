jstr1 = "apna collage" 
len1 = len(str1)
print(len1)

str2 = "series"
len2 = len(str2)
print(len2)

final_str = str1+str2
print(final_str)
print(len(final_str))

#indexing

str = "apna collage"
ch = str[7]
print(ch)
print(str[3]) # second type

#slicing

str = "apna collage"
print(str[1:4])
print(str[:3]) #[0;4]
print(str[5:]) #[5:len(str)]

#slicing negtaive index

str = "apple"
print(str[-1:-3])
print(str[-5:-3])

# string functions

str = ("i am studying from apna collage")
print(str.endswith("age"))

str = "my self respect is biggest things in my life"
str = str.capitalize()
print(str)
print(str.replace("self", "python")) # yet also change any one word
print(str.find("is"))
print(str.count("g"))

# question 1= WAP to find user's first name and price its length

name = input("enter your name :")
print("length of your name is", len(name))

#que 2 = WAP to find the occurrence of "$" in a string

str = "Hi, $Iam the $ symbol $99.99"
print(str.count("$"))

# conditional statement

light ="green"

if(light == "red"):
    print(stop)
elif(light == "green"): 
    print("go")
elif(light == "yellow"):
    print("look")

print("end of code")

# new code
age = 14

if(age >= 18):
    print("can vote") # indentation{} = means proper spacing
else:
    print("CANNOT vote")


# new code
marks = int(input("enter student marks :")) 

if (marks >=90):
    grade = "A"
elif(marks >=80 and marks<90):
    grade ="B"   
elif(marks >=70 and marks<80):
    garde ="C" 
else:
    grade ="D"

print("grade of the student -> , grade")

#new code
age = 95

#nesting = doing one statement ke under second statement work
if(age>=18):
    if (age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")  

 # practice question
 #  question 1 = WAP to cheak if a number entered by the user is odd or even..

num = int(input("enter number:"))

rem = num%2

if(rem==0):
    print("EVEN")
else:
    print("ODD")   
  

#WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER..

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))

if(a>=b and a>=c): # logical oprators
    print("first number is largest",a)
elif(b>=c):
    print("second number is largest",b)
else:
    print("third is largest",c)    

#  WAP to cheak if a number is a multiple of 7 or not..

x = int (input("enter number: "))

if(x % 7 ==0):
    print("multiple of 7")
else:
    print("not a multiple")
