students="john , mary,steve"
students= ["john","mary","steve"]
print(type(students))  #<class 'list'>
print(len(students)) #3
print(students[0])# john
print(students[-1])#steve
print(students[:2])#['john', 'mary']

#tuples
months= ("jan","feb","mar")
print(type(months))#<class 'tuple'>
print(months[0])#jan

print(students)#['john', 'mary', 'steve']
students[0]="george"
print(students)#['george', 'mary', 'steve']

print(months)#('jan', 'feb', 'mar')
#months[0]="new month"#not supported#TypeError: 'tuple' object does not support item assignment

students.append("kate")
print(students)#['george', 'mary', 'steve', 'kate']

students.insert(0,"peter")
print(students)

students.pop()
print(students)

students.pop(1)
print(students)

students.remove("mary")
print(students)

students2=["poul","john"]
stud3=students+students2
print(stud3)