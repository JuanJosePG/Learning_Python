f_handler=open("Scripts\prueba.txt")

for line in f_handler:
    if line.startswith("de"):
        print(line)


# There is a problem:
#  - each line from the file has a newline (\n) at the end
#  - the print statement adds a newline to each line

# NEW VERSION FIXED:

print("Fixed version\n")
f_handler_2=open("Scripts\prueba.txt")
for line in f_handler_2:
    line=line.rstrip()
    if line.startswith("de"):
        print(line)

# .rstrip() removes any white space at the end of the string


print("We are going to look for something specific in a file and it will show us the line")
f_handler_3=open("Scripts\prueba.txt")
cont=0
for line in f_handler_3:
    cont+=1
    line=line.strip()
    if not "@gmail.com" in line:
        continue
    print("It's in the line number "+str(cont))
    print(line)
