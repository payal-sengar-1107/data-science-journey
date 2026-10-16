marks = [22.3,33.2,43.2,33.6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[3])

payson = ["css student",19,"khitauli"]
print(payson)
print(payson[2])
payson[2] = "komari"
print(payson)

#list slicing = ending index is does not included

marks = [82,84,99,98,65]
print(marks[1:4])
print(marks[:3])
print(marks[0:])
print(marks[-3:-1])

#list method..

list = [2,1,3]
list.append(4)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)
list.reverse()#pehle list ko ulta
print(list)#ab badli hui list
list.insert(2,5)#pahle index 2 par 5 insert karein
print(list)#ab final updated list ko print karein
list.remove(3)
print(list)
list.pop(1)
print(list)


list = ["banana","litchi","apple"]
list.sort(reverse=True)
print(list)

#tuples in python

tup = (2,1,3,1)
print(type(tup))
print(tup[0])
print(tup[3])

tup = ()
print(tup)
print(type[tup])

tup = (1,2,3,4,)
print(tup.index(2))

tup = (1,3,2,4,5,2,3,2)
print(tup.count(2))

# prctice question = WAP to ask te user to enters names of their 3 favorite movies and store them in a  list..

movies =[]
mov1 = input("enter 1st movie:")
mov2 = input("enter 2nd movie:")
mov3 = input("enter 3rd movie")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# question 2 ==WAP to cheak if a list contains a palindrome of elements .(hints :use copy( method))

#(1,2,3,2,1) [1,"abc","abc",1 ]means understand palindrome doing reverse value same exact value given

list1 = [1,2,1]
list2 = [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")

# question 3 == WAP to count th enumber of students with thhe "a" grade in the following touple..["c","D","A","A","B","B","A"]

grade = ("C","D","A","A","B","B","A")
print(grade.count('A'))

#question 3 == store te above value in a list and sort them from "a" to "b"...

grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)