import logging

import src.elements.approximations as apr
import src.elements.specification as sc


class Persist:

    def __init__(self):
        pass

    @staticmethod
    def exc(specification: sc.Specification, approximations: apr.Approximations) -> int:

        logging.info(approximations.forecasts)
        logging.info(approximations.estimates)

        return specification.ts_id
