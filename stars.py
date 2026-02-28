n=int(input("Number of times to print:"))
a="-"
for i in range(0,n):
            print(a*i);
            if(i==0 or i/2==0):
                print("**",end="**")
            else:
                print("***",end="***")
