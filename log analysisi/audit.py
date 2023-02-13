from statistics import mode
import pandas as pd
import matplotlib.pyplot as plt
file=open(r"//home/sandhya/Documents/audit.txt","r")
cnt=0
c=file.readlines()
l=[]
for i in c:
    cnt+=1
    h=i.strip().split(" ")
    l.append(h)
log_number=[]
date_time=[]
desc=[]
desc2=[]
for i in l:
    log_number.append(i[0])
    date_time.append(i[2])
    desc.append(''.join(str(elem) for elem in i[-5:-2]))
    desc2.append(i[-3])
lp=[]
print("log_number","\t","date_time","\t","\t","\t","desc")
for i in range (cnt):
    print(log_number[i],"\t",date_time[i],"\t",desc[i])


freq=mode(desc2)
print( "frequently logged user:",freq)
df=pd.DataFrame({"logno":log_number,"datetime":date_time,"description":desc})
count = df.groupby('logno').count()
count1=df.groupby('description').count()
print(df)
fig=plt.figure(figsize=(10,10))
plt.plot(count1)
plt.show()

