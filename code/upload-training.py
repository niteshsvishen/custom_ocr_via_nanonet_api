import os, requests, json
from tqdm import tqdm

pathToAnnotations = './annotations/json'
pathToImages = './images'
model_id = os.environ.get('fcbd87bc-64f0-4ba7-8d88-a4ff7110bfda')
api_key = os.environ.get('qoKoKYaUnjCALd6W7gv9IkRui4zffGCt')

for root, dirs, files in os.walk(pathToAnnotations, topdown=False):
    for name in tqdm(files):
        annotation = open(os.path.join(root, name), "r")
        filePath = os.path.join(root, name)
        imageName, ext = name.split(".")
        if imageName == "":
            continue
        imagePath = os.path.join(pathToImages, imageName + '.jpg')
        jsonData = annotation.read()
        url = 'https://app.nanonets.com/api/v2/OCR/Model/fcbd87bc-64f0-4ba7-8d88-a4ff7110bfda/' + '/UploadFile/'
        data = {'file' :open(imagePath, 'rb'),  'data' :('', '[{"filename":"' + imageName+".jpg" + '", "object": '+ jsonData+'}]'),   'modelId' :('', model_id)}       
        response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)
        if response.status_code > 250 or response.status_code<200:
            print(response.text), response.status_code

print("\n\n\nNEXT RUN: python ./code/train-model.py")