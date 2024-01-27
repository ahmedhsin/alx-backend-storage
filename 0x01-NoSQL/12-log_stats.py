#!/usr/bin/env python3
""" 11-main """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    print(f'{logs.count_documents({})} logs')
    m = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in m:
        count = logs.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')
    print(f'{logs.count_documents({"path":"/status"})} status check')
