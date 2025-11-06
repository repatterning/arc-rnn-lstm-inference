import logging

import pandas as pd

import src.elements.specification as sc


class Persist:

    def __init__(self):
        pass

    @staticmethod
    def exc(specification: sc.Specification, approximations: pd.DataFrame) -> int:

        logging.info(approximations.tail())

        return specification.ts_id
