from itertools import combinations
n=input().split()
val=int(n[1])
final=[]
for i in range (val):
    s=list(combinations(sorted(n[0]),i+1))
    for j in s:
        x=list(j)
        x.sort()
        w=''.join(k for k in x)
        final.append(w)
for k in final:
    print(k)
