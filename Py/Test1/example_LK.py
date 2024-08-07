import os
import re
import pandas as pd

# Define the base paths
input_base_path = r'C:\Users\HUAWEI\Desktop\token\Chain\BSC\\'
output_base_path = r'C:\Users\HUAWEI\Desktop\token\Chain\BSC\\'

tokens = { "DAI", "ETH", "USDC","BTCB","BNB","USDT"}

# Loop through each token in the set
for token in tokens:
    input_file_path = os.path.join(input_base_path, token + '.txt')
    token_output_folder = os.path.join(output_base_path, token)

    # Create a folder for the token if it doesn't exist
    os.makedirs(token_output_folder, exist_ok=True)

    # Open and read the content of the input file with the correct encoding
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        with open(input_file_path, 'r', encoding='gbk') as file:
            content = file.read()

    # Use regular expressions to parse the data
    pattern = re.compile(
        r'(?P<Address>0x[a-fA-F0-9]{40})\n(?P<Address_Tag>[^\n]*)\n(?P<Type>[^\n]+)\n(?P<Token_Balance>[\d,\.]+)\n(?P<Percentage>[\d\.]+%)'
    )
    matches = pattern.findall(content)

    # Convert matches to a DataFrame
    data = pd.DataFrame(matches, columns=['Address', 'Address Tag', 'Type', 'Token Balance', 'Percentage'])

    # Count the number of addresses for each type
    address_counts = data['Type'].value_counts()

    # Find the type with the most addresses
    most_frequent_type = address_counts.idxmax()
    most_frequent_data = data[data['Type'] == most_frequent_type]

    # Print the number of addresses for each type
    print("\n")
    print(token)
    print(f"Address counts for {token}:")
    for address_type, count in address_counts.items():
        print(f"{address_type}: {count}")
    print("\n")

    # Save the DataFrame of the most frequent type to a CSV file named 'most_frequent.csv'
    most_frequent_output_path = os.path.join(token_output_folder, 'most_frequent.csv')

    # Save separate DataFrames for each address type (Eoa, Dex, Exchange) and mark the most frequent one
    for address_type in ['Eoa', 'Dex', 'Exchange']:
        address_type_data = data[data['Type'] == address_type]
        if not address_type_data.empty:
            if address_type == most_frequent_type:
                address_type_output_file_path = os.path.join(token_output_folder, f'{token}_{address_type}_most_frequent.csv')
            else:
                address_type_output_file_path = os.path.join(token_output_folder, f'{token}_{address_type}.csv')
            address_type_data.to_csv(address_type_output_file_path, index=False)
