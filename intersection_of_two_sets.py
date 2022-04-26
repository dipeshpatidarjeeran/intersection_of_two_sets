s1={5,3,2,1}
s2={4,3,6,8}
print("set1 is :-",s1)
print("set2 is:-",s2)
print("intersection of two sets:-",s1&s2)
print("intersection of two sets:-",s1.intersection(s2))
s3={8,5,9,2,1}
s4={4,5,6,1,9}
s3.intersection_update(s4)
print(s3)
