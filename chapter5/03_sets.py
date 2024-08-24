s = {8,2,2,4,5,5,6, 'hardik' }
e = set()   # this is used to make empty set

e.add("hardik")
e.add(2)

# print(s)
# print(type(e), e)

# print(len(s))
print(type(s) , s)
s.remove(5)
print(type(s) , s)

# s = {8,2,2,4,5,5,6, 'hardik' }    # written above already

s2 = {8,2 }

# print(s.symmetric_difference(s2))
print(s.issuperset(s2))






