from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("house.pkl")

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
        UC = request.form["Under Construction"]
        uc = int(UC)
        print(uc)
        RERA = request.form["RERA"]
        RERA = int(RERA)
        print(RERA)
        BHK = request.form["BHK"]
        BHK = int(BHK)
        print(uc)
        SQFT = request.form["SQFT"]
        SQFT = float(SQFT)
        print(SQFT)      
        list1=[[uc,RERA,BHK,SQFT]]  
        print(list1)
        price = np.abs(model.predict(list1))
        return render_template('index.html',prediction_text="Price in Lakhs={}".format(price))

if __name__ == "__main__":
    app.run()
