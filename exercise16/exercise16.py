
text_file=open('exercise16.txt')
content= text_file.read()
remove=content.replace(","," ").replace("-"," ").replace("*","")
count=remove.split(' ')
print(len(count))
replaced=remove.replace("is","should be")
print(replaced)
transform=replaced.upper()
print(transform)

text_file.close()