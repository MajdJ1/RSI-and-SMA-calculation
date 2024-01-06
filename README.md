# RSI-and-SMA-calculation
 This script  provides features for calculating Simple Moving Averages (SMA) and Relative Strength Index (RSI) using a given CSV dataset that holds financial market information. The script employs CSV file management and Python's inherent libraries for data analysis in computing these specific indicators.
 #Prerequisites
 Python 3.x CSV file containing financial data (e.g., 'orcl.csv').
 #Installation 
 Follow these steps to set up and use the package:
 download the script files or Clone the repository to your device (note:Python 3.x must be installed on your device/system ) 
 #Usage  
 * Relative Strength Index (RSI)calcultion (rsi.py):
 1- calculating the RSI for a 14-day window and Writing RSI to CSV:
 
 
 * Simple Moving Average (SMA) Calculation(sma.py):
 1-Calculating SMA for a 5-day window and Writing SMA to CSV:
   Ensure that the 'orcl.csv' file containing financial data is placed in the project directory before running the script. Upon execution, the script will compute SMA values for a 5-day window using the 'Close' prices from the 'orcl.csv' file. The resulting SMA values will be saved in a new file named orcl-sma.csv.
* Relative Strength Index (RSI)calcultion (rsi.py):
  This script will compute RSI values for a 14-day window using the 'Close' prices from the 'orcl.csv' file. The resulting RSI values will be saved in a new file named orcl-rsi.csv.
   
