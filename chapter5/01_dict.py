marks = {
    "hardik" : 100,
    "shubham": 45,
    "rohan" : 23,
    "list" : [1,2,9]
}

print (marks, type(marks))
print (marks["hardik"])
print (marks["list"])



# 02_dict_methods

marks = {
    "hardik" : 100,
    "shubham": 45,
    "rohan" : 23,
    "list" : [1,2,9],
    0: 'harry'

}


# print(marks.values())

marks.update({"hardik": 99})

print(marks)