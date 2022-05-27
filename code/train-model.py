import requests, os

model_id = os.environ.get('fcbd87bc-64f0-4ba7-8d88-a4ff7110bfda')
api_key = os.environ.get('qoKoKYaUnjCALd6W7gv9IkRui4zffGCt')

url = 'https://app.nanonets.com/api/v2/OCR/Model/fcbd87bc-64f0-4ba7-8d88-a4ff7110bfda/' + '/Train/'

querystring = {'modelId': model_id}

response = requests.request('POST', url, auth=requests.auth.HTTPBasicAuth(api_key, ''), params=querystring)

print(response.text)

print("\n\nNEXT RUN: python ./code/model-state.py")