for i in range(9):
    for j in range(10):
        if(((j==1)and(i>0 and i<7))or(i==2 and j==2) or((j==7)and(i>0 and i<7)) or (i==3 and j==3) or (i==4 and j==4) or
           (i==3 and j==5) or (i==2 and j==6)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
        