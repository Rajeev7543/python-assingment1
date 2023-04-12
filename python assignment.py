#!/usr/bin/env python
# coding: utf-8

# ## Question 1.	Python program to add two numbers
# 
# 

# In[1]:


a=5
b=10
c=a+b
print("sum=",c)


# ## Question 2.Maximum of two numbers in Python
# 

# In[ ]:


def maximum(a, b):
     
    if a >= b:
        return a
    else:
        return b
     
# Driver code
a = 2
b = 4
print(maximum(a, b))


# ## Question 3.	Python Program for factorial of a number
# 

# In[ ]:


# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 7

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)


# ## 4.	Python Program for simple interest
# 

# In[ ]:


# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.
 
 
def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
    return si
     
# Driver code
simple_interest(8, 6, 8)


# ## 5.	Python Program for compound interest
# 

# In[ ]:


# Python3 program to find compound
# interest for given values.
  
  
def compound_interest(principal, rate, time):
  
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
  
  
# Driver Code
compound_interest(10000, 10.25, 5)


# ## 6.	Python Program to check Armstrong Number
# 

# In[ ]:


# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# ## 7.	Python Program for Program to find area of a circle
# 

# In[ ]:


# Python program to find Area of a circle using inbuild library
 
import math
def area(r):
 area = math.pi* pow(r,2)
 return print('Area of circle is:' ,area)
area(4)
 


# ## 8.	Python program to print all Prime numbers in an Interval
# 

# In[ ]:


# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# ## 9.	Python program to check whether a number is Prime or not
# 

# In[ ]:


num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# ## 10.	Python Program for n-th Fibonacci number
# 

# In[ ]:


# Function for nth Fibonacci number
 
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Driver Program
 
print(Fibonacci(10))
 


# ## 11.	Python Program for How to check if a given number is Fibonacci number?
# 

# In[ ]:


# python program to check if x is a perfect square
import math
 
# A utility function that returns true if x is perfect square
 
 
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
# Returns true if n is a Fibonacci Number, else false
 
 
def isFibonacci(n):
 
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
 
 
# A utility function to test above functions
for i in range(1, 11):
    if (isFibonacci(i) == True):
        print(i, "is a Fibonacci Number")
    else:
        print(i, "is a not Fibonacci Number ")


# ## 12.	Python Program for n\’th multiple of a number in Fibonacci Series
# 

# In[ ]:


# Python Program to find position of n\'th multiple
# of a number k in Fibonacci Series
 
def findPosition(k, n):
    f1 = 0
    f2 = 1
    i =2;
    while i!=0:
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
 
        if f2%k == 0:
            return n*i
 
        i+=1
         
    return
 
 
# Multiple no.
n = 5;
# Number of whose multiple we are finding
k = 4;
 
print("Position of n\'th multiple of k in"
                "Fibonacci Series is", findPosition(k,n));
 


# ## 13.	Program to print ASCII Value of a character
# 

# In[ ]:


# Python program to print 
# ASCII Value of Character
  
# In c we can assign different
# characters of which we want ASCII value 
  
c = 'g'
# print the ASCII value of assigned character in c
print("The ASCII value of '" + c + "' is", ord(c))


# ## 14.	Python Program for Sum of squares of first n natural numbers
# 

# In[ ]:


# Python3 Program to
# find sum of square
# of first n natural
# numbers
 
 
# Return the sum of
# square of first n
# natural numbers
 
def squaresum(n):
 
    # Iterate i from 1
    # and n finding
    # square of i and
    # add to sum.
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i * i)
 
    return sm
 
 
# Driven Program
n = 4
print(squaresum(n))
 


# ## 15.	Python Program for cube sum of first n natural numbers

# In[ ]:


# Python program to find the sum of the cubes of n numbers
# Take user input
n = int(input("Enter Number: "))

sum = 0
for i in range(n+1):
  sum += i**3
  
# Print Result
print("Sum of cubes of first {} natural numbers: ".format(n), sum)

