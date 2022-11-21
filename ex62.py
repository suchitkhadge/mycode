farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

for x in farms[0]["agriculture"]:
    print(x)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

for farm in farms:
    print("-", farm["name"])
ask = input("Choose a NE, W or SE Farm to display the result: ")

for farm in farms:
    if farm["name"].lower() == ask.lower():
        print(farm["agriculture"])
print("xxxxxxxxxxxxxxxxxx")
yuck= ["carrots", "celery"]

for farm in farms:
    if farm["name"].lower() == ask.lower():
        for ag_item in farm["agriculture"]:
            if ag_item not in yuck:
                 print(ag_item)

    
