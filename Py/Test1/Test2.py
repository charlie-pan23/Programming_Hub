import pandas as pd

# 读入xlsx文件
file_path = 'D:\\Programming_Hub\\Py\\Test1\\XLSX\\0x0966602e47f6a3ca5692529f1d54ecd1d9b09175.xlsx'
df = pd.read_excel(file_path)

ID = '0x0966602e47f6a3ca5692529f1d54ecd1d9b09175'
ID = ID.upper()
ID = str(ID)

# df['To'] = df['To'].astype(str).str.strip().str.upper()
df['To'] = df['To'].str.upper()

df1 = df
df2 = df
# 创建ExcelWriter对象
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    # 将df1输出到名为'Sheet1'的工作表
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    
    # 将df2输出到名为'Sheet2'的工作表
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
# for i, row in df.iterrows():
#     if row['To'] != ID:
#         print(f"Row {i}: {row['To']} != {ID}")

# ID = str(ID)
# 按照'To'列筛选数据
# aa = df[df['To'] == ID]  # 'To'等于ID的行
# ab = df[df['To'] != ID]  # 'To'不等于ID的行

# outpath1="D:\Programming_Hub\Py\Test1\In.xlsx"
# outpath2="D:\Programming_Hub\Py\Test1\Out.xlsx"

# aa.to_excel(outpath1, sheet_name='in' ,index=True)
# ab.to_excel(outpath2, sheet_name='out' ,index=True)


