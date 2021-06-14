import csv
import matplotlib.pyplot as plt
from datetime import datetime

#with open("C:/Users/w010ked/Documents/GitHub/CEG2900/Class-Demos/sitka_weather_07-2018_simple.csv", 'r') as f:
with open("sitka_weather_07-2018_simple.csv", 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    highs = []
    dates = []
    for row in reader:
        #print(row)
        high = int(row[5])
        #print(type(row[5]))
        highs.append(high)
        date = row[2]
        #dates.append(date)
        date_to_dt = datetime.strptime(date, '%Y-%m-%d')
        dates.append(date_to_dt)

print(highs)
#print(dates)

plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.plot(highs, c='red')
#plt.plot(highs)
ax.plot(dates, highs, c="red")
ax.set_title("High Temperature to Based on Day", fontsize = 24)
ax.set_xlabel("Days of the Month", fontsize = 18)
ax.set_ylabel('High Temps', fontsize = 18)
ax.tick_params(axis = 'both', which = 'major', labelsize = 16)
fig.autofmt_xdate()

plt.show()