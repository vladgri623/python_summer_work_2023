import datetime, calendar

year = 2023
free = []
for month in range(1, 13):
    thu = 0
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        dd = calendar.weekday(year, month, day)
        if dd == 3:
            thu += 1
            if thu == 3:
                free_thu = datetime.date(year, month, day)
                free.append(free_thu.strftime("%d/%m"))

for i in free:
    print(i)
