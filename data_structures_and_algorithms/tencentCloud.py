# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: tencentCloud.py
@time: 2023/3/15 18:40
"""

import requests

tencentCloudUrl = 'qh-security-1258830046.cos.ap-shanghai.myqcloud.com'


resp = requests.request(method='GET', url=tencentCloudUrl)