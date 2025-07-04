# %%
import pyreadstat
from pejk import RAW, EXCEL
from pejk.utils import compute_transport_days
from pejk.config import N_STUDENTS, N_TEACHERS, N_NON_TEACHERS

# %%
## Prepare data
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")
## Values above 7 mean someone did not go to the Uni in a given
## semester
df.loc[:, "P4"] = df.loc[:, "P4"].apply(lambda x: x if x < 8 else 0)
df.loc[:, "P5"] = df.loc[:, "P5"].apply(lambda x: x if x < 8 else 0)

df["students"] = df.loc[:, "P1_1":"P1_4"].sum(axis=1)
n_students = df.query("students > 0").loc[:, "WAGA"].sum()
df["non_teachers"] = df.loc[:, "P1_7"]
n_non_teachers = df.query("non_teachers > 0").loc[:, "WAGA"].sum()
df["teachers"] = df.loc[:, "P1_6"]
n_teachers = df.query("teachers > 0").loc[:, "WAGA"].sum()
# %%
students_summer = df.query("students > 0").reset_index(drop=True)


students_summer.loc[:, "emission"] = (
    students_summer.apply(
        lambda x: compute_transport_days(
            x=x, f="WAGA", t="WAGA", days="P4", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(students_summer.loc[:, "P6"], axis=0)
)

students_summer_means = (
    students_summer.groupby("P8")["emission"]
    .sum()
    .reset_index()
    .rename(columns={"P8": "group", "emission": "km"})
    .assign(km=lambda x: round(x["km"] * N_STUDENTS / n_students, 2))
    .replace({"group": mappings.variable_value_labels["P8"]})
)

students_summer_means.to_excel(EXCEL / "students_summer_means.xlsx")
# %%
students_winter = df.query("students > 0").reset_index(drop=True)

students_winter.loc[:, "WAGA"] = (
    students_winter.apply(
        lambda x: compute_transport_days(
            x=x, f="WAGA", t="WAGA", days="P5", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(students_winter.loc[:, "P6"], axis=0)
)

students_winter_means = (
    students_winter.groupby("P8b")["WAGA"]
    .sum()
    .reset_index()
    .rename(columns={"P8b": "group", "WAGA": "km"})
    .assign(km=lambda x: round(x["km"] * N_STUDENTS / n_students, 2))
    .replace({"group": mappings.variable_value_labels["P8b"]})
)

students_winter_means.to_excel(EXCEL / "students_winter_means.xlsx")
# %%
teachers_summer = df.query("teachers > 0").reset_index(drop=True)

teachers_summer.loc[:, "WAGA"] = (
    teachers_summer.apply(
        lambda x: compute_transport_days(
            x=x, f="WAGA", t="WAGA", days="P4", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(teachers_summer.loc[:, "P6"], axis=0)
)

teachers_summer_means = (
    teachers_summer.groupby("P8")["WAGA"]
    .sum()
    .reset_index()
    .rename(columns={"P8": "group", "WAGA": "km"})
    .assign(km=lambda x: round(x["km"] * N_TEACHERS / n_teachers, 2))
    .replace({"group": mappings.variable_value_labels["P8"]})
)

teachers_summer_means.to_excel(EXCEL / "teachers_summer_means.xlsx")
# %%
teachers_winter = df.query("teachers > 0").reset_index(drop=True)


teachers_winter.loc[:, "WAGA"] = (
    teachers_winter.apply(
        lambda x: compute_transport_days(
            x=x, f="WAGA", t="WAGA", days="P5", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(teachers_winter.loc[:, "P6"], axis=0)
)

teachers_winter_means = (
    teachers_winter.groupby("P8b")["WAGA"]
    .sum()
    .reset_index()
    .rename(columns={"P8b": "group", "WAGA": "km"})
    .assign(km=lambda x: round(x["km"] * N_TEACHERS / n_teachers, 2))
    .replace({"group": mappings.variable_value_labels["P8b"]})
)

teachers_winter_means.to_excel(EXCEL / "teachers_winter_means.xlsx")
# %%
non_teachers_summer = df.query("non_teachers > 0").reset_index(drop=True)


non_teachers_summer.loc[:, "WAGA"] = (
    non_teachers_summer.apply(
        lambda x: compute_transport_days(
            x=x, f="WAGA", t="WAGA", days="P4", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(non_teachers_summer.loc[:, "P6"], axis=0)
)

non_teachers_summer_means = (
    non_teachers_summer.groupby("P8")["WAGA"]
    .sum()
    .reset_index()
    .rename(columns={"P8": "group", "WAGA": "km"})
    .assign(km=lambda x: round(x["km"] * N_NON_TEACHERS / n_non_teachers, 2))
    .replace({"group": mappings.variable_value_labels["P8"]})
)

non_teachers_summer_means.to_excel(EXCEL / "non_teachers_summer_means.xlsx")
# %%
non_teachers_winter = df.query("non_teachers > 0").reset_index(drop=True)


non_teachers_winter.loc[:, "WAGA"] = (
    non_teachers_winter.apply(
        lambda x: compute_transport_days(
            x=x, f="WAGA", t="WAGA", days="P5", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(non_teachers_winter.loc[:, "P6"], axis=0)
)

non_teachers_winter_means = (
    non_teachers_winter.groupby("P8b")["WAGA"]
    .sum()
    .reset_index()
    .rename(columns={"P8b": "group", "WAGA": "km"})
    .assign(km=lambda x: round(x["km"] * N_NON_TEACHERS / n_non_teachers, 2))
    .replace({"group": mappings.variable_value_labels["P8b"]})
)

non_teachers_winter_means.to_excel(EXCEL / "non_teachers_winter_means.xlsx")
