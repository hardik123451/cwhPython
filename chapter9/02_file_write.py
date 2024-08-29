st = "hey hardik , how are you today!"

f = open("file.txt", "w")
f.write(st)
f = open("file.txt", "r")

data2 = f.read()

print(data2)
f.close()
