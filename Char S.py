for i in range(7):
    for j in range(19):
        if(((j>2 and j<8) and (i==0 or i==3 or i==6)) or ((i==1 and j==2) or (i==2 and j==2)) or
           ((i==4 and j==8) or (i==5 and j==8))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")