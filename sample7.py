x={"name":"suhana","age":21,"gender":"female","nation":"india"}
print(x)
print(type(x))
print(len(x))
print(x["age"])
print(x["nation"])
print(x.get("gender"))
print(x.keys())
print(x.values())
print(x.items())
print("name" in x)
print("name" not in x)
x["age"]=22
print(x)
x["name"]="rajeena"
print(x)
x.update({"name":"suhana"})
print(x)
x["place"]="aluva"
print(x)
x.update({"district":"ernakulam"})
print(x)
x.pop("name")
print(x)
x.popitem()
print(x)
del x["age"]
print(x)
#x.clear()
#print(x)
#del x
#print(x)
for i in x:
    print(i)
for i in x[i]:
    print   
