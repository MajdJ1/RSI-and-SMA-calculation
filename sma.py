import csv


def sma(filename):
    historical_data = []  # Creating an empty list to store the historical data
    with open(filename, 'r') as file:
        header = file.readline().strip().split(',')  # Reading the header and splitting  columns
        for line in file:
            data = line.strip().split(',')  # Splitting data into columns
            entry = {header[i]: data[i] for i in range(len(header))}  # Creating dictionary for each row
            historical_data.append(entry)  # Append dictionary to list
    sma_values_5 = []  # Create a list to store SMA values
    # Task 2: Calculating Simple Moving Averages (SMA) for a 5-day window
    for i in range(5, len(historical_data)):
        sum_close = sum(float(historical_data[j]['Close']) for j in range(i - 4, i + 1))  # Calculating the sum of Close prices
        sma = sum_close / 5  # Calculating SMA for 5-day window
        sma_values_5.append(sma)  # adding SMA value to the list
    # Writing SMA values to orcl-sma.csv
    with open('orcl-sma.csv', 'w') as sma_file:
        sma_file.write('SMA\n')
        for value in sma_values_5:
            sma_file.write(f'{value}\n')