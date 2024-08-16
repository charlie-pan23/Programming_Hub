# get_html 说明

## 主要实现功能
get_html包 能够追踪按照格式放入.csv文件的地址，并在原始表格后面添加相应的数据列。    


一共添加以下列：    
| 列名 | 备注 |
| --- | --- |
|_Date Time (UTC)_| 最后一次大额交易的UTC时间 |    
|_Txhash_| 交易哈希值|   
|_Value (USD)_|交易金额（根据amount基于当前汇率计算得）|     
|_From_| - |    
|_To_| - |    
|_Transfer Type_| 进账/出账（in/out）|     

## 使用说明
* __在get_html.py中替换自己的API key__     
* __使用前先运行Get_Price.py以获得当前汇率__    
* __将想要查询的地址存入csv文件夹中对应币种的.csv文件并保存__   
* __运行get_html.py，按照提示输入币种__    
* __是否沉淀需要自己判断，具体操作为，在经过处理的表格后面增加列 *是否沉淀* 并输入代码__
` =IF(ISBLANK(F2),"",IF(F2<DATE(2024,1,1),"yes","")) `


## 数据来源
追踪数据来自:BSC: https://bscscan.com/      
            Matic: https://polygonscan.com/
            ETH: https://etherscan.io/
实时汇率来自：https://www.coingecko.com/


## 存在问题
* 部分大额转账被分成多笔小额转账可能会错过追踪。
* Get_Price需要打开代理才能使用。
* 在使用免费API时，有每秒至多五次请求和每天查询100,000条数据的限制，数据量大时搜索速度极慢。
* 雪崩链暂不兼容这个方法


