people=[

    {"name":"shahzad","Phone":"03363748411"},
    {"name":"ahsan","Phone": "123452323267"},
    {"name":"sajad","Phone":"788585855757"}

]

people.sort(key=lambda person:person["name"])

for i in people:
    print(i)