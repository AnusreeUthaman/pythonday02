#Logical operators

#and
print(5>2 and 5==5)
print(5>2 and 4==5)
print(5>10 and 5==5)
print(5>10 and 5!=5)

#or
print(5>2 or 5==5)
print(5>2 or 4==5)
print(5>10 or 5==5)
print(5>10 or 5!=5)

#not
print(not 5>2)
print(not 4==5)
print(not 5>10)
print(not 5!=10)

#concatenation(str+str)

print("hello"+"world")
print("hello "+"world")

#string multiplies(str*int)
print("hello"*5)

#variables
#variables are used to store and manipulate data
#container that holds a value

x="codeme"
print(x)

username="Anusree"
print(username)

rollno=12
print(rollno)

x=10
y=20
print(x+y)
print(x*y)
print(x/y)
print(x-y)


#Dynamic typed programming language-
#while creating a variable we donot need to declare its datatype
a=10
a="hello"
print(a)


#Escape sequence
print("hello \nworld")
print("hello \tworld")
print('i\'m 20 years old')
print("my name is \"Anusree\"")

#swapping

# method 1
a=10
b=5
temp=a
b=a
a=temp
print(a)
print(b)

# method 2

a=10
b=5
a,b=b,a
print(a)
print(b)

a=10
b=5
c=15
a,b,c=b,c,a
print(a)
print(b)
print(c)
    
#type casting
x="12.3"
y=float(x)
print(type(y))
print(y*10)
print(x*2)

x="144"
z=int(x)
print(z)

a=145
b=15.15
c=True
x=str(a)
y=str(b)
z=str(c)
print(x)
print(y)
print(z)

#inplace operators:
+=-addition
-=-subtraction
/=-division
*=-multiplication
//=-floor divsion
**=-exponentiation
%=-modulus
 

a=10
a+=15
print(a)

 

