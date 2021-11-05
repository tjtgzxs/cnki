import main
import os
import pandas as pd
from pandas import DataFrame
# https://zhuanlan.zhihu.com/p/64474157
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
excel_file=BASE_DIR+os.sep+"test.xls"
# print(excel_file)
df = pd.read_excel(excel_file,sheet_name='2003',keep_default_na=False)
for i in range(0,len(df)):
    # print(df.iloc[i]['论文题目'],df.iloc[i]["使用数据（最新）"])
    if df.iloc[i]["使用数据（最新）"]=="":
        pdf_value = main.PDFHandle(BASE_DIR+os.sep+'pdf'+os.sep+df.iloc[i]['论文题目']+'.pdf')
        if(pdf_value!=False):
            new_value=main.re_find(pdf_value)
            if(new_value==False):
                new_value="12213"
            df.loc[i,"使用数据（最新）"]=new_value
        else:
            df.loc[i, "使用数据（最新）"] = "333"
DataFrame(df).to_excel("./example.xls",index=False, header=True)


