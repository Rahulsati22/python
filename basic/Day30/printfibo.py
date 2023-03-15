dp = [];
num = 1000;
 

for i in range(0,num+1):
    if (i < 2):
        dp.append(i);
        print(i,end=" ");
    else:
        print(dp[i-1]+dp[i-2],end=" ");
        dp.append(dp[i-1]+dp[i-2]);
    
