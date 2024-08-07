import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font

Search_ID = str(input("What is the ID of the account? ")) 
exlpath = "D:\Programming_Hub\Py\Test1\XLSX" + "\\"+ Search_ID + ".xlsx"
respath ="D:\Programming_Hub\Py\Test1\\Trace_" + Search_ID + ".xlsx"
# respathin = "D:\Programming_Hub\Py\Test1\In.xlsx"
# respathout = "D:\Programming_Hub\Py\Test1\Out.xlsx"


#统一格式，方便比较 
Search_ID = Search_ID.upper()
Search_ID = str(Search_ID)

rdata = pd.read_excel(exlpath)
rdata['To'] = rdata['To'].str.upper()
#rdata = rdata[rdata['Value (USD)']>=0.01]

# 分成进出两个表
in_rdata = rdata[rdata['To'] == Search_ID]
out_rdata = rdata[rdata['To'] != Search_ID]
# 排序
out_data = out_rdata.sort_values(by='To', ascending=True)
in_data = in_rdata.sort_values(by='From', ascending=True)
# 分类汇总
out_grouped = out_data.groupby('To').agg(
    **{
    "Times":pd.NamedAgg(column='To', aggfunc='count'),
    "Last Time (UTC)": pd.NamedAgg(column='Date Time (UTC)', aggfunc='max'),
    "Total Value (USD)": pd.NamedAgg(column='Value (USD)', aggfunc='sum')
    })
in_grouped = in_data.groupby('From').agg(
    **{
    "Times":pd.NamedAgg(column='From', aggfunc='count'),
    "Last Time (UTC)": pd.NamedAgg(column='Date Time (UTC)', aggfunc='max'),
    "Total Value (USD)": pd.NamedAgg(column='Value (USD)', aggfunc='sum')
    })
# 增加标签
To_tags = out_rdata.drop_duplicates(['To', 'To_NameTag'])[['To', 'To_NameTag']]
From_tags = in_rdata.drop_duplicates(['From', 'From_NameTag'])[['From', 'From_NameTag']]
out_grouped = pd.merge(out_grouped, To_tags, left_index=True, right_on='To', how='left')
in_grouped = pd.merge(in_grouped, From_tags, left_index=True, right_on='From', how='left')
# 去掉多余列
# del out_grouped['To_y']
# del in_grouped['From_y']
print(out_grouped)
# 重命名列名['Transacts with','Times', 'Last Time (UTC)', 'Total Value (USD)','NameTag']
# out_grouped.columns = ['Transacts with','Times', 'Last Time (UTC)', 'Total Value (USD)','NameTag']
# in_grouped.columns = ['Transacts with','Times', 'Last Time (UTC)', 'Total Value (USD)','NameTag']
out_grouped['Direction'] = 'out'
in_grouped['Direction'] = 'in'
# 合并两张表
res= pd.concat([out_grouped,in_grouped],axis=0)
res = res[res['Total Value (USD)']>=1] #设置筛选最低金额
#设置单元格恰当格式，并去除多余空格
res['Total Value (USD)'] = res['Total Value (USD)'].apply(lambda x: '${:,.2f}'.format(x))
res['NameTag'] = res['NameTag'].str.strip()
with pd.ExcelWriter(respath, engine='openpyxl') as writer:
    # 将df1输出到名为'Sheet1'的工作表
    res.to_excel(writer, sheet_name='Sheet1', index=False)



