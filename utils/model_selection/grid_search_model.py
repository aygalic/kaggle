from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

class GridSearchFactory:
    
    @staticmethod
    def RandomForestSearchFactory():
        parameter_grid = {'n_estimators':[10,50,100,200]}
        model = RandomForestClassifier()
        return GridSearchCV(model, parameter_grid)


    @staticmethod
    def XGBSearchFactory():
        parameter_grid = {'n_estimators':[10,50,100,200]}
        model = XGBClassifier()
        return GridSearchCV(model, parameter_grid)


