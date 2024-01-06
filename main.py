# Importing necessary functions from respective modules
from rsi import rsi  # Importing the Relative Strength Index (RSI) function from the 'rsi' module
from sma import sma  # Importing the Simple Moving Average (SMA) function from the 'sma' module
# Calculating Simple Moving Average and (SMA) Relative Strength Index (RSI) for the 'orcl.csv' dataset

sma('orcl.csv') # Calling the 'sma' function and providing the 'orcl.csv' file as input

rsi('orcl.csv') # Calling the 'rsi' function and providing the 'orcl.csv' file as input
