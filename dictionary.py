import functools
#hii welcome sukumar

# a = {'1':2, '2':'edwin','5':4,'4':'vicky'}
# print(a)
# b = a['1']
# print(b)
# c = a.keys()
# print(c)
# d = a.values()
# print(d)
# a['1']=3
# print(a.items())
# if '1' in a:
#     print('yes it is present')

# a['key'] = 'value'
# print(a)
# b = a.items()
# print(b)
# a.update({'5':'rock'})
# print(a)

# c = a.pop('1')
# print(a)
# del a['3']
# print(a)

# for i in a:
#     print(a[i])

# for i in a.values():
#     print(i)

# b = dict(a)
# print(b)
#
# c = {'3':5,'5':6}
# d = {'2':8,'5':8}
# e = {'c':c,'d':d}
# print(e)


# To sort (ascending and descending) a dictionary by value

a = { '1': 2, '2':5, '3':3, '4':7}
# b = []
# for x in a.values():
#     b.append(x)
# print(b)
# b.sort()
# print(b)
#
# for x in a.values():
#     print(x)

# d = {'car': 30, 'plane': 100, 'train': 40, 'doll': 90}
# a = input('enter you toy to boy')
# for i,j in d.items():
#     if a == i:
#         print(i)

# take a list any value find out the second largest value

# list1 = [45, 35, 54, 60]
# list1.sort()
# print(list1)
# print(list1[-2])

# take my name and find out the each character

# name = {"nam": "edwin"}
#
# each_character = name["nam"]
#
# print(each_character)
# # i = 0
# for i in each_character:
# #     print(each_character)
#
# # nested if else1
#
# percentage = eval("enter your percentage")
#
# if percentage < 0 and percentage > 100:
#     print("percentage you have entered is not valid")
#     if percentage >= 35:
#         print("just pass")
#     elif percentage <= 50:
#         print("second class")
#
#     elif percentage >=75:
#         print("first class")
# else:
#     print("you are fail")
#
# x = y = z = e = 10
# print(y)

# Take two int values from user and print greatest among them.

# A python program to accept a string from keyboard and display it.
# a = input('enter anything')
# print(a)
# a python program to accept a character as a string
# a = input("enter anything ")
# print("YYYH:"+a)

# # PYTHON PROGRAM TO ACCEPT A SINGLE CHARACTER FROM  KEYBOARD
# a = input("enter a single character ")
# print(a[0])

# a python program to accept an integer number from keyboard
#
# # a python program to accept two numbers and find their sum
# a = int(input('first integer '))
# b = int(input('second integer '))
# print("the value of a and b ", a + b)
# # print(f"the value of {a} and {b}", a + b)
#
# # a python program to find sum and product of two numbers.
# a = int(input('first integer ')),
# b = int(input('second integer '))
# print('the sum of {2} and {0} is {1}'.format(a, b, a * b))

# write a python program to accept 3 integers in same line and give output
# var1, var2, var3 = [int(x) for x in input(" enter three numbers ").split('+')]
# print('sum', var1+var2+var3)

# write a program to evaluating an expression entered from keyboard

# a = eval(input('enter an expression :'))
# print("%s"%a)
#
# a = 1
# if a == 1:
#     print("one")

# write a program to display a group of message when the condition is true

# a = "edwin is good boy"
# b = a
# if a == b:
#     print(a)
#     print('subash is a bad boy')

# a = 'subash'
# b = 'edwin'
# c = a
# a = b
# b = c
# print(a)
# print(b)

# a = 1234567
# print(str(a)[::-1])
#

# a python program to test whether a given number is in between 1 and 10

# b = int(input("enter any number 1 and 10 "))
# if b > 0 and b <= 10 :
#     print("entered number is between 1 and 10")
# else:
#     print("it is not present")

# a python program to know if a given number is zero, positive or negative.
# a = int(input('enter any number '))
# if a < 0:
#     print('it is negative number')
# elif a > 0:
#     print('it is positive number')
# else:
#     print("it is equal")

