import requests, os, json

model_id = os.environ.get('fcbd87bc-64f0-4ba7-8d88-a4ff7110bfda')
api_key = os.environ.get('qoKoKYaUnjCALd6W7gv9IkRui4zffGCt')

url = 'https://app.nanonets.com/api/v2/OCR/Model/fcbd87bc-64f0-4ba7-8d88-a4ff7110bfda/'

response = requests.request('GET', url, auth=requests.auth.HTTPBasicAuth(api_key,''))

state = json.loads(response.text)["state"]
status = json.loads(response.text)["status"]

if state != 5:
	print("The model isn't ready yet, its status is:", status)
	print("We will send you an email when the model is ready. If you are impatient, run this script again in 10 minutes to check.")
else:
	print("NEXT RUN: python ./code/prediction.py ./images/151.jpg")