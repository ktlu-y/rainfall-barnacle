import matplotlib.pyplot as plt
import csv
import matplotlib
from datetime import datetime

# Setting font as Microsoft YaHei
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
data = []

# Read CSV file
with open('C:\\Users\\sdit\\Desktop\\pfad\\daily_SSP_RF_2024.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(spamreader)  # Jump the title

    for row in spamreader:
        if not row or len(row) < 4:  # Make sure rows are not empty and have enough columns
            continue
        
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')  # The date format is YYYY-MM-DD
            rainfall = float(row[3])  # Rainfall is located in the 4th column
            
            # Filter Date Range
            if date >= datetime(2024, 7, 1) and date <= datetime(2024, 7, 31):
                data.append((date.strftime('%Y-%m-%d'), rainfall))
        except ValueError:
            continue  # If the conversion fails, skip the line.

# Saperate Date and Rainfall
if data:  # Make sure the data is not empty
    dates, rainfalls = zip(*data)

# 绘制柱状图
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(dates, rainfalls, color='blue')  # Use a bar chart as the visualization

    ax.set_title('Daily Total Rainfall in July 2024 - Sham Shui Po', fontsize=16)
    ax.set_xlabel('Date (YYYY-MM-DD)', fontsize=14)
    ax.set_ylabel('Total Rainfall (mm)', fontsize=14)

    ax.set_xticklabels(dates, rotation=45, ha='right', fontsize=10)

    plt.tight_layout()
    plt.show()
else:
    print("No valid data to plot.")
