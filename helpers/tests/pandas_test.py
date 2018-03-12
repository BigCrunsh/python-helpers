# testing
from unittest import TestCase
from pandas.testing import assert_series_equal, assert_frame_equal

# data
import pandas as pd

# helpers
from helpers.pandas import explode_series, explode_dataframe, unpivot


class TestPandas(TestCase):

    def test_explode_series(self):
        series = pd.Series({1: [1, 3, 2, 3], 2: [5]})
        got = explode_series(series)
        expected = pd.Series({0: 1, 1: 3, 2: 2, 3: 3, 4: 5})
        assert_series_equal(expected, got)

        series = pd.Series({1: []})
        got = explode_series(series)
        expected = pd.Series([])
        assert_series_equal(expected, got)

        series = pd.Series()
        got = explode_series(series)
        expected = pd.Series([])
        assert_series_equal(expected, got)

    def test_explode_dataframe(self):
        col = 1
        df = pd.DataFrame({
            col: {0: [1, 3, 2, 3]},
            'org': {0: 5}
        })
        got = explode_dataframe(df, col)
        expected = pd.DataFrame({
            col: {0: 1, 1: 3, 2: 2, 3: 3},
            'org': {0: 5, 1: 5, 2: 5, 3: 5}
        })
        assert_frame_equal(expected, got)

    def test_unpivot(self):
        df = pd.DataFrame({
            'us': {0: 0.1, 1: 0.2},
            'de': {0: 1.0, 1: 2.0},
            'id': {0: 100, 1: 200}
        })
        got = unpivot(df, 'country_code', 'values', ['us', 'de'])
        expected = pd.DataFrame({
            'country_code': {0: 'us', 1: 'us', 2: 'de', 3: 'de'},
            'id': {0: 100, 1: 200, 2: 100, 3: 200},
            'values': {0: 0.1, 1: 0.2, 2: 1.0, 3: 2.0}
        })
        assert_frame_equal(got, expected, check_like=True)

        # check consistency with pivot
        df2 = expected.pivot(index='id', columns='country_code', values='values').reset_index()
        df2.columns.name = ''
        assert_frame_equal(df, df2, check_like=True)
