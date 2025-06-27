# %%
import pyreadstat
from pejk import RAW, EXCEL
from pejk.config import N_TEACHERS, N_STUDENTS, N_NON_TEACHERS
from pejk.utils import compute_transport_days

# %%
## Prepare data
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

df["students"] = df.loc[:, "P1_1":"P1_4"].sum(axis=1)
n_students = df.query("students > 0").shape[0]
df["non_teachers"] = df.loc[:, "P1_7"]
n_non_teachers = df.query("non_teachers > 0").shape[0]
df["teachers"] = df.loc[:, "P1_6"]
n_teachers = df.query("teachers > 0").shape[0]
# %%
students_summer = df.query("students > 0").reset_index(drop=True)


students_summer.loc[:, "students"] = (
    students_summer.loc[:, "students"]
    .divide(students_summer.loc[:, "students"])
    .multiply(students_summer.loc[:, "WAGA"])
)

students_summer.loc[:, "students"] = (
    students_summer.apply(
        lambda x: compute_transport_days(
            x=x, f="students", t="students", days="P4", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(students_summer.loc[:, "P6"], axis=0)
)

students_summer_means = (
    students_summer.groupby("P8")["students"]
    .sum()
    .reset_index()
    .rename(columns={"P8": "group", "students": "km"})
    .map(lambda x: mappings.variable_value_labels["P8"].get(x, x))
)

students_summer_means.loc[:, "km"] = students_summer_means.loc[:, "km"].apply(
    lambda x: round(x * N_STUDENTS / n_students, 2)
)

students_summer_means.to_excel(EXCEL / "students_summer_means_weighted.xlsx")
# %%
students_winter = df.query("students > 0").reset_index(drop=True)


students_winter.loc[:, "students"] = (
    students_winter.loc[:, "students"]
    .divide(students_winter.loc[:, "students"])
    .multiply(students_winter.loc[:, "WAGA"])
)

students_winter.loc[:, "students"] = (
    students_winter.apply(
        lambda x: compute_transport_days(
            x=x, f="students", t="students", days="P4", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(students_summer.loc[:, "P6"], axis=0)
)

students_winter_means = (
    students_winter.groupby("P8b")["students"]
    .sum()
    .reset_index()
    .rename(columns={"P8b": "group", "students": "km"})
    .map(lambda x: mappings.variable_value_labels["P8b"].get(x, x))
)

students_winter_means.loc[:, "km"] = students_winter_means.loc[:, "km"].apply(
    lambda x: round(x * N_STUDENTS / n_students, 2)
)

students_winter_means.to_excel(EXCEL / "students_winter_means_weighted.xlsx")
# %%

# %%
teachers_summer = df.query("teachers > 0").reset_index(drop=True)


teachers_summer.loc[:, "teachers"] = (
    teachers_summer.loc[:, "teachers"]
    .divide(teachers_summer.loc[:, "teachers"])
    .multiply(teachers_summer.loc[:, "WAGA"])
)

teachers_summer.loc[:, "teachers"] = (
    teachers_summer.apply(
        lambda x: compute_transport_days(
            x=x, f="teachers", t="teachers", days="P4", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(teachers_summer.loc[:, "P6"], axis=0)
)

teachers_summer_means = (
    teachers_summer.groupby("P8")["teachers"]
    .sum()
    .reset_index()
    .rename(columns={"P8": "group", "teachers": "km"})
    .map(lambda x: mappings.variable_value_labels["P8"].get(x, x))
)

teachers_summer_means.loc[:, "km"] = teachers_summer_means.loc[:, "km"].apply(
    lambda x: round(x * N_TEACHERS / n_teachers, 2)
)

teachers_summer_means.to_excel(EXCEL / "teachers_summer_means_weighted.xlsx")
# %%
teachers_winter = df.query("teachers > 0").reset_index(drop=True)


teachers_winter.loc[:, "teachers"] = (
    teachers_winter.loc[:, "teachers"]
    .divide(teachers_winter.loc[:, "teachers"])
    .multiply(teachers_winter.loc[:, "WAGA"])
)

teachers_winter.loc[:, "teachers"] = (
    teachers_winter.apply(
        lambda x: compute_transport_days(
            x=x, f="teachers", t="teachers", days="P4", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(teachers_summer.loc[:, "P6"], axis=0)
)

teachers_winter_means = (
    teachers_winter.groupby("P8b")["teachers"]
    .sum()
    .reset_index()
    .rename(columns={"P8b": "group", "teachers": "km"})
    .map(lambda x: mappings.variable_value_labels["P8b"].get(x, x))
)

teachers_winter_means.loc[:, "km"] = teachers_winter_means.loc[:, "km"].apply(
    lambda x: round(x * N_TEACHERS / n_teachers, 2)
)

teachers_winter_means.to_excel(EXCEL / "teachers_winter_means_weighted.xlsx")
# %%
non_teachers_summer = df.query("non_teachers > 0").reset_index(drop=True)


non_teachers_summer.loc[:, "non_teachers"] = (
    non_teachers_summer.loc[:, "non_teachers"]
    .divide(non_teachers_summer.loc[:, "non_teachers"])
    .multiply(non_teachers_summer.loc[:, "WAGA"])
)

non_teachers_summer.loc[:, "non_teachers"] = (
    non_teachers_summer.apply(
        lambda x: compute_transport_days(
            x=x, f="non_teachers", t="non_teachers", days="P4", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(non_teachers_summer.loc[:, "P6"], axis=0)
)

non_teachers_summer_means = (
    non_teachers_summer.groupby("P8")["non_teachers"]
    .sum()
    .reset_index()
    .rename(columns={"P8": "group", "non_teachers": "km"})
    .map(lambda x: mappings.variable_value_labels["P8"].get(x, x))
)

non_teachers_summer_means.loc[:, "km"] = non_teachers_summer_means.loc[:, "km"].apply(
    lambda x: round(x * N_NON_TEACHERS / n_non_teachers, 2)
)

non_teachers_summer_means.to_excel(EXCEL / "non_teachers_summer_means_weighted.xlsx")
# %%
non_teachers_winter = df.query("non_teachers > 0").reset_index(drop=True)


non_teachers_winter.loc[:, "non_teachers"] = (
    non_teachers_winter.loc[:, "non_teachers"]
    .divide(non_teachers_winter.loc[:, "non_teachers"])
    .multiply(non_teachers_winter.loc[:, "WAGA"])
)

non_teachers_winter.loc[:, "non_teachers"] = (
    non_teachers_winter.apply(
        lambda x: compute_transport_days(
            x=x, f="non_teachers", t="non_teachers", days="P4", times_semester=(4, 1)
        ),
        axis=1,
    )
    .multiply(1 / 4, axis=0)
    .multiply(non_teachers_summer.loc[:, "P6"], axis=0)
)

non_teachers_winter_means = (
    non_teachers_winter.groupby("P8b")["non_teachers"]
    .sum()
    .reset_index()
    .rename(columns={"P8b": "group", "non_teachers": "km"})
    .map(lambda x: mappings.variable_value_labels["P8b"].get(x, x))
)

non_teachers_winter_means.loc[:, "km"] = non_teachers_winter_means.loc[:, "km"].apply(
    lambda x: round(x * N_NON_TEACHERS / n_non_teachers, 2)
)

non_teachers_winter_means.to_excel(EXCEL / "non_teachers_winter_means_weighted.xlsx")
# %%
