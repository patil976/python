#create a file
'''file=open("example.txt","w")
file.write("Welcome to the python\n")
file.write("pyhton is very easy languiage ")
file.close()'''


#read a file
'''file=open("example.txt","r")
content=file.read()
print(content)
file.close()'''

#  Append Data to a File
'''file = open("example.txt", "a")
file.write("\nThis line is appended.")
file.close()
print("Data appended successfully.")'''


#read and write
'''file= open("example.txt", "r+")
print(file.read())
file.write("\nHello")
file.close()'''

#write and read
'''file = open("example.txt", "w+")
file.write("Hello World")
file.seek(0)
print(file.read())
file.close()'''


#Append and read 
'''file = open("example.txt", "a+")
file.write("\nHello")
file.seek(0)
print(file.read())
file.close()'''

#for reading the content from file
#read()
'''file = open("example.txt", "r")
print(file.read())
file.close()'''

#readline()
'''file= open("example.txt", "r")
print(file.readline())
print(file.readline())
file.close()'''

#readlines()
'''file = open("example.txt", "r")
lines = file.readlines()
print(lines)
file.close()'''

#x 
'''file = open("dev.txt","x")
file.write("Hello")
file.close()'''










