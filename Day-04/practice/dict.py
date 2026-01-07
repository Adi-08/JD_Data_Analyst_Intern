d ={
    "course":"python",
    "fees":8000,
    "duration":"2 months"
    }
n = d["course"]
print(n)

##GET()##
d = {
    "course":"python",
    "fees":8000,
    "duration":"2 months"
}
c = d.get("course")
print(c)

##KEY()##
d = {
    "course":"python",
    "fees":8000,
    "duration":"2 months"
}
for a in d.keys():
    print(a)

##VALUES()##
d = {
    "course":"python",
    "fees":8000,
    "duration":"2 months"
}
for a in d.values():
    print(a)

##ITEMS()##
d = {
    "course":"python",
    "fees":8000,
    "duration":"2 months"
}
for a,b in d.items():
    print(a,b)

##del_(is a keyword)
d = {
    "course":"python",
    "fees":8000,
    "duration":"2 months"
}
del d["fees"]
print(d)

##POP():-(delete)##
d = {
    "course":"python",
    "fees":8000,
    "duration":"2 months"
}
d.pop("duration")
print(d)

##dict()##
d=dict(name="python",fees=8000)
print(d)

##UPDATE()##
d = {
    "course":"python",
    "fees":8000,
    "duration":"2 months"
}
d.update({"fees":10000})
print(d)

##CLEAR()##
d = {
    "course":"python",
    "fees":8000,
    "duration":"2 months"
}
d.clear()
print(d)

##NESTED DICTIONARY##
course = {
    "php":{"duration":"2 months", "fees":15000},
    "python":{"duration":"2 months", "fees":15000},
    "java":{"duration":"2 months", "fees":15000}
}
print(course)
print(course["php"])
