a=set(map(int,input().split()))
n=int(input())
cnt=0
for i in range(n):
    s=set(map(int,input().split()))
    if a.issuperset(s):
        cnt+=1
if cnt==n:
    print("True")
else:
    print("False")
    
