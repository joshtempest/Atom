import requests, json, urllib.request
from PIL import Image
# https://rapidapi.com/kaushalsharma880-GAglnDIvTy/api/programming-memes-images/
url = "https://programming-memes-images.p.rapidapi.com/v1/memes"

headers = {
    'x-rapidapi-host': "programming-memes-images.p.rapidapi.com",
    'x-rapidapi-key': "02d7ce6693msh2f1abdd78e28f3bp128d5bjsna7d6db42c7c8"
    }

response = requests.request("GET", url, headers=headers)
dataDict = response.json()
#print(dataDict)
print(json.dumps(dataDict[0], indent=4))

for img in dataDict:
    image = img['image']

urllib.request.urlretrieve(image,"meme")
img = Image.open("meme")
img.show()
