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

import random

def game():
    return random.randint(1, 62)

currScore = game()
print(currScore)
f = open("Hi-score.txt")

hi = f.read()
if(hi==""):
    hi = 0
else:
    hi = int(hi)

f.close()

if(hi < currScore):
    f = open("Hi-score.txt","w")
    f.write(str(currScore))
    f.close()
    print("you win", currScore, hi)
else:
    print("you lose", currScore, hi )


f.close()