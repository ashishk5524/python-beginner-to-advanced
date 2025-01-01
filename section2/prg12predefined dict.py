#create program with predefined dictionary for a persn include following name age gender address phone
#ask user what he wants then print value associated to that key or display mesaage if not found

person={"name":"Ashish","age":22,"gender":"male","address":"sinnar","phone":7798595428}

user=input("enter what you want").lower()
result=person.get(user,"that info is not available")
print(result)