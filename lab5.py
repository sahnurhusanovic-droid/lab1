#1
import re
s=input()
if re.match(r"Hello",s):
    print("Yes")
else:
    print("No")
    
#2
a=input()
b=input()
if b in a:
    print("Yes")
else:
    print("No")
    
#3
import re
a=input()
b=input()
matches=re.findall(b,a)
print(len(matches))

#4 
a=input()
for i in a:
    if i.isdigit():
        print(i,end=" ")
print()

#5
import re
s=input()
if re.match(r'^[A-Za-z].*[0-9]$', s):
    print("Yes")
else:
    print("No")
    
#6
import re
s=input()
match=re.search(r'\S+@\S+\.\S+',s)
if match:
    print(match.group())
else:
    print("No email")
    
#7
import re
s=input()
b=input()
c=input()
result=re.sub(b,c,s)
print(result)

#8
import re
s=input()
b=input()
parch=re.split(b,s)
result=",".join(parch)
print(result)

#9 
s=input().split()
v=0
for i in s:
    if len(i)==3:
        v+=1
    else:
        v=v
print(v)

#10
import re
s=input()
if re.search(r'cat|dog',s):
    print("Yes")
else:
    print("No")
    
#11
import re
s=input()
result=re.findall(r'[A-Z]', s)
print(len(result))

#12
import re
s=input()
result=re.findall(r'\d{2,}',s)
print(" ".join(result))

#13
import re
s=input()
words=re.findall(r'\w+',s)
print(len(words))

#14
import re
s=input()
b=re.compile(r'^\d+$')
if b.match(s):
    print("Match")
else:
    print("No match")
    
#15
import re
s=input()
def double_digit(match):
    return match.group()*2
result=re.sub(r'\d',double_digit,s)
print(result)

#16
import re
s=input()
b=r'Name: (.*), Age: (.*)'
match=re.match(b,s)
if match:
    name=match.group(1)
    age=match.group(2)
    print(name,age)
    
#17
import re
s=input()
dates=re.findall(r'\b\d{2}/\d{2}/\d{4}\b',s)
print(len(dates))

#18
import re
s=input()
b=input()
pattern=re.escape(b)
result=re.findall(pattern,s)
print(len(result))

#19
import re
s=input()
b=re.compile(r'\b\w+\b')
result=re.findall(b,s)
print(len(result))