# write a program to reverse a string in program
# a = "edwin"
# print(a[::-1])

# Write a program to count the number of letters in a word.
# a = "pythonlobby"
# print(len(a))

# write We are given a string and we need to reverse words of a given string
# a = " geeks quiz practice code"
# b = a.split()[::-1]
# l =[]
# for i in b:
#     l.append(i)
# print(l)
# print(" ".join(l))


# l1 = [2, 5, 4, 9, -2]
# for i in range(len(l1)):
#     print(i)
#     for j in range(0,len(l1)):
#         print(j)
#         if l1[i]<l1[j]:
#             l1[i],l1[j] = l1[j],l1[i]
# print(l1)




# a = int(input('enter a number to multiply'))
# for i in range(1,11):
#     print(i ," *", a , " =", i * a)
#
#
# count = 0
# for i in range(1,11):
#     if i % 2 == 0:
#         print(i,end=" ")
#         count = count + i
# print(count)

# val  = 0
# a = int(input('enter a number'))
# for i in range(1,100):
#     if  a % i == 0 :
#         val+=1
# if val == 2:
#     print('it is prime number')
# else:
#     print('it is not prime number')

#
# a = input('enter the palindrome name to check')
# b = ""
# striplen = len(a)
# for i in range(striplen):
#     b = b + a[striplen-1]
#     striplen = striplen - 1
# print(b)
# if b == a:
#     print('it is palindrome')
# else:
#     print('it is not palindrome')
#
#
# lt = [1,2,3,4]
#
# print(a)

# def factorial(a):
#     x=1
#     for i in range(a,0,-1):
#          x=x*i
#     print(x)
# factorial(5)
#
# def multiply(b):
#     d = 0
#     for i in str(b):
#         d = d + int(i)
#     print(d)
# multiply(265)
#
# def prime(a):
#     for i in range(2,a):
#         if a % i == 0:
#             print('it is not prime number')
#             break
#     else:
#         print('it is prime number')
#
#
# prime
#
#
# a = [1,4,8,9]
# a1=[]
# for i in range(len(a)):
#     if i>0:
#         m=a[i]+a[i-1]
#         a1.append(m)
#     else:
#         a1.append(a[i])
# print(a1)

# a = [12562, 6744, 21498, 34]
# b = []
# for i in a:
#     c=0
#     for j in str(i):
#         c=c+int(j)
#
#     b.append(c)
# print(b)

# str1 = 'aaaabbbccccc'
# a ={}
# for i in str1:
#     a[i] = str1.count(i)
# s=''
# for i,j in a.items():
#     s+=i
#     s+=str(j)
# print(s)
#
# l2 = [1, 2, 3 , 5]
# l4 = [4, 6, 7, 8]
# d = {}
# for i in range(len(l2)):
#    for j in range(len(l4)):
#        if i == j:
#            d[l2[i]] = l4[j]
# print(d)
#
# l2 = [1,2,3,4]
# l3 = [2,3,4,5]
# l4 = [3,4,5,6]
# l5 = []
# d = {}
# for i in range(len(l2)):
#     for j in range(len(l3)):
#         if i == j:
#             x = l2[i] + l3[j]
#             l5.append(x)
# print(l5)
# for i in range(len(l4)):
#     for j in range(len(l5)):
#         if i == j:
#             d[l4[i]] = l5[j]
# print(d)
#
# d = {3: 3, 4: 10, 5: 7, 6: 9}
# c = list(d.values())
# print(list(c))
# count = []
# for i in range(len(c)):
#     for j in range(len(c)):
#         if i == j:

# for i in range(1,101):
#     if (i**0.5).is_integer():
#         print(i)
#
#
# str1 = 'aaaabbbccccc'
# a ={}
# for i in str1:
#     a[i] = str1.count(i)
# print(a)
# s=''
# for i,j in a.items():
#     s+=i
#     s+=str(j)
# print(s)

