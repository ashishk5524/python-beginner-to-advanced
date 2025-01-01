dob=(input("enter your date of birth in format DD-MM-YYYY"))
months=("january","February","March","April","May","june","july","August","September","October","November","December",)
index= int(dob[3:5]) - 1
bd_month=months[index]

print("you were born in",bd_month)