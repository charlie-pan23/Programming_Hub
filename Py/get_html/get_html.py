import requests
import datetime
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
tk = input("What is your token? ")

# 替换为你的BscScan API token
api_token = '8DHTWHC7K1R1YBUJPYRKRPT2P3KU8C6WG3'
input_path = "csv\\"+tk+".csv"
Price_TD = pd.read_excel('Get_Price\Price.xlsx') #获取当前价钱
#初始化变量
contract_address = '0x'
price = 1.00

# '''
if tk=="BTCB":
    contract_address = '0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c'
elif tk=="ETH":
    contract_address = '0x2170ed0880ac9a755fd29b2688956bd959f933f8'
elif tk=="USDT":
    contract_address = '0x55d398326f99059ff775485246999027b3197955'
elif tk=="USDC":
    contract_address = '0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d'
elif tk=="DAI":
    contract_address = '0x1af3f329e8be154074d8769d1ffa4ee058b1dbc3'

tk_rows = Price_TD[Price_TD['Tocken'] == tk]

# 检查是否有匹配的行
if not tk_rows.empty:
    price = float(tk_rows['Price_TD'].iloc[0])
    # print(price)


# 读取地址列表
def read_csv_file(path):
    df = pd.read_csv(path)
    return df

# 获取某个地址的第一笔数额大于10000的交易
def fetch_transactions(address):
    page = 1
    while True:
        # 构建API请求URL
        url = f'https://api.bscscan.com/api?module=account&action=tokentx&address={address}&contractaddress={contract_address}&page={page}&offset=10&sort=desc&apikey={api_token}'

        # 发送请求
        response = requests.get(url)

        # 解析响应
        if response.status_code == 200:
            data = response.json()
            if data['status'] == '1':
                transactions = data['result']
                if not transactions:
                    break
                for tx in transactions:
                    amount = int(tx['value']) / 10 ** 18
                    value = amount * price              # 转换为代币单位
                    if value > 10000:                       # 筛选出数额大于10000的交易
                        timestamp = int(tx['timeStamp'])
                        date_time = datetime.datetime.utcfromtimestamp(timestamp)  # 转换为UTC时间
                        tx_hash = tx['hash']  # 获取交易哈希
                        txn_type = 'in' if tx['to'] == address else 'out'  # 判断交易类型
                        print(
                            f"Date (UTC): {date_time} From: {tx['from']} To: {tx['to']} Value: {value} {tx['tokenSymbol']} Hash: {tx_hash}")

                        return address, date_time, tx_hash, value, tx['from'], tx['to'], txn_type
                page += 1
            else:
                print(f"Error: {data['message']}")
                break
        else:
            print(f'Failed to fetch data. HTTP Status code: {response.status_code}')
            break
    return address, None, None, None, None, None, None

# 从CSV文件中读取地址列表
df = read_csv_file(input_path)
addresses = df['Address'].tolist()

# 新列初始化，并显式指定数据类型
df['Date Times'] = ''
df['Txhash'] = ''
df['Value (USD)'] = 0.0
df['From'] = ''
df['To'] = ''
df['Transfer Type'] = ''

# 使用多线程进行API请求
with ThreadPoolExecutor(max_workers=12) as executor:
    future_to_address = {executor.submit(fetch_transactions, address): address for address in addresses}
    for future in as_completed(future_to_address):
        address, date_time, tx_hash, value, frm, to, txn_type = future.result()
        if date_time:
            # 更新DataFrame中的相应列
            df.loc[df['Address'] == address, 'Date Times'] = date_time
            df.loc[df['Address'] == address, 'Txhash'] = tx_hash
            df.loc[df['Address'] == address, 'Value (USD)'] = value
            df.loc[df['Address'] == address, 'From'] = frm
            df.loc[df['Address'] == address, 'To'] = to
            df.loc[df['Address'] == address, 'Transfer Type'] = txn_type

# df['Value (USD)'] = df['Value (USD)'].apply(lambda x: '${:,.2f}'.format(x))
# 保存结果到原CSV文件
df.to_csv(input_path, index=False)


# BTCB-0x7130d2a12b9bcbfae4f2634d864a1ee1ce3ead9c
# DAI -0x1af3f329e8be154074d8769d1ffa4ee058b1dbc3
# USDT-0x55d398326f99059ff775485246999027b3197955
# USDC-0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d
# ETH -0x2170ed0880ac9a755fd29b2688956bd959f933f8
# '''