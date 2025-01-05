for i in range(10):
    for j in range(12):
        if(((i==1) and (j>2 and j<8)) or ((i==6)and(j>2 and j<8)) or ((j==2 or j==8) and (i==2)) or
           ((j==1 or j==9) and(i==3)) or ((j==1 or j==9) and(i==4)) or  ((j==2 or j==8) and(i==5)) or
           ((j==5 or j==6)and(i==4)) or ((i==5)and(j==7)) or((i==7) and (j==8)) or ((i==8) and (j==9))):  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")  