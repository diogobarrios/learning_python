import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)  # Pass the filename to .reader object
    header_row = next(reader)  # next() function gives me the next line, so will be the header
    
    # Seeing what column do I need to work on
    # for index, column_header in enumerate(header_row):
    #       print(index, column_header)
    
    # So will be used second column (DATE) and fifth column (TMAX)
    
    # Get dates, high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)

# Shading an area of the plot.
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # Draw the date labels diagonally to prevent them from overlapping.
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
