import requests

adult_sha256='7537312dd56c2b98035880805ce99e68183a30ee468aa5329d6df0fbb3cc21bb'
adult_reconstruction_sha256='7537312dd56c2b98035880805ce99e68183a30ee468aa5329d6df0fbb3cc21bb'

url= 'https://archive.ics.uci.edu/static/public/2/adult.zip'
response = requests.get(url)

with open ('adult.zip', mode='wb') as f: 
    f.write(response.content)

url2= 'https://raw.githubusercontent.com/socialfoundations/folktables/main/adult_reconstruction.csv'
response2 = requests.get(url)

with open ('adult_reconstruction.csv', mode='wb') as f: 
    f.write(response2.content)
    
import hashlib
filename = 'adult.zip'
with open(filename, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()
    
if adult_sha256 != sha256hash:
    print("Computed hash does not match expected hash")
else:
    print("Computed hash matches expected hash")

filename2 = 'adult_reconstruction.csv'
with open(filename2, mode='rb') as f:
    data2 = f.read()
    sha256hash2 = hashlib.sha256(data2).hexdigest()
    
if adult_reconstruction_sha256 != sha256hash2:
    print("Computed hash does not match expected hash")
else:
    print("Computed hash matches expected hash")