d={
    'php':{'duration':'2months','fees':1000},
    'java':{'duration': '3months','fees':15000},
    'python':{'duration': '1month','fees':5000}

}



print(d)



print(d['php'])

print(d['php']['duration'])


d['python']['fees']=20000


print(d['python'])



for a,b in d.items():
    print(a,b['duration'])
   # print(a,b)



for c,k in d.items():
    print(k['fees'],c)