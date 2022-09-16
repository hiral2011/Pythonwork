n=int(input("enter num="))
i=0
while i<n:
    for i in range(n):
        for j in range(n):
            if  i==2 or j==2 or (i<=1 and j==0) or (i==n-1 and j<=1) or (i==0 and j>=n-2) or (i>=n-2 and j==n-1):
                print("*",end=" ")
            else:
                  print(' ',end=" ")
        i=i+1
        print()