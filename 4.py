import random
from datetime import datetime, timedelta
from array import array

start_date = datetime.now() - timedelta(days=5*365)
dates_list = []

for _ in range(10):
    random_days = random.randint(0, 5*365)
    random_date = start_date + timedelta(days=random_days)
    dates_list.append(random_date)

timestamp_array = array("q", [int(d.timestamp()) for d in dates_list])

for i in range(len(timestamp_array) - 1):
    date1 = datetime.fromtimestamp(timestamp_array[i])
    date2 = datetime.fromtimestamp(timestamp_array[i+1])
    diff_days = abs((date2 - date1).days)
    print(f"Разница между {date1.strftime('%Y-%m-%d')} и {date2.strftime('%Y-%m-%d')}: {diff_days} дней")