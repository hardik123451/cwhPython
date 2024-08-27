print('hi')


# # a = int(input())
# # b = int(input())
# # c = int(input())
# # average = ( a + b + c)/3
# # print(average)

# def avg():
#     a = int(input("Enter your number: "))
#     b = int(input("Enter your number: "))
#     c = int(input("Enter your number: "))
#     average = ( a + b + c)/3
#     print(average)


# avg()
# avg()
# avg()
# avg()

# till 01 fundtions



# now 03 functions with argument

# def goodDay(name, ending):
#     print("hi "+ name)
#     print(ending)
#     return "done"

# a = goodDay("harry", "Thank you")
# print(a)


# def avg():
#     a = int(input("Enter your number: "))
#     b = int(input("Enter your number: "))
#     c = int(input("Enter your number: "))
#     average = ( a + b + c)/3
#     return average



# a = avg()
# print(a)





# # 04 default argument

# def goodDay(name, ending="thank you"):
#     print("hi "+ name)
#     print(ending)

# goodDay("hardik" )
# goodDay("rohan", "thax" )


# 05 recursions

# factorial(n) = n * factorial(n-1)

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("enter number "))
print(f"fatorial of your number {n} is {factorial(n)}")







































































































































