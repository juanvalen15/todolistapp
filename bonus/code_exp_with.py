with open("../files/doc.txt") as file:
    print(file.read())

# The idea of this experiment was to show:
# 1. open handles the closure of file
# 2. open by default uses the read parameter