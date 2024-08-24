a = int(input("Enter your age: "))

if(a>=18):
    print('you are an adult')
    print('Good for you')

elif(a<0):
    print("Write your correct age")

elif(a==0):
    print("Age cannot be 0 (zero)")

else:
    print("you are a kid")

print('End of program')