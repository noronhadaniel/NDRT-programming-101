def listshift(list,shift,leftshift=True):
    if leftshift == False:
        shift = -shift
    outlist = []
    lenlist = len(list)

    for x in range(0,lenlist):
        if x+shift > lenlist - 1:
            outlist.append(list[x-lenlist+shift])
        else:
            outlist.append(list[x+shift])
    return outlist
    
testlist = [1,2,3,4,5]
print(listshift(testlist,2))#,True))
