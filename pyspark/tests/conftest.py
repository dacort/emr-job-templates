import logging

import pytest
from jobs.extreme_weather import ExtremeWeather
from pyspark.sql import SparkSession


def quiet_py4j():
    """turn down spark logging for the test context"""
    logger = logging.getLogger("py4j")
    logger.setLevel(logging.WARN)


# @pytest.fixture(scope="session")
# def spark():
#     sc = SparkSession.builder.master("local[*]").appName("weather-tests").getOrCreate()
#     # quiet_py4j()
#     return sc

@pytest.fixture(scope="session")
def mock_df():
        ExtremeWeather._gsod_year_uri = lambda self, year: "./tests/data/"
        return ExtremeWeather(2021)._fetch_data()