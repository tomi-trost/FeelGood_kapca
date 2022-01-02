import datetime

# Program uses a day value of the month, to govern how many times the loop prints the sting 'Ass'
d = datetime.datetime.now()
day_date = d.strftime("%d")
day_count = int(day_date)

for _ in range(day_count):
    print('Ass')