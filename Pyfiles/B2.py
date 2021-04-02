a=input()
if int(a)%4==0 & int(a)%100!=0:
    print("YES")
elif int(a)%400==0:
    print("YES")
else:
    print("NO")
    print(int(a)%4)