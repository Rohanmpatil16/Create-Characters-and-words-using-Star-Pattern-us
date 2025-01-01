for i in range(9):
    for j in range(10):
        if((i==0 and j==1) or (i==0 and j==9) or (i==1 and j==2) or (i==1 and j==8) or
           (i==2 and j==3) or (i==2and j==7) or (i==3 and j==4) or (i==3 and j==6) or  
           (i==5 and j==4) or (i==5and j==6) or (i==6 and j==3) or (i==6 and j==7) or
           (i==7 and j==2) or (i==7and j==8) or (i==8 and j==1) or (i==8 and j==9)):
            print("**",end=" ")
        else:
            print(" ",end=" ")
        if(i==4 and j==4):
                print("***",end=" ")
    print(" ")