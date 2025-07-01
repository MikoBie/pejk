# %%
import pyreadstat
from pejk import RAW
from pejk.config import EMISSION, N_TEACHERS, N_NON_TEACHERS
from pejk.utils import compute_emission

# %%
## Prepare data
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")
df.loc[:, "P4"] = df.loc[:, "P4"].apply(lambda x: x if x < 8 else 0)
df.loc[:, "P5"] = df.loc[:, "P5"].apply(lambda x: x if x < 8 else 0)

# %%
df.loc[:, "P29"] = (
    df.loc[:, "P29"].map(mappings.variable_value_labels["P29"]).map(EMISSION)
)
df["non_teachers"] = df.loc[:, "P1_7"]
n_non_teachers = df.query("non_teachers > 0").loc[:, "WAGA"].sum()
df["teachers"] = df.loc[:, "P1_6"]
n_teachers = df.query("teachers > 0").loc[:, "WAGA"].sum()
# %%
teachers = df.query("teachers > 0").reset_index(drop=True)

teachers["emission"] = (
    teachers.loc[:, "WAGA"]
    .multiply(teachers.loc[:, "P28"], axis=0)
    .multiply(teachers.loc[:, "P29"], axis=0)
)

# %%
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)

non_teachers["emission"] = (
    non_teachers.loc[:, "WAGA"]
    .multiply(non_teachers.loc[:, "P28"], axis=0)
    .multiply(non_teachers.loc[:, "P29"], axis=0)
)
# %%
teachers_emission = compute_emission(
    df=teachers, N_GROUP=N_TEACHERS, n_group=n_teachers
)
print("Teachers emission:", teachers_emission)
# %%
non_teachers_emission = compute_emission(
    df=non_teachers, N_GROUP=N_NON_TEACHERS, n_group=n_non_teachers
)
print("Non-teachers emission:", non_teachers_emission)
