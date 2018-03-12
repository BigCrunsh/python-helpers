from __future__ import absolute_import  # to get builtin lib and not local
import pandas as pd
import numpy as np


def explode_series(series):
    """
    Explode a series of iterables.

    Args:
        series (pd.Series): Series that contains iterables

    Returns:
        pd.Series: contains a new row for each element in the given iterable.
    """
    return pd.Series(sum(series.tolist(), []))


def explode_dataframe(df, col):
    """
    Explode a dataframe on a given column of iterables.

    Args:
        df (pd.DataFrame): DataFrame that contains a column of iterables
        col (string): column name in `df` that gets exploded.

    Returns:
        pd.DataFrame: contains a new row for each element in the given column.
    """
    return pd.DataFrame({
        c:
            explode_series(df[c]) if c == col else
            explode_series(pd.Series({
                idx: [row[c]] * len(row[col])
                for idx, row in df.T.iteritems()
            }))
        for c in df
    })


def unpivot(df, type_name, type_value_name, type_values):
    """
    Inverse operation of pivot.

    Reshape data (produce an "unpivot" table) by creating a new column for the
    type names (former column names) and one for the type values (values of the
    former columns).

    Args:
        type_name (string): Name of a new column that contains value types (former column names)
        type_value_name (string): Name of a new column that contains the values of the corresponding
        value types.
        type_values (list): List of column names that are merged into one column.

    Returns:
        pd.DataFrame: unpivoted table.

    """
    num_rows = df.shape[0]
    kept_cols = set(df.columns.tolist()) - set(type_values)
    return pd.DataFrame(dict({
        type_value_name: df[type_values].values.ravel('F'),
        type_name: np.asarray(type_values).repeat(num_rows)
    }, **{
        col: np.tile(np.asarray(df[col]), len(type_values))
        for col in kept_cols
    }))
