import csv

# Task 3: Calculating Relative Strength Index (RSI) for a 14-day window and write to file
def rsi(filename):
    historical_data = []  # Creating an empty list to store the historical data
    rsi_values = []  # Creating a list to store RSI values

    for i in range(14, len(historical_data)):
        gains = []
        losses = []
        for j in range(i - 13, i):
            price_diff = float(historical_data[j]['Close']) - float(historical_data[j - 1]['Close'])
            if price_diff > 0:
                gains.append(price_diff)
            else:
                losses.append(abs(price_diff))

        avg_gain = (sum(gains) / 14) if gains else 0
        avg_loss = (sum(losses) / 14) if losses else 0

        if avg_loss != 0:
            rsi = 100 - (100 / (1 + (avg_gain / avg_loss)))
        else:
            rsi = 100  # for avoiding division by zero scenario(preventing error)

        rsi_values.append(rsi)  #  adding RSI value to the list


    # putting RSI values to orcl-rsi.csv
    with open('orcl-rsi.csv', 'w') as rsi_file:
        rsi_file.write('RSI\n')
        for value in rsi_values:
            rsi_file.write(f'{value}\n')