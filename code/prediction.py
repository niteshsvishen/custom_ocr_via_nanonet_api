import requests, os, sys

model_id = os.environ.get('fcbd87bc-64f0-4ba7-8d88-a4ff7110bfda')
api_key = os.environ.get('qoKoKYaUnjCALd6W7gv9IkRui4zffGCt')
image_path = sys.argv[1]

url = 'https://app.nanonets.com/api/v2/OCR/Model/fcbd87bc-64f0-4ba7-8d88-a4ff7110bfda/LabelFile/'

data = {'file': open(image_path, 'rb'),    'modelId': ('', model_id)}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

print(response.text)