import requests

url= 'https://archive.ics.uci.edu/static/public/53/iris.zip'
response = requests.get(url)

with open ('iris.zip', mode='wb') as f: 
    f.write(response.content)


import hashlib
filename = 'iris.zip'
with open(filename, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()
    
uci_iris_sha256 = 'd11fe30213d36434a0879aab7cb00ce3c812eb7ba2495874438abff7b7b762e9'
if uci_iris_sha256 != sha256hash:
    print("Computed hash does not match expected hash")
else:
    print("Computed hash matches expected hash")