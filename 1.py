n=int(input("enter number of terms: "))
f,s =0,1
i=0
print("fibonacci serise of " ,n, " terms is as follow: ")
print(f)
print(s)
while i!=n-2:
    t=f+s
    f=s
    s=t
    print(t)
    i=i+1
#second program
mylist = [12,-7,5,64,-14]
print("mylist= ",mylist)
print("positive no in mylist: ")
for n in mylist:
    if n>0:
     print(n)
mylist = [12,14,-95,3]
print("mylist",mylist)
print("positive no in mylist: ")
for n in mylist:
    if n>0:
     print(n)
    