#

# x = lambda a,b : a + b
# print(x(10,20))

# import functools
# a = [1,2,3,4,8,10]
# b = (functools.reduce((lambda i,j: i+j ),a))
# print(b)

# dict1 = {'a':1,'b':2,'c':3,'d':4}
# a = list(dict1.values())
# print(a)
# b = []
# for i in a:
#     print(i)
#     c = 0
#     for j in range(i):
#         c+=i
# b.append(c)
# print(b)

# e = 'vn2 solution'
# d = e + 's'
# print(d)



# list1 = [1,3,'a',5,'7','data']
# a = [i for i in list1 type(i)]
# print(a)
# #
#
#
# a = {'1': 'edwin', '2': 'rajavelu', '3': 'karthi', '4':4}
# b = a.values()
# for i in b:
#     print(type(i))

# To sort (ascending and descending) a dictionary by value
# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# b = list(a.values())
# print(b)
# for i in range(len(b)):
#     for j in range(len(b)):
#         if b[i]<b[j]:
#             b[i],b[j] = b[j],b[i]
#
# print(b)

# Add a key to a dictionary
# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# # a[8] = 'edwin'
# # print(a)

# #Check if a given key already exists in a dictionary.
# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# b = eval(input('enter to check whether entered i present in dictionary a or not'))
# c = list(a.keys())
# print(c)
# for i in c:
#     if int(i) == b:
#         print('the key is present')
#         break
#     else:
#         print('key is not present')
#         break


# Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
# a = {}
# for x in range(1,10):
#     a[x] = x*x
# print(a)

# Print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
# a = {}
# for i in range(1,16):
#     a[i] = i * i
# print(a)

# Merge two Python dictionaries
# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# b = {'1': 6, '2': 5, '3': 1, '4': 4,'5':3}

# c = b.copy()
# c.update(a)
# # print(c)
# print({**a, **b})
# a.update(b)
# print(a)
# #
# x= {}
# for i in a.keys():
#     x[i] = a[i]
# for i in b.keys():
#     x[i] = b[i]
# print(x)

# a = 'vn2 solution pvt ltd'
# b = input('to change the string')
# d = input('change to ')
# c = a.split()
# for i in c:
#     if i == b:
#         a.replace('i','d')
# print(' '.join(c))

#Sum all the items in a dictionary
# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# c = []
# d = []
# e = 0
# f = 0
# b = {}
# for i,j in a.items():
#     c.append(int(i))
#     d.append(int(j))
# for i in c:
#     e+=i
# for j in d:
#     f+=j
#
# b[e]=f
# print(b)

# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# c = []
# for i,j in a.items():
#     c.append(sum(int(i),sum(int(j))))
# print(c)

# # multiply all items in dictionary
# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# for i,j in a.items():


# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# b = {}
# b[sum([int(i) for i in a.keys()])] =  sum(a.values())
# print(b)

from operator import*
#
# from functools import reduce
# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# b = {}
# c = [reduce(lambda x,y: x*y in a.keys())]= reduce(lambda x,y : x*y ,a.values())
# print(c)

# Map two lists into a dictionary
# a = [1,2,3,4]
# b = [2,3,5,7]
# c = dict(zip(a,b))
# print(c)

# Find the highest 3 values in a dictionary.
# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# c =[]
# d = {}
# for i in a.values():
#     print(i)
#     c.append(i)
# print(c)
# c.sort(reverse=True)
# b = c[0:3]
# print(b)
# for i in b:
#     if i == a.values():
#         d[]


# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# b =a.copy()
# print(b)

# a = {'1': 6, '2': 5, '3': 1, '4': 4}
# # b = 4
# # # c = dict.fromkeys(a,b)
# # # print(c)
# # a.popitem()
# a.setdefault('5',4)
# print(a)

a