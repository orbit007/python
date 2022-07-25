l=[10,20,30,40]
print(l[1])
print(l[0:])
print(l[0:2])
print(l[0::2])



w=[10,20,30,40,[1,2,3,4]]
print(w[0:])
print(w[4])
print(w[4][2])
print(w[4][0:])



a=[1,2,3,4,5]
print(a[0::2])
print(a[0:])
print(a[-1::-1])

# list iteration

t=len(l)
print(t)

for n in range(t):
    print(l[n])
print()

for i in l:
    print(i)
print()

for n in range(t-1,-1,-1):
    print(l[n])



for n in range(t-1,-1,-1):
    print(l[n])

# list comprehension

k=[]
for n in range(20):
    k.append(n)
print(k)

m=[]
for i in range(6):
    j=int(input("enter"))
    m.append(j)
   # m.append(int(input("enter")))

print(m)

h=[]


for i in range(6):
    k=int(input("enter"))
    if k%2==0:
        h.append(k)
print(h)

s="abhishek"
n=[]
for j in range(len(s)):
    n.append(s[j])
print(n)

o=[]
for l in s:
    o.append(l)
print(o)


#list function------------------------------------------------------------------


l=[20,30,40,50,60,70]
print(l)

del l[1]
print(l)

l.pop(2)
print(l)
print(l.pop(2))
print(l)

l.remove(70)
print(l)
l.clear()
print(l)

k=[1,2,3,4,5,6,7,8]
k[0]=10
print(k)

#insert()------>kishi v jghe pr insert kr skte hai (take two args)
#append()------>last ke side me add hoga---->jesa data type wese utha kr aandar rkh dega
#extends()----->ye andar le value pr kaaam krta hai

m=[20,30,40,50]

m.insert(0,80)
print(m)

n=[1,2]
m.append(n)
m.append(105)
print(m)

m.extend(n)
print(m)

m.insert(1,200)
print(m)

m.append(1000)
print(m)


