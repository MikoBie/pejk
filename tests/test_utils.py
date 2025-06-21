import pytest
from pejk.utils import (
    strip_string,
    rename_column,
    prepare_data_columnswise,
    prepare_data_rowise,
    compute_transport_days,
    compute_emission,
    division_zero,
)
import pandas as pd


def test_strip_string():
    assert strip_string("  test  ") == "test"
    assert strip_string(123) == 123
    assert strip_string(None) is None
    assert strip_string(["test", "strip"]) == ["test", "strip"]


@pytest.mark.parametrize(
    "key,expected",
    [
        ("col1", "Description"),
        ("col2", "Another Description"),
        ("col3", "Yet Another Description"),
        ("col4", "Unknown Column"),
    ],
)
def test_rename_column(key, expected):
    mapping = {
        "col1": "Label 1 - Description",
        "col2": "Label 2 - Another Description",
        "col3": "Label 3 - Yet Another Description",
        "col4": "Unknown Column",
    }
    assert rename_column(key, mapping) == expected
    assert isinstance(rename_column(key, mapping), str)


def test_prepare_data_columnswise():
    data = {"col1": [1, 2, 3], "col2": [1, 2, 3], "col3": [1, 2, 3], "col4": [4, 5, 6]}
    df = pd.DataFrame(data)
    mapping = {
        "col1": "Label 1 - Description",
        "col2": "Label 2 - Another Description",
        "col3": "Label 3 - Yet Another Description",
        "col4": "Unknown Column",
    }

    result = prepare_data_columnswise(df=df, f="col1", t="col3", mapping=mapping)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 3
    assert result.shape[1] == 2
    assert set(result.columns) == {"count", "group"}
    assert result["group"].tolist() == [
        "Description",
        "Another Description",
        "Yet Another Description",
    ]
    assert result["count"].tolist() == [6, 6, 6]


def test_prepare_data_columnswise_weighted():
    data = {
        "col1": [1, 2, 3],
        "col2": [1, 2, 3],
        "col3": [1, 2, 3],
        "WAGA": [0.1, 0.2, 0.3],
    }
    df = pd.DataFrame(data)
    mapping = {
        "col1": "Label 1 - Description",
        "col2": "Label 2 - Another Description",
        "col3": "Label 3 - Yet Another Description",
        "col4": "Unknown Column",
    }

    result = prepare_data_columnswise(
        df=df, f="col1", t="col3", mapping=mapping, weight=True
    )

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 3
    assert result.shape[1] == 2
    assert set(result.columns) == {"count", "group"}
    assert result["group"].tolist() == [
        "Description",
        "Another Description",
        "Yet Another Description",
    ]
    assert result["count"].tolist() == [1.4, 1.4, 1.4]


@pytest.mark.parametrize(
    "data,mapping",
    [
        (
            {"P1": [1, 2, 3, 3], "P2": [4, 5, 6, 6], "P3": [7, 8, 9, 2]},
            {
                "P1": {
                    1: "Description",
                    2: "Another Description",
                    3: "Yet Another Description",
                }
            },
        ),
        ({"P1": [1, 2, 3, 3], "P2": [4, 5, 6, 6], "P3": [7, 8, 9, 2]}, {}),
    ],
)
def test_prepare_data_rowise(data, mapping):
    df = pd.DataFrame(data)

    result = prepare_data_rowise(df=df, key="P1", mapping=mapping)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == df.loc[:, "P1"].unique().size
    assert result.shape[1] == 2
    assert set(result.columns) == {"count", "group"}
    assert (
        result["group"].tolist() == list(mapping.get("P1", {}).values())
        if mapping
        else df["P1"].unique().tolist()
    )
    assert result["count"].tolist() == [1, 1, 2]


def test_prepare_data_rowise_weighted():
    data = {
        "P1": [1, 2, 3, 3],
        "P2": [4, 5, 6, 6],
        "P3": [7, 8, 9, 2],
        "WAGA": [0.1, 0.2, 0.3, 0.4],
    }
    df = pd.DataFrame(data)
    mapping = {
        "P1": {1: "Description", 2: "Another Description", 3: "Yet Another Description"}
    }

    result = prepare_data_rowise(df=df, key="P1", mapping=mapping, weight=True)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == df.loc[:, "P1"].unique().size
    assert result.shape[1] == 2
    assert set(result.columns) == {"count", "group"}
    assert result["group"].tolist() == list(mapping.get("P1", {}).values())
    assert result["count"].tolist() == [0.1, 0.2, 0.3 + 0.4]


@pytest.mark.parametrize(
    "x",
    [
        pd.Series({"col1": 1, "col2": 0, "col3": 3, "col3b": 4}),
        pd.Series({"col1": 1, "col2": 0, "col3": 0, "col3b": 4}),
        pd.Series({"col1": 1, "col2": 0, "col3": 0}),
    ],
)
def test_compute_transport_days(x):
    result = compute_transport_days(
        x, f="col1", t="col2", days="col3", times_semester=(20, 5)
    )
    assert isinstance(result, pd.Series)
    assert len(result) == 2
    if x["col3"] > 0:
        assert result["col1"] == 60
        assert result["col2"] == 0
    else:
        if "col3b" in x:
            assert result["col1"] == 20
        else:
            assert result["col1"] == 0
        assert result["col2"] == 0
    result = compute_transport_days(
        x, f="col1", t="col1", days="col3", times_semester=(20, 5)
    )
    assert isinstance(result, pd.Series)
    assert len(result) == 1


def test_compute_emission():
    data = {"emission": [7, 8, 9], "WAGA": [0.1, 0.2, 0.3]}
    df = pd.DataFrame(data)
    n_group = 2
    N_GROUP = 4

    result = compute_emission(df, n_group=n_group, N_GROUP=N_GROUP)

    assert isinstance(result, float)
    assert result == (7 * 0.1 + 8 * 0.2 + 9 * 0.3) * (4 / 2)


def test_division_zero():
    assert division_zero(10, 2) == 5
    assert division_zero(10, 0) == 0
    assert division_zero(0, 10) == 0
    assert division_zero(0, 0) == 0
