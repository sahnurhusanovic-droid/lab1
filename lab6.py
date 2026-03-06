#1
n=int(input())
s=map(int,input().split())
b=0
for i in s:
    i=i**2
    b+=i
print(b)

#2
a=int(input())
b=map(int,input().split())
def ppp(x):
    return x%2==0
result=filter(ppp,b)
result=list(result)
print(len(result))

#3
n=int(input())
s=input().split()
a=0
for i in s:
    print(f"{a}:{i}",end=" ")
    a+=1
    
#4
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
result =0
for c,d in zip(a,b):
    result+=c*d
print(result)

#5
s=input()
b="aieuoAUOIE"
if any(c in b for c in s):
    print("Yes")
else:
    print("No")

#6
n=int(input())
a=map(int,input().split())
if all(c>=0 for c in a):
    print("Yes")
else:
    print("No")
    
#7
a=int(input())
s=input().split()
print(max(s,key=len))

#8
n=int(input())
s=list(map(int,input().split()))
print(*sorted(set(s)))

#9
n=int(input())
a=input().split()
b=input().split()
d = dict(zip(a,b))
w=input()
if w in d:
    print(d[w])
else:
    print("Not found")
    
#10
n=int(input())
s=list(map(int,input().split()))
q=0
for i in s:
    if i == 0:
        q+=0
    else:
        q+=1
print(q)
