#1
n=int(input())
for i in range(n):
    print((i+1)**2)

#2
n=int(input())
numbers=[]
for i in range(0,n+1):
    if i%2==0:
        numbers.append(str(i))
print(",".join(numbers))

#3
n=int(input())
a=0
while n>=0:
    n-=12
    print(a,end=" ")
    a+=12
    
#4
a,b=map(int,input().split())
for i in range(b-a+1):
    print(a**2,end="\n")
    a+=1
    
#5
n=int(input())
while n>=0:
    print(n,end="\n")
    n-=1
    
#6
n=int(input())
a=0
b=1
for i in range(n):
    if i>0:
        print(",",end="")
    print(a,end="")
    a,b=b,a+b
    
#7
n=input()
print(n[-1::-1])

#8
n = int(input())

for num in range(2, n + 1):
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
        
#9
n=int(input())
for i in range(n+1):
    print(2**i,end=" ")
    n-=1
    
#10
a=input().split()
b=int(input())
for i in range(b):
    print(*a,end=" ")
    
#11
import json
source = json.loads(input())
patch = json.loads(input())
def apply_patch(src, pat):
    for key, value in pat.items():
        if value is None:
            if key in src:
                del src[key]
        elif key in src and isinstance(src[key], dict) and isinstance(value, dict):
            apply_patch(src[key], value) 
        else:
            src[key] = value
    return src
result = apply_patch(source, patch)
print(json.dumps(result, sort_keys=True, separators=(",", ":")))

#12
import json
obj1 = json.loads(input())
obj2 = json.loads(input())
differences = []
def find_diffs(a, b, path=""):
    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a.keys()) | set(b.keys())
        for key in keys:
            new_path = f"{path}.{key}" if path else key
            va = a.get(key, "<missing>")
            vb = b.get(key, "<missing>")
            find_diffs(va, vb, new_path)
    else:
        if a != b:
            va_str = json.dumps(a, separators=(',', ':')) if a != "<missing>" else "<missing>"
            vb_str = json.dumps(b, separators=(',', ':')) if b != "<missing>" else "<missing>"
            differences.append(f"{path} : {va_str} -> {vb_str}")
find_diffs(obj1, obj2)
if differences:
    for line in sorted(differences):
        print(line)
else:
    print("No differences")
    
#13
import json
import re
data = json.loads(input())
q = int(input())
queries = [input() for _ in range(q)]
token_re = re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)|\[([0-9]+)\]')
for query in queries:
    current = data
    not_found = False
    for match in token_re.finditer(query):
        key, idx = match.groups()
        try:
            if key:
                if isinstance(current, dict):
                    current = current[key]
                else:
                    not_found = True
                    break
            elif idx:
                index = int(idx)
                if isinstance(current, list):
                    current = current[index]
                else:
                    not_found = True
                    break
        except (KeyError, IndexError, TypeError):
            not_found = True
            break
    if not_found:
        print("NOT_FOUND")
    else:
        print(json.dumps(current, separators=(',', ':')))
        
#14
from datetime import datetime, timedelta
s1=input().split()
date1=s1[0]
utc1=s1[1]
s2=input().split()
date2=s2[0]
utc2=s2[1]
d1=datetime.strptime(date1, "%Y-%m-%d")
d2=datetime.strptime(date2, "%Y-%m-%d")
if "+" in utc1:
    sign1=1
else:
    sign1=-1
h1, m1=map(int,utc1[4:].split(":"))
if "+" in utc2:
    sign2=1
else:
    sign2=-1
h2,m2=map(int, utc2[4:].split(":"))
d1=d1-sign1*timedelta(hours=h1, minutes=m1)
d2=d2-sign2*timedelta(hours=h2, minutes=m2)
diff=abs(d1-d2)
print(diff.days)

#15
from datetime import datetime, timedelta
def read_utc_date():
    s=input().split()
    date=s[0]
    utc=s[1]
    d=datetime.strptime(date, "%Y-%m-%d")
    sign=1 if "+" in utc else -1
    h,m=map(int,utc[4:].split(":"))
    return d-sign*datetime(hours=h, minutes=m)
def is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)
birth=read_utc_date()
current=read_utc_date()
year=current.year
month=birth.month
day=birth.day
if month==2 and day==29 and not is_leap(year):
    day=28
