import shutil
shutil.copy('Text.txt', 'Text-copy.txt')
file=open("Text-copy.txt")
print(file.read())