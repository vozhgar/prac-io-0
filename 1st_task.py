with open('27A_4685.txt') as f:
    s=f.readlines()
for i in range(0, len(s)):
    s[i]=int(s[i])
maxs=-10000
for i in range(0, len(s)-1):# 1 цех
    sumk1=0
    for z in range(0, len(s)):# проверим кудо доставил 1 цех
        if z!=i:
            if abs(z-i)<=329:
                if s[z]%6==0:
                    sumk1+=(s[z]//6)
                else:
                    sumk1+=(s[z]//6)+1
    for j in range(i+1, len(s)): # 2 цех
        sumk2=0
        for x in range(0, len(s)):# куда доставил 2 цех, но не доставлял 1
            if x==i and abs(x-j)<=329:#доставка в 1 цех
                if s[x]%6==0:
                    sumk2+=(s[x]//6)
                else:
                    sumk2+=(s[x]//6)+1
            if x!=j and x!=i:
                if abs(x-j)<=329 and abs(x-i)>329:
                    if s[x]%6==0:
                        sumk2+=(s[x]//6)
                    else:
                        sumk2+=(s[x]//6)+1
        maxs=max(maxs,sumk1+sumk2)
print(maxs)
    
                        
