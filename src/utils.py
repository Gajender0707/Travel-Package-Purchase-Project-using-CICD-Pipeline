import pandas as pd
import numpy as np

class Dataframe:
    def __init__(self):
        pass
    
    def get_dataframe(self,age,typeofcontact,citytier,durationofpitch,occupation,gender,
                      numberofpersonvisiting,numberoffollowups,productpitched,prefferedpropertystar,
                      maritalstatus,numberoftrips,passport, pitchsatisfactionscore,owncar,
                      numberofchildrenvisiting,designation,monthlyincome):
        self.age=age
        self.typeofcontact=typeofcontact
        self.citytier=citytier
        self.durationofpitch=durationofpitch
        self.occupation=occupation
        self.gender=gender
        self.numberofpersonvisiting=numberofpersonvisiting
        self.numberoffollowups=numberoffollowups
        self.productpitched=productpitched
        self.prefferedpropertystar=prefferedpropertystar
        self.maritalstatus=maritalstatus
        self.numberoftrips=numberoftrips
        self.passport=passport
        self.pitchsatisfactionscore=pitchsatisfactionscore
        self.owncar=owncar
        self.numberofchildrenvisiting=numberofchildrenvisiting
        self.designation=designation
        self.monthlyincome=monthlyincome



