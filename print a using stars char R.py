for i in range(8):
    for j in range(20):
        if((j==1) or ((j>1 and j<7) and (i==0 or i==3)) or ((i==1 or i==2) and
            (j==11)) or ((j==11) and(i==4)) or((j==12)and(i==5)) or((j==13)and(i==6)) or ((j==14)and(i==7)) ):
            print("*",end=" ") 
        else:
            print(end=" ")
    print(" ")