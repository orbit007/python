w="ABHISHEK KUMAR BISWAS"
n=w.lower()
print(n)

u=n.upper()
print(u)

t=n.title()
print(t)

c=n.capitalize()
print(c)



# find() index()  isalpha()  isdigit()  isalnum()

print(w.find('E'))

print(w.find('E',7))

print(w.find('Z'))

#index

print(w.index('E'))
print(w.index('E',7))

#isalpha()  isdigit()  isalnum()

print(w.isalpha())

print(w.isdigit())

print(w.isalnum())



# python chr() and ord()

a=ord("A")
print(a)

y=chr(65)
print(y)


#  python string formate() method


k="abhishek {} biswas {}".format("kumar",20)
print(k)

c="abhishek {0} biswas {1}".format("kumar",20)
print(c)

