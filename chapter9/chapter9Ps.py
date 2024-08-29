# q1  read file and find "twinkle" exists?
# f = open("poems.txt")
# content = f.read()
# if("Twinkle" in content):
#     print("Exists")
# else:
#     print("not exists")

# f.close() 


# q2 make game function and return score as an integer
# you need to read "Hi-score.txt" file may be blank 
# or contains previous Hi-score. and write new hi-score init

# import random

# def game():
#     yourScore = random.randint(1,62)

#     with open("Hi-score.txt") as f:
#         hiScore = f.read()

#     if(hiScore == ""):
#         hiScore = 0
#     else:
#         hiScore = int(hiScore)

#     print(hiScore, type(hiScore))

#     if(yourScore>hiScore):
#         with open("Hi-score.txt", "w") as f:
#             f.write(str(yourScore))
#         print("New Hi-Score, Congrats" ,yourScore)      
#     else:
#         print("You Lose", yourScore)

# game()







# # q3  generate multiply tables from 2 to 20 in different files

# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"
    
#     with open(f"tables/table_of_{n}.txt", "w") as f:
#         f.write(table)

# for i in range(2,21):
#     generateTable(i)



# # q4  a file contains Donkey multiple times , replace that word with '#####' by updating same file

# word = "donkey"
# with open("donkey.txt") as f:
#     content = f.read()

# contentNew = content.replace(word, "#####")

# with open("donkey.txt", "w") as f:
#     f.write(contentNew)



# #q5  same as q4 here a list of words will be censored

# words = ['donkey', 'bad', 'ganda']

# with open("donkey.txt") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "#"*len(word))

# with open("donkey.txt", "w") as f:
#     f.write(content)
    


# # q6   find word 'python' is present in log file ?

# with open("log.txt") as f:
#     content = f.read()

# if("python" in content):
#     print("present")
# else:
#     print("not present")



# # q7 find on which line no. word 'python' is present

# # line = 1
# # word = 'python'
# # with open("log.txt") as f:
# #     lines = f.readlines()
# #     countLines = len(lines)


# # for i in lines:
# #     if(word in i):
# #         print(i.index(word))   # my try failed

# with open("log.txt") as f:
#     lines = f.readlines()

# lineNo = 1
# for line in lines:
#     if('python' in line):
#         print("present", lineNo)
#         break
#     lineNo += 1 
# else:
#     print("not present in all lines")





# # q8 make duplicate file of this.txt file

# with open('this.txt') as f:
#     content = f.read()

# with open('this2.txt', 'w') as f:
#     f.write(content)



# # q9 check both files are identical and matches content of each other or not

# with open('this.txt') as f:
#     content = f.read()

# with open('this2.txt') as f:
#     content2 = f.read()

# if(content == content2):
#     print("yes, matched")
# else:
#     print("not matched")




# # q10 wipe out content of a file

# with open('this2.txt', 'w') as f:
#     f.write("")



# q11     rename file

with open('old.txt') as f:
    content = f.read()

with open('new.txt', 'w') as f:
    f.write(content)
