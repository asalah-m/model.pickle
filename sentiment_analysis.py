import pickle
import requests
from flask import Flask,jsonify
import json


with open('model.pickle', 'rb') as file:
    model = pickle.load(file)

with open('vectorizer.pickle', 'rb') as file:
    vectorizer = pickle.load(file)



payload={'count':1000 ,'sort_order':'ASC'}
result= requests.get("http://127.0.0.1:3000/get_data",payload,headers={"Content-Type":"application/json"})


requs_text=result.text
data=json.loads(requs_text)




labels=[]
txt=[]
new_txt=[]


for i in data:
    txt.append(i[0])
    labels.append(i[1])

import re
def clean_text(text):
    text = re.sub("@[a-z0-9_]+", ' ', text)
    text = re.sub("[^ ]+\.[^ ]+", ' ', text)
    text = re.sub("[^ ]+@[^ ]+\.[^ ]", ' ', text)
    text = re.sub("[^a-z\' ]", ' ', text)
    text = re.sub(' +', ' ', text)

    return text


for x in txt:
    cleand=clean_text(x)
    new_txt.append(cleand )

    
print (new_txt)
print(labels)


dictt={'count':1000,'label':'positive'}
get_count=requests.get("http://127.0.0.1:3000/get_data_count",dictt,headers={"Content-Type":"application/json"})

req=get_count.text
get=json.loads(req)
print("positive count",get)



vecto = vectorizer.transform(new_txt)
predictions=model.predict(vecto)



from sklearn.metrics import accuracy_score
print("accuracy_scor",accuracy_score(labels, predictions))

    