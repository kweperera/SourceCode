import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier


class Predict:

    def data_loading(self):
        gender_lb = pickle.load(open('gender_encoder.sav', 'rb'))
        vehicle_age_lb = pickle.load(open('vehicle_age.sav', 'rb'))
        vehicle_damage_lb = pickle.load(open('vehicle_damage.sav', 'rb'))
        model = pickle.load(open('finalized_model.sav', 'rb'))

        return gender_lb, vehicle_age_lb, vehicle_damage_lb, model

    def data_prediction(self, Gender, Age, Driving_License, Region_Code, Previously_Insured, Vehicle_Age,
                        Vehicle_Damage, Annual_Premium,
                        Policy_Sales_Channel, Vintage):
        gender_lb, vehicle_age_lb, vehicle_damage_lb, model = self.data_loading()
        df = pd.DataFrame(data={'Gender': [Gender], 'Vehicle_Age': [Vehicle_Age], 'Vehicle_Damage': [Vehicle_Damage]})
        df['Gender'] = self.gender_lb.transform(df['Gender'])
        df['Vehicle_Age'] = self.vehicle_age_lb.transform(df['Vehicle_Age'])
        df['Vehicle_Damage'] = self.vehicle_damage_lb.transform(df['Vehicle_Damage'])

        prediction_value = (model.predict(np.array(
            [[df['Gender'].iloc[0], Age, Driving_License, Region_Code, Previously_Insured, df['Vehicle_Age'].iloc[0],
              df['Vehicle_Damage'].iloc[0], Annual_Premium, Policy_Sales_Channel, Vintage]]))[0])
        return prediction_value
