from flask import Flask , render_template , redirect ,request
import json
import requests
import numpy as np
import urllib.request
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/data',methods=[ 'POST' ])
def login():

    if request.method=='POST':
      
        data = Image.open(request.files["data"].stream).convert("L")
        data=data.resize((28,28))
        Image_array=np.array(data)
        normalised_data=Image_array/255.0
        re_shape=normalised_data.reshape(1,-1)
        list_data=re_shape.tolist()
        print(normalised_data.shape)
        print("***************")
        print(normalised_data)
        print(list_data)

        json_input=json.dumps({"data":list_data})


        print(data)
        print(type(data))

        
        url = 'http://f50edca4-c772-43a1-82d2-c4df15b418c0.eastus.azurecontainer.io/score'
        headers = {'Content-Type':'application/json'}
        r = requests.post(url,json_input,headers=headers)
        res=r.text
        print(res)

        return render_template("resp.html", res=res)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)

 