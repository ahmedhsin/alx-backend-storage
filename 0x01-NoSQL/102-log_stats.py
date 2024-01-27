#!/usr/bin/env python3
""" 11-main """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    ips = {}
    print(f'{logs.count_documents({})} logs')
    m = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for method in m:
        count = logs.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')
    print(f'{logs.count_documents({"path":"/status"})} status check')
    allLogs = list(logs.find())
    for i in allLogs:
        if i['ip'] in ips:
            continue
        ips[i['ip']] = logs.count_documents({'ip': i['ip']})
    ips = dict(sorted(ips.items(), key=lambda item: item[0], reverse=True))
    print('IPs:')
    for key, value in list(sorted_dict.items())[:10]:
        print(f'\t{key}: {value}') 
