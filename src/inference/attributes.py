"""Module inference/attributes.py"""
import logging
import boto3
import json

import src.elements.attribute as atr
import src.elements.specification as sc
import src.s3.unload


class Attributes:
    """
    Attributes
    """

    def __init__(self, connector: boto3.session.Session):
        """

        :param connector: An instance of boto3.session.Session
        """

        # Instances for S3 interactions
        s3_client: boto3.session.Session.client = connector.client(
            service_name='s3')
        self.__unload = src.s3.unload.Unload(s3_client=s3_client)

    def __get_data(self, bucket_name: str, key_name: str) -> dict:
        """

        :param bucket_name:
        :param key_name:
        :return:
        """

        buffer = self.__unload.exc(bucket_name=bucket_name, key_name=key_name)

        return json.loads(buffer)

    def exc(self, specification: sc.Specification) -> atr.Attribute:
        """

        :param specification:
        :return:
        """

        string = specification.uri.replace('s3://', '')
        parts = string.split(sep='/', maxsplit=1)
        bucket_name = parts[0]
        prefix = parts[1]

        attribute = atr.Attribute(
            modelling=self.__get_data(bucket_name=bucket_name, key_name=f'{prefix}/modelling.json'),
            scaling=self.__get_data(bucket_name=bucket_name, key_name=f'{prefix}/scaling.json'))

        logging.info(attribute.modelling)
        logging.info(attribute.scaling)

        return attribute
