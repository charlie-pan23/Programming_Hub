import requests
import datetime
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import time
from datetime import timedelta

# import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Welcome to Ether-Trace!")
tk = input("What is your token? ")
tk = tk.upper()
start_time = time.time()
# 替换为你的BscScan API token  A8MMKPADQZBVE1NC6AJFYEJ3FMDX2HMZ7Y
api_token = 'A8MMKPADQZBVE1NC6AJFYEJ3FMDX2HMZ7Y'
input_path = "csv\Chain\eth\\" + tk + "_Eoa_most_frequent.csv"
Price_TD = pd.read_excel('Tools\Price.xlsx')  #获取当前价钱
#初始化变量
contract_address = '0x'
price = 1.00
wei = 18
request_counter = 0  # 请求计数器

if tk == "USDC":
    contract_address = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
    wei = 6
elif tk == "USDT":
    contract_address = '0xdac17f958d2ee523a2206206994597c13d831ec7'
    wei = 6
elif tk == "DAI":
    contract_address = '0x6b175474e89094c44da98b954eedeac495271d0f'
    wei = 18
elif tk == "WBTC":
    contract_address = '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599'
    wei = 8
elif tk == "WETH":
    contract_address = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
    wei = 18
elif tk == "BNB":
    contract_address = '0xb8c77482e45f1f44de1745f52c74426c631bdd52'
tk_rows = Price_TD[Price_TD['Token'] == tk]

# 检查是否有匹配的行
if not tk_rows.empty:
    price = float(tk_rows['Price_TD'].iloc[0])
    # print(price)


# 读取地址列表
def read_csv_file(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


# 写入
def write_to_csv(df, path):
    df.to_csv(path, index=False)
    print("Written in.")


# 获取某个地址的第一笔数额大于10000的交易
def fetch_transactions(address):
    page = 1
    n = 1
    while n<=20:
        try:
            # Build API request URL
            if tk == "ETH":
                url = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&page={page}&offset=10&sort=desc&apikey={api_token}'
            else:
                url = f'https://api.etherscan.io/api?module=account&action=tokentx&address={address}&contractaddress={contract_address}&page={page}&offset=10&sort=desc&apikey={api_token}'

            # Send request
            response = requests.get(url)
            n+=1
            print(response.status_code)
            # print(response.json())


            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()

                if data['status'] == '1':
                    transactions = data['result']
                    if not transactions:
                        break
                    for tx in transactions:
                        # wei = int(tx['tokenDecimal'])
                        value = int(tx['value']) / 10 ** wei * price  # Convert to token units
                        if value > 10000:  # Filter transactions greater than 10000
                            timestamp = int(tx['timeStamp'])
                            date_time = datetime.datetime.utcfromtimestamp(timestamp)  # Convert to UTC time
                            tx_hash = tx['hash']  # Get transaction hash
                            txn_type = 'in' if tx['to'] == address else 'out'  # Determine transaction type
                            print(
                                f"Date (UTC): {date_time} From: {tx['from']} To: {tx['to']} Value: {value}  Hash: {tx_hash}")

                            return address, date_time, tx_hash, value, tx['from'], tx['to'], txn_type
                    page += 1
                else:
                    print(f"API Error: {data['message']}")
                    break
            else:
                print(f'Failed to fetch data. HTTP Status code: {response.status_code}')
                break

        except requests.exceptions.ProxyError:
            print(f"Proxy Error: Unable to connect using the provided proxy for address {address}.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    return address, None, None, None, None, None, None


def prt_time():  #打印当前运行时间
    ntime_ = time.time() - start_time
    ntime = timedelta(seconds=ntime_)
    print(ntime)


# 从CSV文件中读取地址列表
df = read_csv_file(input_path)
if df is not None:
    addresses = df['Address'].tolist()

    # 新列初始化，并显式指定数据类型
    df['Date Times'] = ''
    df['Txhash'] = ''
    df['Value (USD)'] = 0.0
    df['From'] = ''
    df['To'] = ''
    df['Transfer Type'] = ''

    # 使用多线程进行API请求
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_address = {executor.submit(fetch_transactions, address): address for address in addresses}
        for future in as_completed(future_to_address):
            address, date_time, tx_hash, value, frm, to, txn_type = future.result()
            request_counter += 1  # 更新请求计数器
            # print(request_counter)

            if date_time:
                # 更新DataFrame中的相应列
                df.loc[df['Address'] == address, 'Date Times'] = date_time
                df.loc[df['Address'] == address, 'Txhash'] = tx_hash
                df.loc[df['Address'] == address, 'Value (USD)'] = value
                df.loc[df['Address'] == address, 'From'] = frm
                df.loc[df['Address'] == address, 'To'] = to
                df.loc[df['Address'] == address, 'Transfer Type'] = txn_type

            if request_counter % 20 == 0:
                write_to_csv(df, input_path)
                prt_time()

    # df['Value (USD)'] = df['Value (USD)'].apply(lambda x: '${:,.2f}'.format(x))
    # 保存结果到原CSV文件
    try:
        df.to_csv(input_path, index=False)
        print("Results saved successfully.")
    except Exception as e:
        print(f"Error saving CSV file: {e}")
else:
    print("No data to process.")
# 总用时
prt_time()
