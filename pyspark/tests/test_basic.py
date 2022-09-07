import pytest
from jobs.extreme_weather import ExtremeWeather
from pyspark.sql import SparkSession

# pytestmark = pytest.mark.usefixtures("spark")
TEST_YEAR = 2021

def test_s3_uri():
    wd = ExtremeWeather(TEST_YEAR)
    assert wd._gsod_year_uri(TEST_YEAR) == "s3://noaa-gsod-pds/2021/"


def test_data_load():
    ExtremeWeather._gsod_year_uri = lambda self, year: "./tests/data/"
    wd = ExtremeWeather(TEST_YEAR)
    assert wd._gsod_year_uri(TEST_YEAR) == "./tests/data/"

    # In this test, we load data for a single year from a single weather station.
    # As such, we expect only 356 records.
    df = wd._fetch_data()
    assert df.count() == 365

def test_find_largest_temp(mock_df):
    wd = ExtremeWeather(TEST_YEAR)
    max_temp = wd.findLargest(mock_df, "MAX")
    print(max_temp)
    assert max_temp.DATE == '2021-06-29'
    assert max_temp.MAX == 108.0
