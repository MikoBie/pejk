# %%
import pyreadstat
from pejk import RAW
from pejk.config import EMISSION, N_STUDENTS, N_WEEKENDERS
from pejk.utils import compute_emission

# %%
## Prepare data
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

# %%
df.loc[:, "P18"] = (
    df.loc[:, "P18"].map(mappings.variable_value_labels["P18"]).map(EMISSION)
)
df["students"] = df.loc[:, "P1_1":"P1_4"].sum(axis=1)
n_students = df.query("students > 0").loc[:, "WAGA"].sum()

# %%
students_summer = df.query("students > 0").query("P20 == 1.0").reset_index(drop=True)

students_summer.loc[:, "emission"] = (
    students_summer.loc[:, "P1_1":"P1_4"]
    .max(axis=1)
    .multiply(students_summer.loc[:, "P18"], axis=0)
    .multiply(students_summer.loc[:, "P19"], axis=0)
)

n_students_summer = students_summer.loc[:, "WAGA"].sum()
# %%
students_academic = df.query("students > 0").query("P20 == 3.0").reset_index(drop=True)

students_academic.loc[:, "emission"] = (
    students_academic.loc[:, "P1_1":"P1_4"]
    .max(axis=1)
    .multiply(students_academic.loc[:, "P18"], axis=0)
    .multiply(students_academic.loc[:, "P19"], axis=0)
)

n_students_academic = students_academic.loc[:, "WAGA"].sum()
# %%
students_no_classes = (
    df.query("students > 0").query("P20 == 2.0").reset_index(drop=True)
)

students_no_classes.loc[:, "emission"] = (
    students_no_classes.loc[:, "P1_1":"P1_4"]
    .max(axis=1)
    .multiply(students_no_classes.loc[:, "P18"], axis=0)
    .multiply(students_no_classes.loc[:, "P19"], axis=0)
)
n_students_no_calsses = students_no_classes.loc[:, "WAGA"].sum()
# %%
students_summer_emission = compute_emission(
    df=students_summer, N_GROUP=(N_STUDENTS - N_WEEKENDERS), n_group=n_students
)
students_academic_emission = compute_emission(
    df=students_academic, N_GROUP=(N_STUDENTS - N_WEEKENDERS), n_group=n_students
)
students_no_classes_emission = compute_emission(
    df=students_no_classes, N_GROUP=(N_STUDENTS - N_WEEKENDERS), n_group=n_students
)

internship_emission = (
    students_summer_emission + students_academic_emission + students_no_classes_emission
)
print("Students Summer Camps", students_summer_emission)
print("Students Academic Camps", students_academic_emission)
print("Students No Calsses Camps", students_no_classes_emission)
print("Students Camps Emission", internship_emission)


# %%
