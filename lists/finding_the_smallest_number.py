def search_min():
    minimum = None
    cont = 0
    print('Before: ', minimum)

    for i in [3,41,12,9,74,1,15]:
        cont+=1
        print('Iteration numer: ',cont, '---',i)
        if minimum is None or i < minimum:
            minimum=i
    print('Smallest: ', minimum)


search_min()
