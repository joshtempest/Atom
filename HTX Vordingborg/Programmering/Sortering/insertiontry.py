def insertionsort(items):
    for n in range(len(items)):
        key = n
        while key > 0:
            if items[key-1]>items[key]:
                items[key-1],items[key]=items[key],items[key-1]
                print(items)
            key = key-1
        



items=[3,23,2,-1,0]
insertionsort(items)
