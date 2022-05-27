import requests, os
  
url = "https://app.nanonets.com/api/v2/OCR/Model/fcbd87bc-64f0-4ba7-8d88-a4ff7110bfda/"
api_key = os.environ.get('qoKoKYaUnjCALd6W7gv9IkRui4zffGCt')

payload = "{\"categories\" : [\"BIN_NO\"], \"model_type\": \"ocr\"}"
headers = {'Content-Type': "application/json",}

response = requests.request("POST", url, headers=headers, auth=requests.auth.HTTPBasicAuth(api_key, ''))
model_id = "fcbd87bc-64f0-4ba7-8d88-a4ff7110bfda"

print("NEXT RUN: export NANONETS_MODEL_ID=" + model_id)
print("THEN RUN: python ./code/upload-training.py")
