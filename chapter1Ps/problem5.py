import os


directory_path = '.'


contents = os.listdir(directory_path)

for entry in contents:
    print(entry)


