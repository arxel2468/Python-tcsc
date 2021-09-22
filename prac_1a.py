import datetime
name=input("Hello! Please enter your name: \n")
print("Hello! ",name)
age=int(input("Enter your age:\n"))
year_now=datetime.datetime.now()
print("Current year is",year_now.year)
print("You will turn 100 in "+ str(int(100-age)+int(year_now.year)))