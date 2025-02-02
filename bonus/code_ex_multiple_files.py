filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    with open(f"/Users/juan/PycharmProjects/todolistapp/files/{filename}",'w') as file:
        file.write("Hello")