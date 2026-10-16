info = {
    "keys" : "value",
    "name" : "payal",
    "practice" : "python",
    "age" : "19",
    "is_adult" : "True",
    "marks" : "99.5",

    "subjects" : ["python","java","c++"],#list
    "topics" : ("dict","sets"), #tuple
    "33.22" : ("23.34") #floating value
}
print(info)
print(type(info))
print(info["age"])

null_dict = ()
print(null_dict)

info["name"] = "pyson" #overwrite
info["surname"] = "senagr"
print(info)

student = {
    "name" : "payal sengar",
    "subjects" : {
        "phy" : 89,
        "chem" : 98,
        "math" :65
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))

print(student.values())
print(list(student.values()))

print(student.items())
print(list(student.items()))
print(len(list(student.items())))

print(student["name"])
#print(student["name"])
print(student.get("name"))
print(student.get("name2")) # no error output none value

student.update({"city" : "delhi"})
print(student)

new_dict = {"vilaage" : "age"}
student.update(new_dict)
print(student)

#set in python

collection = {1,2,2,2,3,4,"hello","payal","hello","world"}
print(collection)
print(type(collection))
print(len(collection)) #total number of items

collection = set() # empty set ;syntax
print(collection)
print(type(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add("miss pyson")
collection.add((1,2,3))

collection.clear()

print(len(collection))

collection = {"hello","world","python","jaava"}

print(collection.pop())
print(collection.pop())

set1 = {1,2,3}
set2 = {3,2,5}

print(set1.union(set2)) #{1,2,3,4,5}
print(set1.intersection(set2))

  #pratice question  1 == store following word meaning in a python dictionary...  1  = table : "a piece of furniture ", "list of facts and figure"
# cat  : "a small animal"

dictionary = {
    "cat" :"a small animal",
    "table" : ["a piece of furniture", "list of facts & figure"]
}
print(dictionary)

  # que 2 == you are given a list for students . assume one classroom is required for 1 subjects . how many classroom are needed by all students

subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python","java", "c++", "c"
}
print(subjects)
print(len(subjects))

  #wap to enter of 3 subjects from the user and store them in a dictionary. start with an empty dictonary and add one by one . use subects name as key and marks as value..

marks = {}

x = int(input("enter phy :"))
marks.update({"phy" :x})

x = int(input("enter math :"))
marks.update({"math" :x})

x = int(input("enter chem :"))
marks.update({"chem" :x})

print(marks)

  #que 2 == figure out a way to store 9 & 9.0 as separate values in the set. (you can take help of built in data types)

values = {9,9.0}  
print(values)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)