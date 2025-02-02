contents = ["text A","text B","text C"]
filenames = ["a.txt","b.txt","c.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"/Users/juan/PycharmProjects/todolistapp/files/{filename}",'w')
    file.write(content)