next_birthday=datetime(year,month,day)
if next_birthday<current:
    year+=1
    if month==2 and day==29 and not is_leap(year):
        day=28
    else:
        day=birth.day
    next_birthday=datetime(year,month,day)
diff=next_birthday-current
print(diff.day)

#16
from datetime import datetime,timedelta
def read_utc_datetime():
    s=input().split()
    dt_str,tz=" ".join(s[:2]),s[2]
    dt=datetime.strptime(dt_str, "%Y-%m-%d")
    sign =1 if "+" in tz else -1
    hours,minutes=map(int, tz[4:].split(":"))
    return dt-sign*timedelta(hours=hours, minutes=minutes)
start=read_utc_datetime()
end=read_utc_datetime()
duration_seconds=int((end-start).total_seconds)
print(duration_seconds)

#17
import math
r=float(input())
x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
dx=x2-x1
dy=y2-y1
a=dx*dx+dy*dy
b=2*(dx*x1+dy*y1)
c=x1*x1+y1*y1-r*r
disc=b*b-4*a*c
if disc<=0:
    print("0.0000000000")
else:
    sqrt_disc=math.sqrt(disc)
    t1=(-b-sqrt_disc)/(2*a)
    t2=(-b+sqrt_disc)/(2*a)
    t_enter=max(0,min(t1,t2))
    t_exit=min(1,max(t1,t2))
    if t_exit<t_enter:
        print("0.0000000000")
    else:
        segment_lenght=math.hypot(dx,dy)*(t_exit-t_enter)
        print(f"{segment_lenght:.10f}")
        
#18
x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
xr=(x1*y2+x2*y1)/(y1+y2)
yr=0.0
print(f"{xr:.10f} {yr:.10f}")


#19
import math
def solve() -> None:
    R = float(input().strip())
    Ax, Ay = map(float, input().strip().split())
    Bx, By = map(float, input().strip().split())
    dx = Bx - Ax
    dy = By - Ay
    dAB = math.hypot(dx, dy)
    if dAB < 1e-12:
        print("0.0000000000")
        return
    v2 = dx*dx + dy*dy
    dot = Ax*dx + Ay*dy
    t0 = -dot / v2
    obstructed = False
    if 0.0 <= t0 <= 1.0:
        footX = Ax + t0 * dx
        footY = Ay + t0 * dy
        dist_foot = math.hypot(footX, footY)
        if dist_foot < R - 1e-9:   # строго внутри
            obstructed = True
    if not obstructed:
        print("{:.10f}".format(dAB))
        return
    a = math.hypot(Ax, Ay)
    b = math.hypot(Bx, By)
    thetaA = math.atan2(Ay, Ax) % (2*math.pi)
    thetaB = math.atan2(By, Bx) % (2*math.pi)
    gammaA = math.acos(R / a) if a > R else 0.0
    gammaB = math.acos(R / b) if b > R else 0.0
    tangentsA = [ (thetaA + gammaA) % (2*math.pi),
                  (thetaA - gammaA) % (2*math.pi) ]
    tangentsB = [ (thetaB + gammaB) % (2*math.pi),
                  (thetaB - gammaB) % (2*math.pi) ]
    tangent_len = math.sqrt(a*a - R*R) + math.sqrt(b*b - R*R)
    best = float('inf')
    for angA in tangentsA:
        for angB in tangentsB:
            diff = abs(angA - angB)
            if diff > math.pi:
                diff = 2*math.pi - diff
            cand = tangent_len + R * diff
            if cand < best:
                best = cand
    print("{:.10f}".format(best))
if __name__ == "__main__":
    solve()

#20
g = 0  
def outer():
    n = 0  
    def inner(commands):
        nonlocal n
        global g
        for scope, val in commands:
            if scope == "global":
                g += val
            elif scope == "nonlocal":
                n += val
            elif scope == "local":
                x = val 
    return inner, lambda: n 
q = int(input())
commands = [input().split() for _ in range(q)]
commands = [(s,int(v)) for s,v in commands]
inner_func, get_n = outer()
inner_func(commands)
print(g, get_n())

#21
import importlib
n=int(input())
for _ in range(n):
    line=input().split()
    module_path,attr_name=line[0],line[1]
    try:
        mod=importlib.import_module(module_path)
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue
    if not hasattr(mod,attr_name):
        print("ATRIBUTE_NOT_FOUND")
    else:
        attr=getattr(mod,attr_name)
        if callable(attr):
            print("CALLBLE")
        else:
            print("VALUE")
