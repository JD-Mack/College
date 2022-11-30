#1. write a program to create lambda function that returns a square value of a given
#number.
def myFunction():
	return lambda a:a*a
n=int(input("Enter a Number to return its Square: "))
myLambda=myFunction()
print("Square of Number: ",myLambda(n))

#2. A lambda function to calculate the sum of two numbers.
def myFunction():
	return lambda a,b:a+b
n=int(input("Enter first Number: "))
n1=int(input("Enter Second Number: "))
myLambda=myFunction()
print("Sum of two Numbers: ",myLambda(n,n1))


#3. A lambda funtion to find the bigger number in to two given numbers.
def myFunction():
	return lambda a,b:a if a>b else b
n=int(input("Enter first Number: "))
n1=int(input("Enter Second Number: "))
myLambda=myFunction()
print("Bigger Number: ",myLambda(n,n1))


#4. Write a python program using filter() to filter out even numbers from list.
def isEven(n):
	if n%2==0:
		return True
	else:
		return False

lst1=[1,2,3,4,5,6,7,8,9,10]
print("Even Numbers: ",filter(isEven,lst1))


#5. A lambda that returns even numbers from a list.
def isEven():
	return lambda lst1:True if lst1%2==0 else False 
lst1=[1,2,3,4,5,6,7,8,9,10]
myLambda=isEven()
print("Even Numbers using lambda: ",filter(myLambda,lst1))


#6. Write a python progran to find squares of elements in list. (MAP()
#FUNCTION)
def square(n):
	return n*n
lst1=[1,2,3,4,5,6,7,8,9,10]
print("Square Numbers using MapFunction: ",map(square,lst1))


#7. Write a lambda function that returns a squares of elements in a list. (MAP(),
#lambda)
def square():
	return lambda lst1:lst1*lst1
myLambda=square()
lst1=[1,2,3,4,5,6,7,8,9,10]
print("Square Numbers using MapFunction with Lambda: ",map(myLambda,lst1))


#8. write a program to find the products of elements of two different lists sing
#lambda function.
#Lst1=1,2,3,4,5
#lst2=10,20,30,40,50
def square():
	return lambda lst1,lst2:lst1*lst2
myLambda=square()
lst1=[1,2,3,4,5,6,7,8,9,10]
lst2=[1,2,3,4,5,6,7,8,9,10]
print("The products of elements of two different lists: ",map(myLambda,lst1,lst2))


#9. To calculate the sum of numbers from 1 to 50, write reduce() function with a
#lambda.
#OUTPUT: 1275
def sum():
	return lambda n1,n2:n1+n2
myLambda=sum()
lst1=[]
for i in range(1,51):
	lst1.append(i)

print("The sum of numbers from 1 to 50: ",reduce(myLambda,lst1))



#FILE:

#1. write a python program to create a text file to store individual characters.
f=open("/Users/exam/Desktop/Anis.txt","w")
f.write("Anis Mansuri Hanifbhai")
print("File Created!")
f.close()


#2. write a python program to read first 5 bytes from a text file.
f=open("/Users/exam/Desktop/Anis.txt","r")
print(f.read(5))
f.close()

#3. Write a python program to store a group of strings into a text file.
f=open("/Users/exam/Desktop/Mansuri.txt","w")
f.write("Anis Mansuri Hanifbhai")
print("File Created!")
f.close()


#4. A python program to read all the strings from text file and display them.
f=open("/Users/exam/Desktop/Anis.txt","r")
print("Data of text file: ",f.read())
f.close()

#5. A python program to apprend data to an existing file and then display the entire file data.
f=open("/Users/exam/Desktop/Mansuri.txt","a+")
f.write("Anis Mansuri Hanifbhai")
print(f.tell())
f.seek(0,0)
a=f.read()
print(a)
f.close()


#6. A python program to know wheather the file exists or not.
#f=open("/Users/exam/Desktop/Mansuri.txt","r")
#print(f.read())
import os
booll=os.path.isfile("/Users/exam/Desktop/Mansuri.txt")
if(booll):
	print("File Exist")
else:
	print("File does not Exist")


#7. A python program to count number of lines, words and characters in a text file.
f=open("/Users/exam/Desktop/2darray.c","r")
a=f.read()
line=0
words=0
char=0
for i in a:
	if i==' ':
		words+=1
	elif i=='\n':
		line+=1
	char+=1
print("No. of Lines: ",line)
print("No. of Words: ",words)
print("No. of Character: ",char)


#8. A python program to copy an image file into another file.
f=open("/Users/exam/Desktop/Aerial01.jpg","rb")
a=f.read()
f.close()
f=open("/Users/exam/Desktop/Anis.jpg","wb")
f.write(a)
f.close()

#9. A python program ti use with to open a file and write some string into file.
with open("/Users/exam/Desktop/Anis.txt","w") as File:
	File.write("Hello")

#10. A python program ti use with to open a file and read data from it.
with open("/Users/exam/Desktop/Anis.txt","r") as File:
	a=File.read()
print("Read using with function: ",a)
""""
f=open("/Users/exam/Desktop/2darray.c","r+")
print(len(f.read()))	
f.write("Hello")
f=open("/Users/exam/Desktop/2darray.c","r+")
print(len(f.read()))"""