import requests

headers={
    'Cookie':"Ecp_ClientId=2211019140802678256; cnkiUserKey=c35e8fac-e42f-7cc7-d518-a0c78adfe841; UM_distinctid=17c972e0596a70-0445dd36efeec4-1a2f1c08-1fa400-17c972e0597ac4; Ecp_IpLoginFail=21110160.30.241.14; KNS_DisplayModel=listmode@CFLS; RsPerPage=50; _pk_ses=*; ASP.NET_SessionId=wpao4cvi4w4pyxfvwstrewlu; SID_kns=015123128; SID_klogin=125144; SID_crrs=125133; KNS_SortType=SCDB!(FFD%2c%27RANK%27)+desc; _pk_id=ea84f5c3-888d-4d01-8af9-1b6a0fd51341.1634623717.6.1635834751.1635834490.",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}
params={
    "pagename": "ASP.brief_default_result_aspx",
    "isinEn": "1",
    "dbPrefix": "SCDB",
    "dbCatalog": "中国学术文献网络出版总库",
    "ConfigFile": "SCDBINDEX.xml",
    "research": "off",
    "t": "1635834740878",
    "keyValue": "CGSS",
    "S": "1",
    "sorttype": "(FFD,'RANK') desc",
    "queryid": "18"
}
session=requests.Session()
content=session.get("https://kns.cnki.net/kns/brief/brief.aspx",headers=headers,params=params)
print(content.text)
