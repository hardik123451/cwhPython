f = open("file.txt")
print(f.read())
f.close()


# the same can be written line this.
with open("file.txt") as f:
    print(f.read())


# you dont have to explicitly close the file