# find greatest number among 3 numbers using functions

# n1 = int(input())
# n2 = int(input())
# n3 = int(input())

# def mx(a, b, c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
    
# x = mx(n1,n2,n3)

# print(x)





# # q2  convert celsius to fahrenheit using function

# cels = float(input("cels: "))

# def convertCelsiusToFahrenheit(c):
#     fahr = ((9/5 * c) +32)
#     return fahr

# fah = convertCelsiusToFahrenheit(cels)
# print(f"{round(fah)}\u00B0 F")



# # q3 how python prevents print function to print new line at the end 

# a = 1
# b = 2
# c =3
# d = 4
# print(a,end="")
# print(b,end="")
# print(c,end="")
# print(d,end="")



# # q4  write a recursive function to calculate sum of n natural numbers

# n = int(input("enter number : "))

# def recuSum(num):
#     if(num==1 ):
#         return 1
#     elif(num==0):
#         return 0
#     return num + recuSum(num-1) 

# a = recuSum(n)
# print(a)






# # q5 python function for star pattern
# ***
# **
# *      n=3

# n = int(input("enter number: "))

# def starPatt(num):
#     if(num == 0):
#         return
#     print("*"*num)
#     starPatt(num-1)

# starPatt(n)                 # using recursion function

# for i in range(0, n):
#     if(n==0):
#         break
#     print("*"*(n-i))            # using loop
    







# # q6  python function to convert inches to cm

# n = int(input())
# def inchesToCm(num):
#     return num*2.54

# a = inchesToCm(n)
# print(f"{a} cm")




# q7   python function  to remove given word from list and strip it at same time

# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))        

#     return n

# def rem(l, word):
#     l.remove(word)
#     n =[]
#     for i in l:
#         i = i.strip(word)
#         # print(i, word)
#         n.append(i)
#     return n

# l = ["hardik", "harry", "amrit", "munnha", "bhaiya", "ha"]
# print(rem(l, "ha"))




# q8 print multiplication table of given n number

def mTable(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i} ")

inp = int(input())
mTable(inp)








































