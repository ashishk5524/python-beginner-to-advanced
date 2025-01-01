#person=["john","green","1980","canada"]
person={"first_name":"john","last_name":"green","do":1980,"country_of_birth":"canada"}
print(type(person))

print(person["first_name"])
print(person["do"])
person["do"] =1979
print(person)

person["Marital_status"]="Married"
print(person)

person["children"]= ["nathan","ethan"]
print(person)

person["children"].append("Ana")

print(person)

print(person.get("age","invalid property"))
print(person.get("children","invalid property"))

key="first_name"
print(person[key])
print(person["first_name"])