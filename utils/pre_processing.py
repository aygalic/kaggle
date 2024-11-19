import pandas as pd
from collections import Counter


class PreProcessing():

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
