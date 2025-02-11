filenames = ["1.doc","1.presentation","1.report"]

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]

print(filenames)