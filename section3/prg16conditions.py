grade1=float(input("Type grade of first test"))
grade2=float(input("Type grade of second test"))
absenses=int(input("Type =number of absenses"))

total_classes= int(input("type no. of classes"))

avg_grade= (grade1+grade2)/2

attendance= (total_classes-absenses)/total_classes
print("avg_grade:",avg_grade)
print("attenadance rate",attendance)
if(avg_grade>=6):
    if(attendance>=0.8):
        print("student approved")
    else:
        print("student failed due to attendance rate lower than 80%")
elif(attendance>=0.8):
    print("student failed due to average grade lower than 6.0")
else:
    print("student failed due to both attendance rate loer than 80% and grade loer than 6.0")    











