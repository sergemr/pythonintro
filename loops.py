days_of_week = "Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"
should_stop = 10
counter = 0

while(counter < should_stop):
    counter = counter+1
    print(counter)


for day in days_of_week:
    if(day == "Fri"):
        print("almost weekend")
    if(day == "Sat"):
        break
    print(day)
