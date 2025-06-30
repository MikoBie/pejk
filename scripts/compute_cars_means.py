# %%
import pyreadstat
from pejk import RAW, EXCEL

# %%
## Prepare data
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")
df.loc[:, "P4"] = df.loc[:, "P4"].apply(lambda x: x if x < 8 else 0)
df.loc[:, "P5"] = df.loc[:, "P5"].apply(lambda x: x if x < 8 else 0)

df["non_teachers"] = df.loc[:, "P1_7"]
n_non_teachers = df.query("non_teachers > 0").shape[0]
df["teachers"] = df.loc[:, "P1_6"]
n_teachers = df.query("teachers > 0").shape[0]

# %%
teachers = df.query("teachers > 0").reset_index(drop=True)

teachers_means = (
    teachers.groupby("P29")["P28"]
    .sum()
    .reset_index()
    .rename(columns={"P29": "group", "P28": "km"})
    .map(lambda x: mappings.variable_value_labels["P29"].get(x, x))
)

teachers_means.to_excel(EXCEL / "teachers-cars.xlsx")
# %%
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)

non_teachers_means = (
    non_teachers.groupby("P29")["P28"]
    .sum()
    .reset_index()
    .rename(columns={"P29": "group", "P28": "km"})
    .map(lambda x: mappings.variable_value_labels["P29"].get(x, x))
)

non_teachers_means.to_excel(EXCEL / "non-teachers-cars.xlsx")

# %%
