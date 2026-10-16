#functions defination
def calc_sum(a,b):
     sum = a+b
     print(sum)
     return sum

calc_sum(4,6)
calc_sum(50,40)

def calc_sum(a,b): #paremetrs
     return a + b

sum = calc_sum(3,4)  #functions call : arguments print(sum)
print(sum)

def print_hello():
     print("hello")

print_hello()

  # average of 3 numbers..

def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(5,6,9) # 6.smething
calc_avg(2,3,4)

 # types of functions 

print("miss","pyson") #sep means seprater function ==" "
print("misspyson") #end = "\n"

print("pyson",end = " ")
print("pyson")

  # qu == default peremeter = assigning a default value to parameter,which is used when no argument is passed..

def cal_prod(a = 3,b = 2):
     print(a*b)
     return a*b

cal_prod(1)

 # practice qu no 1 == waf to print the length of a list . (list is the parameter)

person = ["baburao","sachin","mamma","krishnaji","papa"]
village = ["kamari","prayagraz","junction","puner","bhadamai","komari"]

print(person[2], end=" ")
print(person[3], end="")

def print_len(list):
     print(len(list))

print_len(person)
print_len(village)

  # qu 2 ==  waf to print the elements of a list in a singal line. (list is the parameter)

cities = ["delhi","mumbai","gujrat","rajsthan"]

def print_len(list):
     print(len(list))

def print_list(list):
     for item in list:
        print(item, end=" ")
        print()
print_list(cities)

  # qu 3 == waf to find the factorial of n.(n is t parameter)

n = 5
fact = 1 
for i in range(1,n+1):
     fact*=i
print(fact)

  # waf to find the factorial of n . (n is the parameter)

def converter(usd_val):
     inr_val = usd_val * 87
     print(usd_val,"USD =", inr_val, "INR")

converter(1)

   # recursion 

def show(n):
     print(n)

show(5)

  # recursive function..

def show(n):
     if(n == 0):
          return
     print(n)
     show(n-1)

show(5) # 5, 4=n-1, 3= n-2, 2=n-3, 1

def show(n):
    if(n == 0): # base case
         return
    print(n)
    show(n-1)
    print("END")

show(3)

 # factorial 

def fact(n):
    if(n == 1 or n ==0):
         return 1
    return fact(n-1) * n

print(fact(5))

# practie que == write a recursive function to calculate te sum of first n naturel numbers..

def calc_sum(n):  
    if(n == 0):  # base case
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(9)
print(sum)

# que 2 == write a recursive function to print all elements in a list .. hint;list and index as parameters...

def print_list(list,ind):
     if(ind == len(list)):
         return
     print(list[ind])
     print_list(list,ind+1)

fruits = ["mango","litchi","apple","pineapple"]

print_list(fruits,0)
