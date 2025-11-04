"""Module inference/interface.py"""
import logging

import boto3
import dask
import pandas as pd

import src.elements.attribute as atr
import src.elements.specification as sc
import src.inference.attributes
import src.inference.data


class Interface:
    """
    Interface
    """

    def __init__(self, connector: boto3.session.Session, arguments: dict, limits: list):
        """

        :param connector:
        :param arguments:
        :param limits:
        """

        self.__connector = connector
        self.__arguments = arguments
        self.__limits = limits

        # Setting up
        self.__endpoint: str = self.__arguments.get('additions').get('modelling_data_source')

    @dask.delayed
    def __get_listing(self, specification: sc.Specification) -> list[str]:
        """

        :param specification:
        :return:
        """

        listing = [f'{self.__endpoint}/{specification.catchment_id}/{specification.ts_id}/{limit}.csv'
                   for limit in self.__limits ]

        return listing

    def exc(self, specifications: list[sc.Specification]):
        """

        :param specifications:
        :return:
        """

        __get_attributes = dask.delayed(src.inference.attributes.Attributes(connector=self.__connector).exc)
        __get_data = dask.delayed(src.inference.data.Data().exc)

        computations = []
        for specification in specifications:
            attribute: atr.Attribute = __get_attributes(specification=specification)
            listing: list[str] = self.__get_listing(specification=specification)
            data: pd.DataFrame = __get_data(listing=listing, modelling=attribute.modelling)
            computations.append(data.shape[0])

        calculations = dask.compute(computations, scheduler='threads')[0]
        logging.info(calculations)
