#Data Structures
#Lists
L=[1,2,3,4,5]
L1=[8,9,10,11,12]
print("maximum:",max(L))
print("minimum",min(L1))
print("sum",sum(L))
print("Average",sum(L)/len(L))
del(L1[3])
print(L1)
print(L[-2])
#Tuple
m=(1,2,3,4,5)
print(m[0])
print(m[-1])
print("maximum",max(m))
n=(1,2,4,0)
a=sorted(n)
print("Sorted:",a)
#Dictionary
d={"Brand":"Apple","Model":"i13"}
a=d["Model"]
print(a)
d.update({"Model":"i14"})
print(d["Model"])
e=d.keys()
print(e)
f=d.values()
print(f)
