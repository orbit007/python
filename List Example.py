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
