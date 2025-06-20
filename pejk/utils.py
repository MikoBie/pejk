import pandas as pd
from textwrap import wrap
from pejk.config import JEDNOSTKI


def strip_string(x):
    """Returna strip string or the object.

    Parameters
    ----------
    x
        an python object

    Returns
    -------
        returns a stirpped string or a python object
    """
    return x.strip() if isinstance(x, str) else x


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


def prepare_data_columnswise(
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
        df = df.loc[:, f:t].multiply(df.loc[:, "WAGA"], axis=0)
    else:
        df = df.loc[:, f:t]

    df = (
        df.rename(columns=lambda x: rename_column(key=x, mapping=mapping))
        .sum()
        .reset_index()
        .rename(columns={"index": "group", 0: "count"})
        .sort_values("count")
    )
    df["group"] = df["group"].map(
        lambda x: JEDNOSTKI.get(strip_string(x), strip_string(x))
    )
    df["group"] = df["group"].apply(
        lambda x: "\n".join(wrap(x, 30)) if isinstance(x, str) else x
    )

    return df


def prepare_data_rowise(
    df: pd.DataFrame,
    key: str,
    mapping: dict,
    weight: bool = False,
) -> pd.DataFrame:
    """Prepares data frame to compute frequencies.

    Parameters
    ----------
    df
        data frame witht the results of PEJK study on emission and travels.

    key
        name of the column for which the frequencies will be calculated

    mapping
        dict that maps names of the variables to labels

    weight
        whether the data should be weighted, by default equals to False

    Returns
    -------
        frequencies for categories in given column
    """
    if weight:
        df = df.loc[:, [key, "WAGA"]].groupby(key).sum("WAGA")
    else:
        df = df.loc[:, key].value_counts()

    df = (
        df.reset_index()
        .rename(columns={key: "group", "WAGA": "count"})
        .sort_values("count")
    )
    df["group"] = df["group"].map(lambda x: mapping[key][x] if key in mapping else x)
    df["group"] = df["group"].map(
        lambda x: JEDNOSTKI.get(strip_string(x), strip_string(x))
    )
    df["group"] = df["group"].apply(lambda x: "\n".join(wrap(str(x), 30)))

    return df


def compute_transport_days(
    x: pd.Series, f: str, t: str, days: str, times_semester: tuple = (20, 5)
) -> pd.Series:
    """Compute the number of transport days based on the number of days a
    person was present at the university.

    Parameters
    ----------
    x :
        a row of the DataFrame containing the number of days present at the university
    f :
        the name of the column from where to select demographic data
    t :
        the name of the column to where to select demographic data

    days :
        the name of the column containing the number of days a person was present at the university weekly

    times_semester :
        a tuple containing the number of weeks in the semester or weekends with classes, respectively. Defaults to (20, 5).

    Returns
    -------
        a Series containing the number of transport days in the semester.
    """

    if x.loc[days] > 0:
        return x.loc[f:t].multiply(times_semester[0]).multiply(x.loc[days], axis=0)
    else:
        return (
            x.loc[f:t].multiply(times_semester[1]).multiply(x.loc[f"{days}b"], axis=0)
        )
