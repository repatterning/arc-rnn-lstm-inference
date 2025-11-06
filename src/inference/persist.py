import logging

import src.elements.approximations as apr
import src.elements.specification as sc


class Persist:

    def __init__(self):
        pass

    @staticmethod
    def exc(specification: sc.Specification, approximations: apr.Approximations) -> int:
        """
        * Add an absolute percentage error field to the `approximations.estimates` frame<br>
        * Per `approximations` frame drop `date` & `ts_id`<br><br>

        :param specification: <br>
        :param approximations: <br>
        :return:
        """

        logging.info(approximations.forecasts)
        logging.info(approximations.estimates)

        return specification.ts_id
