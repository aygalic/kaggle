"""module for outlier removal"""

from collections import Counter

import pandas as pd

from .pre_processor import PreProcessorABC


class OutlierRemover(PreProcessorABC):
    """Remove low occurring dummies within categorical columns"""

    def __init__(self):
        self.features_to_process = {}
        self.threshold = 10

    def fit(self, data: pd.DataFrame) -> None:
        for col in data:
            if data[col].dtype == "object":
                self.features_to_process[col] = [
                    var
                    for (var, count) in Counter(data[col].astype(str)).items()
                    if count > 10
                ]

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        for col in data:
            if data[col].dtype == "object":
                data[col] = [
                    var if var in self.features_to_process[col] else "Unknown"
                    for var in data[col]
                ]

        return data
