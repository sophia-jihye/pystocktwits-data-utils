from pystocktwits_data_utils import PyStockTwitData

data = PyStockTwitData()

# This needs to be cleaned up

# Create a CSV named VEEV.csv
# Get the company VEEV
# Infinite loop
# Wait 2 seconds before checking again
# Set limit messages to 30 (Get the recent 30 messages)
data.stocktwit_csv_create(["VEEV","AAPL"], 0, 2, limit=30)
