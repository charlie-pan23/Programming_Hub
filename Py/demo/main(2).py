import requests
from bs4 import BeautifulSoup
import re
import logging
import json
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue

'''
# Proxy settings
proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
}
'''

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

Token = "Binance-Peg BSC-USD(BSC-USD)"
STOP_AMOUNT = 10000

def fetch_page_content(url, headers, session):
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None

def extract_quick_export_data(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        script_tags = soup.find_all('script')
        for script in script_tags:
            if 'quickExportTokentxnsData' in script.text:
                quick_export_data = re.search(r'const quickExportTokentxnsData = (.*?);', script.text)
                if quick_export_data:
                    return quick_export_data.group(1)
        logging.warning("quickExportTokentxnsData not found in the script tags.")
        return None
    except Exception as e:
        logging.error(f"Failed to extract quick export data: {e}")
        return None

def extract_max_page_number(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        page_info = soup.find('span', class_='page-link text-nowrap')
        if page_info:
            max_page_number = int(page_info.text.split()[-1])
            return max_page_number
        logging.warning("Page information not found in the HTML content.")
        return None
    except Exception as e:
        logging.error(f"Failed to extract max page number: {e}")
        return None

def process_transaction_data(quick_export_data, address):
    try:
        transactions = json.loads(quick_export_data)
    except json.JSONDecodeError as e:
        logging.error(f"JSONDecodeError: {e}")
        return None

    for txn in transactions:
        if txn['Token'] == Token:
            date_time = txn['DateTime']
            value = txn['Value']
            txn_type = 'in' if txn['Receiver'] == address else 'out'
            amount = float(value.replace('$', '').replace(',', ''))
            txn_hash = txn['Txhash']
            print(f"Txhash: {txn_hash}, DateTime (UTC): {date_time}, Value: {value}, Type: {txn_type}")
            if amount > STOP_AMOUNT and txn_type == 'in':
                return {
                    "Txhash": txn_hash,
                    "DateTime": date_time,
                    "Value": value,
                    "Transfer Type": txn_type
                }
    return None

def process_address(address, headers, session):
    url = f"https://bscscan.com/tokentxns?a={address}"

    # Get max page number
    html_content = fetch_page_content(url, headers, session)
    if html_content:
        max_page_number = extract_max_page_number(html_content)
        if max_page_number:
            logging.info(f"Maximum page number for {address}: {max_page_number}")
        else:
           None
    else:
        return None

    # Read data from each page
    for page in range(1, max_page_number + 1):
        page_url = f"https://bscscan.com/tokentxns?a={address}&p={page}"
        html_content = fetch_page_content(page_url, headers, session)
        if html_content:
            quick_export_data = extract_quick_export_data(html_content)
            if quick_export_data:
                logging.info(f"Page {page} quickExportTokentxnsData: {quick_export_data}")
                if quick_export_data:
                    # Remove leading/trailing whitespace and quotes for safe JSON parsing
                    quick_export_data = quick_export_data.strip().strip("'\"")
                    transaction_data = process_transaction_data(quick_export_data, address)
                    if transaction_data:
                        return transaction_data
            else:
                logging.warning(f"quickExportTokentxnsData not found on page {page} for {address}")
        else:
            logging.warning(f"Failed to fetch content for page {page} for {address}")
    return None

def main():
    start_time = time.time()

    file_path = r'D:\Programming_Hub\Py\demo\demo.csv'
    data = pd.read_csv(file_path)
    addresses = data['Address']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }

    results = Queue()
    address_times = Queue()

    def process_and_record(address):
        with requests.Session() as session:
            address_start_time = time.time()
            result = process_address(address, headers, session)
            address_end_time = time.time()
            address_duration = address_end_time - address_start_time
            address_times.put({
                "Address": address,
                "Time (s)": address_duration
            })
            if result:
                result["Address"] = address
                results.put(result)

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_and_record, address) for address in addresses]

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logging.error(f"Error processing address: {e}")

    # Collect results from the queues
    results_list = []
    while not results.empty():
        results_list.append(results.get())

    address_times_list = []
    while not address_times.empty():
        address_times_list.append(address_times.get())

    results_df = pd.DataFrame(results_list)
    merged_df = pd.merge(data, results_df, on="Address", how="left")
    merged_df.to_csv(file_path, index=False)

    total_duration = time.time() - start_time

    print("Results saved to CSV.")
    print(f"Total execution time: {total_duration:.2f} seconds")


if __name__ == "__main__":
    main()
