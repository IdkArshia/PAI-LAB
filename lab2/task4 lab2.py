num=(3,2,4,0,6,1,2,4,9)
lowest=100
for x in range(len(num)):
    for y in range (x+1,len(num)):
        if(num[x]+num[y]<=lowest):
            lowest=num[x]+num[y]
            n1=num[x]
            n2=num[y]
print(n1, n2)            