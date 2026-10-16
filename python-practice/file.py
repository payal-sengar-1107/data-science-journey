f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

# practice

f = open("demo.txt", "r")
data = f.read(6)
print(data)
print(type(data))
f.close()

# practice

f = open("demo.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

# pratice

f = open("demo.txt", "w")

f.write("then I'll move to reactJS")

f.close()

  # practice

f = open("sample.txt", "w")
f.close()

  # new

f = open("demo.txt", "r+")
print(f.read())
f.write("abc")
f.close()

  # new practice

with open("demo.txt", "r")as f:
    data = f.read()
    print(data)

  # deletin a file

import os

os.remove("sample.txt")