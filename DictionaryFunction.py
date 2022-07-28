#get()
#keys()
#values()
#items()



d={
    'name': 'abhishek',
    'fees': 8000,
    'duration': '2 months'

}
print(d)

a=d.get('name')
print(a)

for i in d.keys():
    print(i)
for n in d.values():
    print(n)
for a,b in d.items():
    print(a,b)




#delete
#1-del()
#2-pop()

del d['fees']
print(d)

a=d.pop("name")
print(a)
print(d)


#creat-------------------



m=dict(name='python',fees=8000)
print(m)



#update----------



d.update({'fees':1000})
print(d)

d['name']='biswas'
print(d)


#insert----------------------------------------------------------------------



d['name']='abhishek'
print(d)

d['age']=24

print(d)

k={

}

k['name']='another'
print(k)
k['home']='xyz'
k['age']=24
print(k)