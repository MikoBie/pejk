# %%
import pyreadstat
from pejk import RAW
from pejk.config import EMISSION, N_STUDENTS, N_WEEKENDERS, N_TEACHERS, N_NON_TEACHERS
from pejk.utils import compute_emission

# %%
## Prepare data
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

# %%
df.loc[:, "P23"] = (
    df.loc[:, "P23"].map(mappings.variable_value_labels["P23"]).map(EMISSION)
)
df["students"] = df.loc[:, "P1_1":"P1_4"].sum(axis=1)
n_students = df.query("students > 0").loc[:, "WAGA"].sum()
df["non_teachers"] = df.loc[:, "P1_7"]
n_non_teachers = df.query("non_teachers > 0").loc[:, "WAGA"].sum()
df["teachers"] = df.loc[:, "P1_6"]
n_teachers = df.query("teachers > 0").loc[:, "WAGA"].sum()

# %%
students_summer = df.query("students > 0").query("P25 == 1.0").reset_index(drop=True)

students_summer.loc[:, "emission"] = (
    students_summer.loc[:, "P1_1":"P1_4"]
    .max(axis=1)
    .multiply(students_summer.loc[:, "P23"], axis=0)
    .multiply(students_summer.loc[:, "P24"], axis=0)
)

# %%
students_academic = df.query("students > 0").query("P25 == 3.0").reset_index(drop=True)

students_academic.loc[:, "emission"] = (
    students_academic.loc[:, "P1_1":"P1_4"]
    .max(axis=1)
    .multiply(students_academic.loc[:, "P23"], axis=0)
    .multiply(students_academic.loc[:, "P24"], axis=0)
)

# %%
students_no_classes = (
    df.query("students > 0").query("P25 == 2.0").reset_index(drop=True)
)

students_no_classes.loc[:, "emission"] = (
    students_no_classes.loc[:, "P1_1":"P1_4"]
    .max(axis=1)
    .multiply(students_no_classes.loc[:, "P23"], axis=0)
    .multiply(students_no_classes.loc[:, "P24"], axis=0)
)

# %%
students_summer_emission = compute_emission(df=students_summer, N_GROUP=1, n_group=1)
students_academic_emission = compute_emission(
    df=students_academic, N_GROUP=1, n_group=1
)
students_no_classes_emission = compute_emission(
    df=students_no_classes, N_GROUP=1, n_group=1
)

internship_emission = (
    (
        students_summer_emission
        + students_academic_emission
        + students_no_classes_emission
    )
    * (N_STUDENTS - N_WEEKENDERS)
    / n_students
)
print("Students Erasmus Emission", internship_emission)


# %%
teachers_summer = df.query("teachers > 0").query("P25 == 1.0").reset_index(drop=True)

teachers_summer.loc[:, "emission"] = (
    teachers_summer.loc[:, "P1_6"]
    .multiply(teachers_summer.loc[:, "P23"], axis=0)
    .multiply(teachers_summer.loc[:, "P24"], axis=0)
)

# %%
teachers_academic = df.query("teachers > 0").query("P25 == 2.0").reset_index(drop=True)

teachers_academic.loc[:, "emission"] = (
    teachers_academic.loc[:, "P1_6"]
    .multiply(teachers_academic.loc[:, "P23"], axis=0)
    .multiply(teachers_academic.loc[:, "P24"], axis=0)
)
# %%

teachers_summer_emission = compute_emission(df=teachers_summer, N_GROUP=1, n_group=1)
teachers_academic_emission = compute_emission(
    df=teachers_academic, N_GROUP=1, n_group=1
)

teachers_internship_emission = (
    (teachers_summer_emission + teachers_academic_emission) * (N_TEACHERS) / n_teachers
)
print("Teachers Erasmus Emission", teachers_internship_emission)
# %%
non_teachers_summer = (
    df.query("non_teachers > 0").query("P25 == 1.0").reset_index(drop=True)
)

non_teachers_summer.loc[:, "emission"] = (
    non_teachers_summer.loc[:, "P1_7"]
    .multiply(non_teachers_summer.loc[:, "P23"], axis=0)
    .multiply(non_teachers_summer.loc[:, "P24"], axis=0)
)

# %%
non_teachers_academic = (
    df.query("non_teachers > 0").query("P25 == 2.0").reset_index(drop=True)
)

non_teachers_academic.loc[:, "emission"] = (
    non_teachers_academic.loc[:, "P1_7"]
    .multiply(non_teachers_academic.loc[:, "P23"], axis=0)
    .multiply(non_teachers_academic.loc[:, "P24"], axis=0)
)
# %%

non_teachers_summer_emission = compute_emission(
    df=non_teachers_summer, N_GROUP=1, n_group=1
)
non_teachers_academic_emission = compute_emission(
    df=non_teachers_academic, N_GROUP=1, n_group=1
)

non_teachers_internship_emission = (
    (non_teachers_summer_emission + non_teachers_academic_emission)
    * (N_NON_TEACHERS)
    / n_non_teachers
)
print("Non-teachers Erasmus Emission", non_teachers_internship_emission)
# %%
