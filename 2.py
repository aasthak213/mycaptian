#assigning elements to different lists
print("assigning elements to different lists")
mylist1=[1,2,3]
mylist2=["cat","rat","dog"]
print("mylist1",mylist1,"mylist2",mylist2)
#accessing element from a tuple
print("accessing element from a tuple")
mytuple=("cat","rat","dog")
print("element at index 1 is ", mytuple[1])
#deleting dictionary elements
print("deleting dictionary elements")
myd={
    "cat" : 1,
    "rat" : 2,
    "dog" : 3
    }
print(myd)
del myd["rat"]
print("after deleting element at index rat",myd)

