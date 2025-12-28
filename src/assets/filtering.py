"""Module filtering.py"""
import numpy as np
import pandas as pd


class Filtering:
    """
    Filtering
    """

    def __init__(self, cases: pd.DataFrame, foci: pd.DataFrame, arguments: dict):
        """

        :param cases: The gauge stations that have model artefacts
        :param foci: The gauge stations within a current warning area
        :param arguments:
        """

        self.__cases = cases
        self.__foci = foci
        self.__arguments = arguments

    def __inspect(self):
        """
        Beware, the number of cases herein will be due to the model artefacts that exist within the
        `inspect`, i.e., pre-live, storage area.

        :return:
        """

        return self.__cases

    def __live(self):
        """
        The number of cases herein will be due to the model artefacts that exist within the `live` storage area.

        :return:
        """

        return self.__cases

    def __service(self):

        excerpt = self.__arguments.get('series').get('excerpt')
        if excerpt is None:
            return pd.DataFrame()

        codes = np.unique(np.array(excerpt))
        cases = self.__cases.copy().loc[self.__cases['ts_id'].isin(codes), :]
        cases = cases if cases.shape[0] > 0 else pd.DataFrame()

        return cases

    def __warning(self) -> pd.DataFrame:
        """

        :return:
        """

        if self.__foci.empty:
            return pd.DataFrame()

        codes: np.ndarray = self.__foci['ts_id'].values
        cases = self.__cases.copy().loc[self.__cases['ts_id'].isin(codes), :]
        cases = cases if cases.shape[0] > 0 else self.__cases

        return cases

    def exc(self):
        """

        :return:
        """


