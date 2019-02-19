def dec2bin(a):
    l=[]
    c=a
    while(c>0):
        b=c%2
        l.append(b)
        c=c//2
    return (l) 
n=int(input("enter a decimal number: "))
l=dec2bin(n)
print("\ndecimal to binary=",end='')
for i in l[::-1]:
    print(i,end='')
