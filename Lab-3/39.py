'''Write a program to Get Only unique items from two sets'''

s1={1,2,3}
s2={1,7,5}

us=s1.union(s2) - s1.intersection(s2)

print("The only Unique elements are :", us)