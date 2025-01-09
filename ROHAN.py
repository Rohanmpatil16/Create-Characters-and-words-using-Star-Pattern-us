for i in range(7):
    for j in range(35):
        if(((i==0 or i==3)and(j>-1 and j<4)) or ((i==1) and (j==0 or j==5)) or ((i==2) and(j==5 or j==0)) or ((j==0)and(i==4 or i==5 or i==6)) or ((i==4)and(j==5)) or ((i==5 and j==6)) or ((i==6)and(j==7))
        or (((i==0) or (i==6)) and ((j>8)and(j<13))) or((j==9 or j==12)and(i<6 and i>0))
        or((j==14 or j==18)and(i<=6 and i>=0)) or((i==3)and(j>14 and j<18)) or
        ((i==0 or i==3)and(j>20 and j<24)) or ((j==20 or j==24))
        or (j==26 or j==31) or (j==27 and i==1) or(j==28 and i==2) or(j==29 and i==3) or(j==30 and i==4)):
            print("*",end=" ")
        else:
            print("",end="  ")
    print(" ")