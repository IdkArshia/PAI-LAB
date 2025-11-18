import json

try:
    d={'Ali':23,'Saad':24,'Salman':15,'Shams':25,'Sadiq':46,'Hammad':23}

    with open("ages.json","w") as f:
        json.dump(d,f)

    with open("ages.json","r") as f:
        data=json.load(f)

    max_age=-1
    max_name=""
    for name in data:
        if data[name]>max_age:
            max_age=data[name]
            max_name=name

    print("Max age:",max_name,max_age)

    for name in data:
        if name!=max_name and data[name]==max_age:
            print(name,"also has max age")

except Exception as e:
    print("Error:",e)
