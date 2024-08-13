import requests
import datetime
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import time
from datetime import timedelta

# import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Welcome to MATIC-Trace!")
tk = input("What is your token? ")
tk = tk.upper()
start_time = time.time()
# 替换为你的BscScan API token  4XE15VKVY9MMA6384FZPXSW3BMR21SQ3T3
api_token = '4XE15VKVY9MMA6384FZPXSW3BMR21SQ3T3'
input_path = "csv\Chain\polygon\\" + tk + "_Eoa_most_frequent.csv"
Price_TD = pd.read_excel('Tools\Price.xlsx')  #获取当前价钱
#初始化变量
contract_address = '0x'
price = 1.00
wei = 18
request_counter = 0  # 请求计数器

if tk == "USDC":
    contract_address = '0x3c499c542cef5e3811e1192ce70d8cc03d5c3359'
    wei = 6
elif tk == "USDT":
    contract_address = '0xc2132d05d31c914a87c6611c10748aeb04b58e8f'
    wei = 6
elif tk == "DAI":
    contract_address = '0x8f3cf7ad23cd3cadbd9735aff958023239c6a063'
    wei = 18
elif tk == "WBTC":
    contract_address = '0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6'
    wei = 8
elif tk == "WETH":
    contract_address = '0x7ceb23fd6bc0add59e62ac25578270cff1b9f619'
    wei = 18
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
            if tk == "MATIC":
                url = f'https://api.polygonscan.com/api?module=account&action=txlist&address={address}&page={page}&offset=10&sort=desc&apikey={api_token}'
            else:
                url = f'https://api.polygonscan.com/api?module=account&action=tokentx&address={address}&contractaddress={contract_address}&page={page}&offset=10&sort=desc&apikey={api_token}'

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
