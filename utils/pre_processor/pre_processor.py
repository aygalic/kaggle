"""Base class for preprocessors"""
from abc import ABC, abstractmethod
import pandas as pd

class PreProcessorABC(ABC):
    """Defines PreProcessor API"""

    @abstractmethod
    def fit(self, data: pd.DataFrame) -> None:
        """Fit the preprocessor

        Parameters
        ----------
        data : pd.DataFrame
            Data to use for fit.
        """
        pass
    
    @abstractmethod
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Transform data

        Parameters
        ----------
        data : pd.DataFrame
            Data to transform

        Returns
        -------
        pd.DataFrame
            Processed data
        """
        pass

    def fit_transform(self, data:pd.DataFrame ) -> pd.DataFrame:
        """Fit the pre processor and transforms data

        Parameters
        ----------
        data : pd.DataFrame
            data to fit and transformed

        Returns
        -------
        pd.DataFrame
            transformed data.
        """
        self.fit(data)
        return self.transform(data)