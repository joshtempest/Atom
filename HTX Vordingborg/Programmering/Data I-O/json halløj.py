import requests, json

users=requests.get('https://jsonplaceholder.typicode.com/comments')

dataDict = users.json()
print(len(dataDict), 'comments')
if len(dataDict) > 0:
    print('Keys:')
    for key in dataDict[0]:
        print('-', key, '({})'.format(type(key)))

    print(json.dumps(dataDict[0], indent=4))
