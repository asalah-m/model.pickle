import pickle
import requests
from flask import Flask , jsonify



with open('model.pickle', 'rb') as file:
    model = pickle.load(file)

with open('vectorizer.pickle', 'rb') as file:
    vectorizer = pickle.load(file)
    

payload={'count':1000 ,'sort_order':'ASC'}
result= requests.get("http://127.0.0.1:3000/get_data",payload, headers={"Content-Type":"application/json"})
print(result.json())


dictt={'count':1000,'label_name':'positive' }
get_data_count=requests.get("http://127.0.0.1:3000/get_data_count",dictt,headers={"Content-Type":"application/json"})
print(get_data_count.json())



labels=[]
txt=[]
new_txt=[]

for i in result:
    txt.append(i.index(0))
    labels.append(i.index(1))




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
    new_txt.append(cleaned )


vector = vectorizer.transform(new_txt)
predictions = model.predict(vector)
print(result)




from sklearn.metrics import accuracy_score
print(accuracy_score(labels, predictions))