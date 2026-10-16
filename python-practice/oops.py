class Student:
    name = "pyson"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

  # new

class car:  #class
    color = "blue"
    brand = "mercedes"

car1 = car()  #object
print(car1.color)
print(car1.brand)

   # new

class student:

    name = "payal"
    def __init__(self):
        print("adding new student in database..")

s1 = student()
print(s1)

  # new

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new students in Database..")

s1 = Student("payal", 19)
print(s1.name, s1.marks) #payal

s2 = Student("sengar",22)
print(s2.name,s2.marks)

  #  new ..

class student:
    collage_name = "vit collage"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

  #new

class Student:
    collage_name = "abc collage"
    name = "anonymous"  #class attr

    def __init__(self,name,marks):
        self.name = name  #obj attr > class attr
        self.marks = marks
        print("adding new student in Database..")

s1 = student("payal",19)
print(s1.name)



