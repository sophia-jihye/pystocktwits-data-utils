from pystocktwits_data_utils import PyStockTwitData
from datetime import datetime
import argparse
import os

data_dir = './scraped_data'

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default="companies")
args = parser.parse_args()

mode = args.mode

def start_one_file(company_ids, time_delay, save_dir):
    if not os.path.exists(save_dir): os.makedirs(save_dir)
    df, stop_msg = data.stocktwit_csv_create(company_ids, time_delay=time_delay, limit=30, max_row_num=50000)
    save_filepath = os.path.join(save_dir, '{}_{}.csv'.format(datetime.now().strftime('%Y%m%d_%H%M%S'), len(df)))
    df.to_csv(save_filepath, index=False)
    print('Created', save_filepath)
    return stop_msg

data = PyStockTwitData()

for _ in range(60):   # 목표: 50,000*60 = 3,000,000건
    if mode == 'companies':   # 2021.10.06 현재 S&P 500에 속하는 회사 505개 
        company_ids = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'FB', 'GOOG', 'TSLA', 'BRK.B',
       'JPM', 'NVDA', 'JNJ', 'V', 'UNH', 'HD', 'PG', 'BAC', 'DIS', 'MA',
       'PYPL', 'NFLX', 'ADBE', 'CRM', 'XOM', 'CMCSA', 'PFE', 'CSCO', 'VZ',
       'TMO', 'INTC', 'MRK', 'PEP', 'KO', 'ABT', 'ACN', 'CVX', 'AVGO',
       'T', 'COST', 'WMT', 'WFC', 'ABBV', 'DHR', 'NKE', 'MCD', 'LLY',
       'TXN', 'MDT', 'NEE', 'LIN', 'PM', 'HON', 'ORCL', 'LOW', 'C',
       'INTU', 'QCOM', 'MS', 'UNP', 'RTX', 'SBUX', 'BMY', 'UPS', 'IBM',
       'GS', 'BA', 'NOW', 'AMD', 'AMT', 'AMGN', 'BLK', 'ISRG', 'GE',
       'AMAT', 'MRNA', 'TGT', 'AXP', 'CVS', 'SCHW', 'CAT', 'MMM', 'BKNG',
       'SPGI', 'DE', 'COP', 'CHTR', 'PLD', 'ZTS', 'ANTM', 'ADI', 'SYK',
       'MO', 'LMT', 'GILD', 'ADP', 'PNC', 'USB', 'MDLZ', 'TFC', 'MU',
       'TJX', 'LRCX', 'GM', 'DUK', 'MMC', 'CB', 'CCI', 'FIS', 'COF',
       'TMUS', 'EL', 'EQIX', 'CME', 'BDX', 'SHW', 'CSX', 'CI', 'EW', 'SO',
       'ICE', 'FISV', 'AON', 'CL', 'NSC', 'BSX', 'HCA', 'ADSK', 'ATVI',
       'ITW', 'D', 'ETN', 'REGN', 'WM', 'MCO', 'APD', 'F', 'EMR', 'ILMN',
       'NOC', 'FDX', 'ECL', 'PGR', 'IDXX', 'DXCM', 'CMG', 'EOG', 'KLAC',
       'NXPI', 'HUM', 'JCI', 'DG', 'MSCI', 'FCX', 'AIG', 'EXC', 'ROP',
       'TWTR', 'ALGN', 'A', 'VRTX', 'TEL', 'GPN', 'IQV', 'INFO', 'GD',
       'PSA', 'MET', 'CARR', 'KMB', 'SNPS', 'APH', 'TROW', 'LHX', 'NEM',
       'EBAY', 'SPG', 'DOW', 'SLB', 'APTV', 'MAR', 'MTCH', 'BK', 'SYY',
       'TT', 'AEP', 'BIIB', 'ORLY', 'DLR', 'CDNS', 'PRU', 'EA', 'PXD',
       'MPC', 'BAX', 'SRE', 'MCHP', 'ROST', 'MSI', 'FTNT', 'CTSH', 'HLT',
       'SIVB', 'TRV', 'DFS', 'ALL', 'PH', 'GIS', 'RMD', 'PAYX', 'DD',
       'XLNX', 'SBAC', 'CNC', 'YUM', 'STZ', 'AZO', 'WELL', 'OTIS', 'FRC',
       'XEL', 'IFF', 'ADM', 'PPG', 'ROK', 'CTAS', 'HPQ', 'TDG', 'WBA',
       'CBRE', 'WMB', 'PSX', 'KMI', 'MNST', 'CMI', 'LUV', 'AFL', 'VRSK',
       'MTD', 'STT', 'AVB', 'CTVA', 'MCK', 'AWK', 'PEG', 'EFX', 'AJG',
       'ZBH', 'VLO', 'WLTW', 'WST', 'AMP', 'FITB', 'KEYS', 'FAST', 'BLL',
       'ES', 'ANSS', 'DAL', 'CPRT', 'NUE', 'AME', 'EQR', 'SYF', 'OXY',
       'WEC', 'SWK', 'GLW', 'PCAR', 'DHI', 'KR', 'ARE', 'ZBRA', 'WY',
       'OKE', 'LH', 'ODFL', 'SWKS', 'O', 'IT', 'FTV', 'GNRC', 'LEN', 'ED',
       'URI', 'RSG', 'CDW', 'ALB', 'KSU', 'HSY', 'CZR', 'LYB', 'HIG',
       'DVN', 'EXPE', 'ETSY', 'KHC', 'PAYC', 'BBY', 'VIAC', 'HBAN',
       'GRMN', 'TSN', 'DLTR', 'HES', 'VMC', 'NTRS', 'EXR', 'DOV', 'TSCO',
       'VFC', 'CTLT', 'MAA', 'NDAQ', 'DTE', 'PPL', 'MLM', 'FLT', 'XYL',
       'KEY', 'EIX', 'WAT', 'ESS', 'VTR', 'AEE', 'BKR', 'IP', 'RF',
       'CERN', 'CFG', 'HAL', 'TRMB', 'IR', 'ETR', 'DRI', 'ULTA', 'COO',
       'CCL', 'STE', 'CHD', 'CLX', 'MKC', 'TDY', 'NTAP', 'RCL', 'KMX',
       'VRSN', 'CRL', 'MPWR', 'MTB', 'FE', 'ENPH', 'EXPD', 'HPE', 'PKI',
       'ANET', 'BR', 'TECH', 'TYL', 'DRE', 'CTRA', 'PEAK', 'QRVO', 'TTWO',
       'HOLX', 'AMCR', 'MGM', 'CMS', 'TFX', 'FANG', 'ABC', 'WDC', 'GPC',
       'POOL', 'DPZ', 'GWW', 'DGX', 'RJF', 'AVY', 'J', 'CE', 'CINF',
       'STX', 'WAB', 'BBWI', 'AKAM', 'TER', 'UAL', 'K', 'CAG', 'VTRS',
       'PFG', 'NVR', 'BXP', 'MKTX', 'IEX', 'OMC', 'PWR', 'TXT', 'BIO',
       'AES', 'CDAY', 'UDR', 'CNP', 'IPG', 'NLOK', 'CAH', 'EVRG', 'ABMD',
       'LNT', 'EMN', 'JBHT', 'MAS', 'LKQ', 'AAL', 'AAP', 'WRK', 'FOXA',
       'BRO', 'PKG', 'MOS', 'KIM', 'CTXS', 'CBOE', 'LDOS', 'SJM', 'CF',
       'WHR', 'LYV', 'LUMN', 'IRM', 'FBHS', 'XRAY', 'INCY', 'PTC', 'BF.B',
       'HWM', 'LNC', 'JKHY', 'LVS', 'PHM', 'PNR', 'ATO', 'FFIV', 'HST',
       'MRO', 'FMC', 'ALLE', 'HRL', 'SNA', 'RHI', 'CHRW', 'DISH', 'PENN',
       'L', 'HAS', 'CMA', 'HSIC', 'BWA', 'TPR', 'REG', 'WRB', 'ZION',
       'UHS', 'RE', 'NCLH', 'MHK', 'NRG', 'NI', 'AIZ', 'NWSA', 'LW',
       'JNPR', 'TAP', 'WYNN', 'DXC', 'CPB', 'FRT', 'NWL', 'GL', 'APA',
       'PNW', 'OGN', 'SEE', 'WU', 'IVZ', 'AOS', 'BEN', 'HII', 'ROL',
       'DVA', 'ALK', 'PVH', 'PBCT', 'DISCK', 'NLSN', 'VNO', 'LEG', 'HBI',
       'RL', 'FOX', 'IPGP', 'GPS', 'DISCA', 'UAA', 'UA', 'NWS']
        time_delay = 300
        save_dir = os.path.join(data_dir, mode)
        stop_msg = start_one_file(company_ids, time_delay, save_dir)
    
    elif mode == 'indices':
        company_ids = ['SPY', 'DJIA']
        time_delay = 300
        save_dir = os.path.join(data_dir, mode)
        stop_msg = start_one_file(company_ids, time_delay, save_dir)
        
    if stop_msg == 'forced_stop': break
