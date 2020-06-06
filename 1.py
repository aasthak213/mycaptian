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
