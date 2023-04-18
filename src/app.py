from flask import Flask, render_template,request
import pandas as pd
import pickle
import dill


with open(r"notebook\Model.pkl","rb") as f:
    model=pickle.load(f)

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST","GET"])
def predict():
    if request.method=="POST":
        age=request.form["age"]
        prefferedpropertystar=request.form["prefferedpropertystar"]
        typeofcontact=request.form["typeofcontact"]
        maritalstatus=request.form["maritalstatus"]
        citytier=request.form["citytier"]
        numberoftrips=request.form["numberoftrips"]
        durationofpitch=request.form["durationofpitch"]
        passport=request.form["passport"]
        pitchsatisfactionscore=request.form["pitchsatisfactionscore"]
        occupation=request.form["occupation"]
        gender=request.form["gender"]
        owncar=request.form["owncar"]
        numberofpersonvisiting=request.form["numberofpersonvisiting"]
        numberofchildrenvisiting=request.form["numberofchildrenvisiting"]
        numberoffollowups=request.form["numberoffollowups"]
        designation=request.form["designation"]
        productpitched=request.form["productpitched"]
        monthlyincome=request.form["monthlyincome"]

        data_points={
            "Age":[int(age)],
            "TypeofContact":[typeofcontact],
            "CityTier":[int(citytier)],
            "DurationOfPitch":[int(durationofpitch)],
            "Occupation":[occupation],
            "Gender":[gender],
            "NumberOfPersonVisiting":[int(numberofpersonvisiting)],
            "NumberOfFollowups":[int(numberoffollowups)],
            "ProductPitched":[productpitched],
            "PreferredPropertyStar":[int(prefferedpropertystar)],
            "MaritalStatus":[maritalstatus],
            "NumberOfTrips":[int(numberoftrips)],
            "Passport":[int(passport)],
            "PitchSatisfactionScore":[int(pitchsatisfactionscore)],
            "OwnCar":[int(owncar)],
            "NumberOfChildrenVisiting":[int(numberofchildrenvisiting)],
            "Designation":[designation],
            "MonthlyIncome":[int(monthlyincome)]
        }

        with open(r"C:\Users\asdf\Documents\D.S\INEURON-PROJECTS\Tour_Package_Project\notebook\Processor.pkl","rb") as f:
            processor=dill.load(f)

        print(processor)

        df=pd.DataFrame(data_points)
        print(df)

        arr=processor.transform(df)

        # return render_template("home.html",arr=arr)
        return data_points

        

if __name__=="__main__":
    app.run(debug=True)