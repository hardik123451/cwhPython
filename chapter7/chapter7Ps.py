
# gNumber = int(input())

# i=1
# while(i<=10):
#     print(f"{gNumber} x {i} = {gNumber*i}")
#     i += 1
#   # q1    and q3



# l = ["Harry", "Soham", 'Sachin', 'Rahul']

# # for i in l:
# #     for j in i:
# #         if(j[0] == "R"):
# #             print(f"Hi {i}")   # my answer


# for name in l:
#     if(name.startswith("S")):
#         print(f"Hi {name}")    # harry answer
# q2



# find prime number   

# n = int(input())

# for i in range(2, n):
#     if(n%i == 0):
#         print('not', n , i)
#         break
# else:
#     print("prime")     #q4

# i = 2
# while(i < n):
#     if(n%i== 0):
#         print("not")
#         break
#     i += 1 
# else:
#     print("prime")   #q4



# sum first n natural numbers with while loop

# n = int(input())

# i=1
# s = 0
# while(i <= n):
#     s = s + i
#     if(i == n):
#         print(s)
#         break
#     i += 1
# else:
#     print("nnnn")       #q5



# # find factorial of given number using for loop
# # 5! = 1 x 2 x 3 x 4 x 5

# n = int(input())
# facto = 1
# for i in range(1, n+1):
#     facto = facto * i

# print(facto)      #q6





# # print star pattern    q7
# #   *
# #  ***
# # ***** for n = 3
# n = int(input())
# for i in range(1 , n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1))


# # q8 print star pattern
# # *
# # **
# # ***
# n = int(input())
# for i in range(1,n+1):
#     print("*"*i)




# # q9  print star pattern
# # * * *
# # *   *
# # * * *

# n = int(input())

# for i in range(1, n+1):
#     if(i == 1 or i == n):
#         print("*"*n)
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*")



# q10    multiplication table of n number

n = int(input())

# i = 10
# while(i>0):
#     print(f"{n} X {i} = {n*i}")
#     i = i - 1

for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")













































































