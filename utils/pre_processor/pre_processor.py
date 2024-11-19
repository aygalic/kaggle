
from abc import ABC, abstractmethod
import pandas as pd

class PreProcessorABC(ABC):

    @abstractmethod
    def fit(self, data: pd.DataFrame) -> None:
        pass
    
    @abstractmethod
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

    def fit_transform(self, data:pd.DataFrame ) -> pd.DataFrame:
        self.fit(data)
        return self.transform(data)