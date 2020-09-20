f_handler=open("./prueba.txt")
cont=0

for line in f_handler:
    cont+=1

print("There are "+str(cont)+" lines.")
