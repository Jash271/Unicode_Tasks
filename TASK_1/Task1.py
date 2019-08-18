binlist=[]
l=[]

print("Head Count of numbers to be tested")
Test=int(input())

for i in range(0,Test):
    print("Enter the binary Number")
    val=input()
    binlist.append(val)

length=len(binlist)
j=0
for  j in binlist:
    val=j
    value=int(val,2)
    
    if value % 5 ==0:
        l.append(bin(value))
        
        


print("NO DIVISIBLE BY 5:")
for i in l:
    length=len(i)
    print(i[2:length+1],end=" ,")