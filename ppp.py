#1
a=int(input())
if a%4==0 or a%100==0 or a%400==0:
    print("YES")
else:
    print("NO")

#2
a=int(input())
s=0
while a>0:
    s+=a
    a-=1
print(s)

#3
a=int(input())
b=list(map(int,input().split()))
som=0
for i in b:
    som+=i
print(som)

#4
a=int(input())
b=list(map(int,input().split()))
s=0
for i in b:
    if i>0:
        s+=1
    else:
        continue
print(s)

#5
a=int(input())
b=1
while b<a:
    b*=2
if a==b:
    print("YES")
else:
    print("NO")

#6
a=int(input())
b=list(map(int,input().split()))
s=-1e9
for i in b:
    if i>s:
        s=i
print(s)

#7
a=int(input())
b=list(map(int,input().split()))
c=-1e9
for i in b:
    if i>c:
        c=i
print(b.index(c)+1)

#8
a=int(input())
b=1
while b<=a:
    print(b, end=" ")
    b=b*2
    
#9
a=int(input())
arr=list(map(int,input().split()))
mn=min(arr)
mx=max(arr)
for i in range(a):
    if arr[i]==mx:
        arr[i]=mn
print(*arr)

#10
a=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
print(*arr)
 
#11
n,a,b=map(int,input().split())
arr=list(map(int,input().split()))
a-=1
b-=1
arr[a:b+1]=arr[a:b+1][::-1]
print(*arr)

#12
a=int(input())
arr=list(map(int,input().split()))
for i in range(a):
    arr[i]=arr[i]**2
print(*arr)

#13
a=int(input())
b=0
n=0
while n<a:
    n+=1
    if a%n==0:
        b+=1
if b>2:
    print("NO")
else:
    print("YES")

#14
n=int(input())
arr=list(map(int,input().split()))
count_max=0
answer=arr[0]
for x in arr:
    count=0
    for y in arr:
        if x==y:
            count+=1
    if count>count_max or(count==count_max and x<answer):
        count_max=count
        answer=x
print(answer)

#15
a=int(input())
arr=[]
n=0
for i in range(a):
    arr.append(input())
b=set(arr)
print(len(b))

#16
a=int(input())
arr=list(map(int,input().split()))
seen=set()
for x in arr:
    if x in seen:
        print("NO")
    else:
        print("YES")
        seen.add(x)
        
#17
a=int(input())
numbers=[input() for _ in range(a)]
count={}
for num in numbers:
    if num in numbers:
        count[num]+=1
    else:
        count[num]=1
three_times=0
for v in count.values():
    if v==3:
        three_times+=1
print(three_times)

#18
n=int(input())
arr=[input() for _ in range(n)]
first_index={}
for i in range(n):
    if arr[i] not in first_index:
        first_index[arr[i]]=i+1
        
for s in sorted(first_index.keys()):
    print(s,first_index[s])
    
#19

n=int(input())
episode={}
for _ in range(n):
    line=input().split()
    name=line[0]
    count=int(line[1])
    if name in episode:
        episode[name]+=count
    else:
        episode[name]=count
for dorama in sorted(episode.keys()):
    print(dorama,episode[dorama])
    
#20
doc = {}
n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == "set":
        key = command[1]
        value = command[2]
        doc[key] = value

    elif command[0] == "get":
        key = command[1]
        if key in doc:
            print(doc[key])
        else:
            print(f"KE: no key {key} found in the document")
