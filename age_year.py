from datetime import date,timedelta,datetime
name = str(input("Enter your name: "))
age =int(input("Enter your current age: "))
print(name, "is the age of ",age)
rem_year= 100-age
now = datetime.now()
cur_year = now.year
print("Current year is ",rem_year)
age_100 = now + timedelta()
age_100= now.replace(year = cur_year + rem_year)
print("In the year " ,age_100.year ,name ,"will be 100 years old")