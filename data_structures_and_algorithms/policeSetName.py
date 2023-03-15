# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: policeSetName.py
@time: 2023/3/13 17:43
"""

import requests

headers = {
    'cookie': 'Hm_lvt_8506537a5bb9e3b42110f54275d10fcd=1665974806; TSESSIONID=DCYJ3A6V-QV61HUGMEBPJQCU4DU6P2-077FCSEL-4IX6D; _lang_=zh_CN; TSESSIONID_2.0=DCYJ3A6V-QV61HUGMEBPJQCU4DU6P2-077FCSEL-4IX6D_2.0; Hm_lvt_10fe8b1c34ca2f19a201dd50508153a2=1677836323; TDCP_US=adda8af44b794b4592345170ccb3cc31; Hm_lpvt_10fe8b1c34ca2f19a201dd50508153a2=1678700500'
}

policySetList = []

resp = requests.get(url='https://bastion.tongdun.cn/contentsecurity/content/partnerTextAudit.json?operationType=queryTextAuditList&&riskStatus=All&&dataSource=&&hitReason=&&content=&&account=&&sequenceId=&&productId=&&ip=&&feedbackStatus=&&pageSize=10&&currentPage=1&&eventType=&&startTime=2023-03-07 00:00:00&&endTime=2023-03-13 23:59:59', headers=headers).json()

for each in resp['attr']['data']:
    if each['policySetName'] not in policySetList:
        policySetList.append(each['policySetName'])

print(policySetList)


