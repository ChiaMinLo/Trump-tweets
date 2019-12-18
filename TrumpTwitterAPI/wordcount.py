import pandas as pd
import string
df=pd.read_excel('波動大.xlsx')
punc="!()-[]{};:\,<>./?@#$%^&*_~"
a=[]
d=dict()
ans=[]
for i in df.index:
    x=df["Trump's tweets"][i].lower()
    for j in x:
        if j in punc:
            x=x.replace(j,"")
    x=x.split()
    for word in x:
        a.append(word)
for key in a:
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
for key in d:
    ans.append((d[key],key))
ans.sort(reverse=True)
print(ans)
