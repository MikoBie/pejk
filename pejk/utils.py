import pandas as pd
from textwrap import wrap
from pejk.config import JEDNOSTKI


def rename_column(key: str, mapping: dict) -> str:
    """Maps the name of the column to the string behind "-" of the label.

    Parameters
    ----------
    key
        name of the column
    mapping, optional
        a dictionary that maps names of the columns to labels, by default _.column_names_to_labels

    Returns
    -------
        a string behind "-" of the label.
    """
    return mapping[key].split(" - ")[-1]


def prepare_data_barplots(
    df: pd.DataFrame, f: str, t: str, mapping: dict, weight: bool = False
) -> pd.DataFrame:
    """Prepares data frame to compute frequencies.

    Parameters
    ----------
    df
        data frame witht the results of PEJK study on emission and travels.

    f
        the name of the column to select from

    t the name of the column to select until

    mapping
        dict that maps names of the columns to labels

    weight
        whether the data should be weighted, by default equals to False

    Returns
    -------
        sum of the given columns
    """
    if weight:
        df = df.loc[:, f:t].mulitply(df.loc[:, "WAGA"], axis=0)
    df = df.loc[:, f:t]

    df = (
        df.rename(columns=lambda x: rename_column(key=x, mapping=mapping))
        .sum()
        .reset_index()
        .rename(columns={"index": "group", 0: "count"})
        .sort_values("count")
    )
    df["group"] = df["group"].map(lambda x: JEDNOSTKI.get(x.strip(), x.strip()))
    df["group"] = df["group"].apply(lambda x: "\n".join(wrap(x, 30)))

    return df
