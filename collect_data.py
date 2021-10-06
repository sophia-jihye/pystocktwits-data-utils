from pystocktwits_data_utils import PyStockTwitData
from datetime import datetime
import argparse
import os

data_dir = './scraped_data'

parser = argparse.ArgumentParser()
parser.add_argument('--ticker', type=str, default="AAPL")
args = parser.parse_args()

company_id = args.ticker

save_dir = os.path.join(data_dir, company_id)
if not os.path.exists(save_dir): os.makedirs(save_dir)

data = PyStockTwitData()

for _ in range(60):   # 목표: 50,000*60 = 3,000,000건
    save_filepath = os.path.join(save_dir, '{}_{}.csv'.format(company_id, datetime.now().strftime('%Y%m%d_%H%M%S')))

    df, stop_msg = data.stocktwit_csv_create(company_id, time_delay=300, limit=30, max_row_num=10000)
    df.to_csv(save_filepath, index=False)
    print('Created', save_filepath)
    if stop_msg == 'forced_stop': break
