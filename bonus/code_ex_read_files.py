# Then, create a program that:
# 1. reads each text file and
# 2. prints out the content of each file in the command line.

filenames = ['a.txt', 'b.txt', 'c.txt']
content = []

for filename in filenames:
    with open(f"/Users/juan/PycharmProjects/todolistapp/files/{filename}",'r') as file:
        content = file.read().strip()
        print(content)
