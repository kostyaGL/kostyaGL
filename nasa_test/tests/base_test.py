import logging
import sys
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)


class BaseTest(object):
    """
        Base class to initialize the base test class and driver

    """

    @property
    def log(self):
        logger = logging.getLogger(self.__class__.__name__ + "." + sys._getframe(1).f_code.co_name)
        return logger

    @staticmethod
    def convert_sols_to_earth_date(sols):
        one_sol_day = 1.0275
        days = sols * one_sol_day
        d = datetime.today() - timedelta(days=days)
        return d
