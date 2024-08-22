# i=1
# while i<=10:
#     print(i)
#     i+=1
# i=1
# while i<=20:
#     print(i)
#     i+=2
# i=1
# while i<=10:
#     print(i)
#     if i==5:
#         break
#     i+=1

i=0
while i<=10:
    i+=1
    if i==5:
        continue
    print(i)

x=("apple","banana","orange") 
for i in x:
    print(i) 
x={"name":"suhana","age":21,"gender":"female"}
for i in x:
    print(i)
for i in x.keys():
    print(i)
for i in x.items():
    print(i)
for i in x. values():
    print(i)

x=["apple","banana","orange"]
for i in x:
    print(i)

x="apple"
for i in x:
    print(i)

x={"apple","banana","orange"}
for i in x:
    print(i)

for i in range(11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,21,2):
    print(i)    

for i in range(1,21):
    if i==5:
        break
    print(i)        
for i in range(1,21):
    if i==5:
        continue
    print(i)

for i in x:
    pass
    