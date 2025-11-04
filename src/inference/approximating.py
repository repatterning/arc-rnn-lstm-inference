import logging
import os

import tensorflow as tf

import config
import src.elements.specification as sc


class Approximating:

    def __init__(self):

        self.__configurations = config.Config()

    def __get_model(self, path: str) -> tf.keras.models.Sequential:

        return tf.keras.models.load_model(
            filepath=os.path.join(path, 'model.keras'))

    def exc(self, specification: sc.Specification):

        path = os.path.join(self.__configurations.data_, str(specification.catchment_id), str(specification.ts_id))
        model = self.__get_model(path=path)
        logging.info(model)
