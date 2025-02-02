contents = ["text A","text B","text C"]
filenames = ["a.txt","b.txt","c.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"/Users/juan/PycharmProjects/todolistapp/files/{filename}",'w')
    file.write(content)

countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

for content, country in zip(countries, countries):
    with open(f"/Users/juan/PycharmProjects/todolistapp/files/{country}.txt",'w') as file:
        file.write(content)