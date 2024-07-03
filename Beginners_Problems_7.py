print("===Have you seen this number before?===")
s = set()
num = [1,3,8,35,4,2,3]
for n in num:
    if n in s :
        print ("YES")
    else:
        print ("NO")
        s.add(n)
print("===Special Words===")
count = 0
a = input().lower()
s = set(a.split( ))
print(len(s))
for i in a:
    if 'a' == i:
        count+=1
print(count)
print("===Special Numbers===")
listA = [18, 2, 90, 3, 5]
listB = [2, 86, 42, 5, 7]
both = set()
for i in listA:
    if i in listB :
        both.add(i)
print(both)
print("===Multilingual===")
numP = int(input("How many people are there?\n>>"))
L = []
for i in range(numP):
    numL = int(input("How many languages can you speak?\n>>"))
    for l in range(numL):
        l = input("What languages can you speak in?\n>>")
        L.append(l)
totalL = set(L)
print("Total languages spoken in the group:",len(totalL))
print("Languages spoken:",", ".join(sorted(totalL)))
