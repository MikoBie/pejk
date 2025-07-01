# %%
import pyreadstat
from pejk import RAW
from pejk.config import N_TEACHERS, N_NON_TEACHERS
from pejk.utils import compute_emission

# %%
## Prepare data
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")
df.loc[:, "P4"] = df.loc[:, "P4"].apply(lambda x: x if x < 8 else 0)
df.loc[:, "P5"] = df.loc[:, "P5"].apply(lambda x: x if x < 8 else 0)

df["non_teachers"] = df.loc[:, "P1_7"]
n_non_teachers = df.query("non_teachers > 0").loc[:, "WAGA"].sum()
df["teachers"] = df.loc[:, "P1_6"]
n_teachers = df.query("teachers > 0").loc[:, "WAGA"].sum()

# %%
teachers = df.query("teachers > 0").reset_index(drop=True)

teachers.loc[:, "emission"] = teachers.loc[:, "P28"]
for _, mean in teachers.groupby("P29"):
    mean_name = mappings.variable_value_labels["P29"].get(_)
    distance = compute_emission(df=mean, N_GROUP=N_TEACHERS, n_group=n_teachers)
    print(f"The distance for {mean_name} is equal to {distance} km")

# %%
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)

non_teachers.loc[:, "emission"] = non_teachers.loc[:, "P28"]
for _, mean in non_teachers.groupby("P29"):
    mean_name = mappings.variable_value_labels["P29"].get(_)
    distance = compute_emission(df=mean, N_GROUP=N_NON_TEACHERS, n_group=n_non_teachers)
    print(f"The distance for {mean_name} is equal to {distance} km")

# %%
