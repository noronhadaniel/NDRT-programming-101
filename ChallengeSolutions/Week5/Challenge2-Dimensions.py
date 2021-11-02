import numpy as np
#print("1---------------1")
#print(np.ones((4,4,4)))
x=2
string = "2*np.ones((2,2))"
strlst = list(string)
while True:
    strlst.insert(-2,",")
    strlst.insert(-2,"2")
    eval(''.join(strlst))
    print(f"----------{x+1}D----------")
    x += 1
