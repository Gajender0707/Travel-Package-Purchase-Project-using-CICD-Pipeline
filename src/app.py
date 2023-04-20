from flask import Flask, render_template,request
import pandas as pd
from prediction_pipeline import Dataframe,Prediction


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST","GET"])
def predict():
    if request.method=="GET":
        return render_template("index.html")
    else:
        data=Dataframe(
        age=request.form["age"],
        prefferedpropertystar=request.form["prefferedpropertystar"],
        typeofcontact=request.form["typeofcontact"],
        maritalstatus=request.form["maritalstatus"],
        citytier=request.form["citytier"],
        numberoftrips=request.form["numberoftrips"],
        durationofpitch=request.form["durationofpitch"],
        passport=request.form["passport"],
        pitchsatisfactionscore=request.form["pitchsatisfactionscore"],
        occupation=request.form["occupation"],
        gender=request.form["gender"],
        owncar=request.form["owncar"],
        numberofpersonvisiting=request.form["numberofpersonvisiting"],
        numberofchildrenvisiting=request.form["numberofchildrenvisiting"],
        numberoffollowups=request.form["numberoffollowups"],
        designation=request.form["designation"],
        productpitched=request.form["productpitched"],
        monthlyincome=request.form["monthlyincome"])

        df=data.get_values_as_dataframe()

        preds=Prediction()
        output=preds.Predict_class(df)
        if output[0]==1:
            res="Take"
            return render_template("result.html",res=res)
        else:
            res="Not Take"
            return render_template("result.html",res=res)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)