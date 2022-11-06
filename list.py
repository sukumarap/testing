# sum of two elements
# a = [1, 2, 6, 8]
# b = [2, 3, 4, 9]
# c = [3, 5, 7, 10]
#
# d = []
# # print(sum(c))
# # print(sum(a))
# for i in range(len(a)):
#     for j in range(len(b)):
#         for k in range(len(c)):
#             if i == j == k:
#                 e = a[i]+b[j]+c[k]
#                 d.append(e)
#
# print(d)

# Finding a second largest number
# a = [1, 3, 5, 8]
# b = ""
# for i in a:
#     b=str(i)+b
# print(b)
# l=[]
# for i in b:
#     l.append(int(i))
# print(l)
# l.sort(reverse=True)
# print(l[1])
#

# Get unique values
# a = [1, 1, 3, 2, 2, 4, 4, 5, 6]
# for i in a:
#     if a.count(i)<=1:
#         print(i)

# Frequency of elements
# a = [1, 1, 3, 2, 2, 4, 4, 5, 6]
# d = {}
# for i in a:
#     d[i] = a.count(i)
# print(d)

# Mulitply of elements
# a = [1, 2, 6, 8]
# b = [2, 3, 4, 9]
# c = []
# for i in range(len(a)):
#     for j in range(len(b)):
#         if i == j:
#             x = a[int(i)] * b[int(j)]
#             c.append(x)
# print(c)


#Largest number from list

# a = [1, 2, 6, 8]
# print(max(a))

# Count no of strings whose length is 2
# a = ' edwin is very good boy'
# b = a.split()
# print(b)
# for i in b:
#     if len(str(i)) == 2:
#         print(i)

# Sort elements in increasing order

# Check list is empty or not

# Words that are longer than any element
# a = [1,4,'edwin','fyj','dcukdhffg']
# for i in a:
#     if
#

# Find common element from 2 lists

# a = [1, 2, 6, 8]
# b = [2, 3, 4, 9]
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             print(a[i])

# Remove specified index from list and print
# a = [1, 2, 6, 8]
# a.pop(1)
# a.remove(6)
# print(a)

# Remove even elements and print list
# a = [1, 3, 5, 8, 9]
# b = []
# for i in a:
#     if i % 2 != 0:
#         print(i)
#         b.append(i)
# print(b)

# Shuffle list and print
#
# a = [1,7,5,4,8]
# for i in range(len(a)):
#     for j in range(len(a)):
#         a[i],a[j]=a[j],a[i]
# print(a)

# from random import shuffle
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# shuffle(color)
# print(color)

# To access index of list
# a = [1, 3, 5, 8]
# b = a.index(3)
# print(b)

# List of characters into string
# a = [1, 2, 3, 'a', 'b', 'c']
# b = ''
# for i in a:
#     if str(i).isalpha():
#         b = b + i
# print(b)
# str(a)
# print(a)

#Append a list to second list
# a= [1,2,3]
# b = [ 2,3,4]
# b.extend(a)
# print(b)

# find the second smallest number
# a = [1, 2, 5, 6, 3]
# a.sort()
# print(a[1])


# a = [1, 2, 3 ,[1, 2, 3],[2, 3, 4]]
# for i in a:
#     if type(i)==list:
#         print(i)
#
# a = [ 1, 2, 3, 4, 5]
# str1 = ""
# for i in a:
#     str1 += str(i)
# print(str1)
# print(int(str1))


# def dict1:
#
#     dict1 = {'1':'0', '2':'0','3':'0','4':'0'}
#
#     a = dict1.keys()
#     print(a)


#
# l1=[]
# for i in range(1,10):
#     l1.append(i)
# print(l1)

l2= []
# for i in range(1,10):
#     for j in range(1,10):
#         if i == j:
#             x = i + j
#             l2.append(x)
# print(l2)


# l2 = [1, 2, 3, 4]
# l3 = []
# for i in l2:
#     count = 0
#     for j in range(0,i):
#         count+=i
#     l3.append(count)
# print(l3)





# Sum of elements
# a = [1, 9, 2, 4, 3, 8]
# c = []
# p = []
# for i in range(len(a)):
#     if i > 0:
#         d = a[i]+a[i]
#         c.append(d)
#     else:
#         e = a[i]
#         c.append(e)
# print(c)

from functools import reduce
# Mulitply of elements
# a = [1, 9, 2, 4, 3, 8]
# res = 1
# b = []
# for i in a:
#     res *= i
#     b.append(res)
# print(b)
# print(reduce(lambda x,y: x*y,a))


#
# # largest number from list
# a = [1, 9, 2, 4, 3, 8]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i] == a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)

# Variable unique identification number
# a = [1, 9, 2, 4, 3, 8,'edwin']
# for i in a:
#     print(type(i))

#Finding common items from two lists

# a = [1, 9, 2, 4, 3, 8]
# b = [1, 7, 6, 5]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             print(i)

# Change the position of e
# very nth value with (n+1)th value
# a = [1, 9, 2, 4, 3, 8]
# print([(i+i) for i in a])


# Converting multiple integers into single integer
# from functools import reduce
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# c = reduce(lambda i,j : i * j,b)
# print(c)

# # Split a list based on first character of word
# a = ['edwin', 'ram', 'lucky' ,'terminal']
# a.sort(key= lambda i:i[1])
# c = []
# for i in a:
#     b = i[1]
#     print(b)
#
# print(c)

# create multiple list
# a = []
# for i in range(10,1,-2):
#     a.append(i)
# print(a)


# Find missing and additional values
# a = [1, 2, 3, 5, 8]
# b = [5, 7, 9, 10, 11]
# a.extend(b)
# print(a)
# for i in a:
#     if














