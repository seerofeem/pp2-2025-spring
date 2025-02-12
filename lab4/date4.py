import datetime

date1 = datetime.datetime(2023, 10, 5, 12, 0, 0)  
date2 = datetime.datetime(2023, 10, 5, 11, 0, 0)  

difference = date1 - date2

difference_in_seconds = difference.total_seconds()

print(date1)
print(date2)
print(difference_in_seconds)