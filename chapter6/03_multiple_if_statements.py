

a = int(input("Enter your age: "))

# if statement no 1
if(a%2 == 0):
    print("a is even")

# if statement no 2
if(a>=18):
    print('you are an adult')
    print('Good for you')

elif(a<0):
    print("Write your correct age")

elif(a==0):
    print("Age cannot be 0 (zero)")

else:
    print("you are a minor")

print('End of program')