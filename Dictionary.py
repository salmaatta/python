#nested dictionary
languages={
    "one":{
        "name":"python",
        "progress":"50%"
    },
    "two":{
        "name":"c++",
        "progress":"80%"
    }

}
#print the dictionary
print (languages)
print (languages["one"])
#print the length
print(len(languages))
print(len(languages["one"]))
#update dictionary
languages["three"]={
    "name":"c",
    "progress":"0%"
}
print (languages)
languages.update({"four":{
    "name":"js",
    "progress":"0%"
}}
)
print(languages)
print("-"*100)
print(languages.setdefault("two","three"))
print("-"*100)
#popitem
x={
    "name":"salma",
    "country":"egypt"

}
x.update({"age":"21"})
print(x.popitem())
print("-"*100)

#items
