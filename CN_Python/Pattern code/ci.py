n=int(input())
cnt=1
prev=0
last=0
for i in range(0,(n+1)//2):
    for j in range(0,n):
        print(cnt,end=" ")
        cnt+=1
        last=cnt
    cnt+=(n)
    print()
# cnt-=n*2
# cnt+=1



#second half
if(n%2==1):
    prev=last-n
    cnt=prev-n
    for i in range(0,n//2):
        prev=cnt
        for j in range(0,n):
            print(cnt,end=" ")
            cnt+=1
        cnt=prev-n*2
        prev=cnt 
        print()
else:
    cnt=last
   
    #cnt+=1
    prev=cnt
    
    for i in range(0,n):
        print(cnt,end=" ")
        cnt+=1
    print()
    cnt=prev
    cnt-=n*2
    prev=cnt
    #print(cnt)
    #print(cnt)
    for i in range(0,(n//2)-1):
        for j in range(0,n):

            print(cnt,end=" ")
            cnt+=1
        cnt=prev
        cnt-=n*2
        prev=cnt
        #cnt-=n*n
        print()

/*
#test case  n=4 
#1 2 3 4
#9 10 11 12
#13 14 15 16
#5 6 7 8

#test case n=5
# 1    2   3    4   5
# 11   12  13   14  15
# 21   22  23   24  25
# 16   17  18   19  20
# 6    7    8   9   10

#testcase n=8
#1 2 3 4 5 6 7 8 
#17 18 19 20 21 22 23 24 
#33 34 35 36 37 38 39 40 
#49 50 51 52 53 54 55 56 
#57 58 59 60 61 62 63 64 
#41 42 43 44 45 46 47 48 
#25 26 27 28 29 30 31 32 
#9 10 11 12 13 14 15 16 
*/
