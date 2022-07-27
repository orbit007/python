#l=[10,20]
#a=15
#n=input("enter")
#l.append(n)
#b=int(l[2])
#print(b+a)

#------------------------------------------------------
#using list stack and queue

#1push
#2pop
#3peek
#display

l=[]
while True:
    c=int(input(
        '''
        1 push element
        2 pop element
        3 peek element
        4 display element
        5 exit
        
        '''
    ))

    if c==1:
        n=input("enter number")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("stack is empty")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("empty stack")
        else:
            print(l[-1])
    elif c==4:
        print(l)
    else:
        break