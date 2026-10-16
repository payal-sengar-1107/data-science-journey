count = 1 
while count <= 5 :
    print("radhe radhe")
    count += 1

print(count)

i = 1
while i <= 5:
    print("hello")
    i+=1

i=1
while i <= 5:
    print(i)
    i+=1

print("loop ended")

  # question 1 == print number from 1 to 100

i=1
while i <= 100:
    print(i)
    i+=1

  #question 2 == print te numbers from 100 to 1..

i=100
while i >= 1:
    print(i)
    i-=1

  #question 3 == print multiplicatiom table of a number n ..

n = int(input("enter number : "))
i=1
while i <= 10:
    print(n*i)
    i+=1

  #question 4 == print te elements of the following list of a number..

nums = [1,4,9,16,25,36,49,64,81,100]

 #traverse 
ind = 0
while ind < len(nums):
    print(nums[ind]) # nums[0],nums[1],nums[2]
    ind += 1

  # question 4  ==  search for a number x in this tuple using loop ..

nums = (1,4,9,16,25,36,49,64,81,100,36)

x = 36

i=0
while i<len(nums):
    if(nums[i] == x):
        print("FOUND at idx , i")
    else:
        print("finding..") 
    i+=1    

  #new problem

i=1
while i <= 5:
    if(i==3):
        i+=1
        continue  #skip
    print(i)
    i += 1

  # new problem

i=1
while i <= 10:
    if(i%2 == 0):
        i+=1
        continue
    print(i)
    i+=1

 #new problem

colours = ["black","white","pink"]

for val in colours:
    print(val)

# work on touples

tup = (1,2,6,5,8,9,3)

for num in tup:
    print(num)

# work on string

str = "apnacollage"

for char in str:
    if(char == "o"):
        print("o found")
        break
    print(char)
else:
    print("END")

    #pratice question 1 = print the elements of the following list using a loop.

nums = [1,4,9,16,25,36,49,64,81,100,49]
x = 49
idx = 0
for el in nums:
    if(el == x):
        print("number found at idx",idx)
    idx += 1   

  #range..

for i in range(10): #range (stop)
    print(i)

for i in range(2,10): #range(start,stop)
    print(i)

for i in range(2,10,2): # range(start, stop, step)
    print(i)

# question 3 == print numbers from 1 to 100

for i in range (100,0,-1):
    print(i)

#question 4 == print number 100 to 1

for i in range(1,101):
    print(i)

 # question 4 ==  print the multiplication table of a number n ..

n = int(input("enter number :"))

for i in range(1,11):
    print(n*i)

# ques == wap to find te sum of first n numbers , (using while)

n = 5

for i in range(1,n+1):
    print(i)

n = 5 
sum = 0
i = 1
while i <= n:
    sum += i
    i+=1

print("total sum =", sum)

#que  ==  wap to find the sum of factorial of first n number ,(using for)

n = 5
fact =1

for i in range(1,n+1):
    fact *= i

print("factorial = ", fact)


