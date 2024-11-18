import pandas as pd
from collections import Counter


class PreProcessing():
    def __init__(self, X_train):
        self.X_train = X_train
        self.valid_cities = [city for (city,count) in Counter(X_train["City"]).items() if count > 10]
        self.valid_degrees = [degree for (degree,count) in Counter(X_train["Degree"].astype(str)).items() if count > 10]
        self.valid_profession = [profession for (profession,count) in Counter(X_train["Profession"].astype(str)).items() if count > 10]
        self.valid_sleep_times = [sleep_times for (sleep_times,count) in Counter(X_train["Sleep Duration"].astype(str)).items() if count > 10]
        self.valid_dietary_habits = [habits for (habits,count) in Counter(X_train["Dietary Habits"].astype(str)).items() if count > 10]



    # this actually decrease the performance widely
    @staticmethod
    def concat_features(data:pd.DataFrame) -> pd.DataFrame:
        pres = [[work_pres, academic_pres][is_student]  for (academic_pres, work_pres, is_student) in zip(data["Academic Pressure"], data["Work Pressure"], data["Working Professional or Student"]=="Student")]
        data["Work/Study Presure"] = pres
        data = data.drop(["Academic Pressure", "Work Pressure"], axis=1)
        
        sat = [[work_sat, academic_sat][is_student]  for (work_sat, academic_sat, is_student) in zip(data["Study Satisfaction"], data["Job Satisfaction"], data["Working Professional or Student"]=="Student")]
        data["Work/Study Satisfaction"] = sat
        data = data.drop(["Study Satisfaction", "Job Satisfaction"], axis=1)
        return data


    
    def fix_outliers(self, data: pd.DataFrame) -> pd.DataFrame:
        data["City"] = [var if var in self.valid_cities else "Unknown" for var in data["City"]]
        data["Degree"] = [var if var in self.valid_degrees else "Unknown" for var in data["Degree"]]
        data["Profession"] = [var if var in self.valid_profession else "Unknown" for var in data["Profession"]]
        data["Sleep Duration"] = [var if var in self.valid_sleep_times else "Unknown" for var in data["Sleep Duration"]]
        data["Dietary Habits"] = [var if var in self.valid_sleep_times else "Unknown" for var in data["Dietary Habits"]]
        return data