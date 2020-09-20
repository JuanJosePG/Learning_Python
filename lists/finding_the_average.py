def average_loop():
    cont=0
    sum=0
    print('Before: ',cont,sum)
    for i in [9,41,12,3,74,15]:
        cont+=1
        sum+=i
        print('Cont:',cont, 'New value:',i,'Sum:',sum)
    print('Average: ',sum/cont)

average_loop()
