import requests

url = "https://bscscan.com/tokentxns?a=0x058a871358c1b01039a265635ea282c3f435a9ed&p=1"

# Request headers 装成人
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

# Send GET request
response = requests.get(url, headers=headers)

# Check response status code
if response.status_code == 200:
    print(f"请求成功，状态码: {response.status_code}")
    print(response.text)