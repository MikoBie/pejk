# %%
import pyreadstat
from pejk import RAW
from pejk.config import EMISSION, N_STUDENTS, N_WEEKENDERS
from pejk.utils import compute_transport_days, compute_emission

# %%
## Prepare data
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

# %%
df.loc[:, "P15"] = (
    df.loc[:, "P15"].map(mappings.variable_value_labels["P15"]).map(EMISSION)
)
df["students"] = df.loc[:, "P1_1":"P1_4"].sum(axis=1)
n_students = df.query("students > 0").shape[0]

# %%
students_summer = df.query("students > 0").query("P17 == 1.0").reset_index(drop=True)
students_summer.loc[:, "P1_1":"P1_4"] = students_summer.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_1", t="P1_4", days="P14", times_semester=(1, 0)
    ),
    axis=1,
)

students_summer.loc[:, "emission"] = (
    students_summer.loc[:, "P1_1":"P1_4"]
    .max(axis=1)
    .multiply(students_summer.loc[:, "P15"], axis=0)
    .multiply(students_summer.loc[:, "P16"], axis=0)
)

# %%
students_academic = df.query("students > 0").query("P17 == 3.0").reset_index(drop=True)
students_academic.loc[:, "P1_1":"P1_4"] = students_academic.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_1", t="P1_4", days="P14", times_semester=(1, 0)
    ),
    axis=1,
)

students_academic.loc[:, "emission"] = (
    students_academic.loc[:, "P1_1":"P1_4"]
    .max(axis=1)
    .multiply(students_academic.loc[:, "P15"], axis=0)
    .multiply(students_academic.loc[:, "P16"], axis=0)
)

# %%
students_no_classes = (
    df.query("students > 0").query("P17 == 2.0").reset_index(drop=True)
)
students_no_classes.loc[:, "P1_1":"P1_4"] = students_no_classes.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_1", t="P1_4", days="P14", times_semester=(1, 0)
    ),
    axis=1,
)

students_no_classes.loc[:, "emission"] = (
    students_no_classes.loc[:, "P1_1":"P1_4"]
    .max(axis=1)
    .multiply(students_no_classes.loc[:, "P15"], axis=0)
    .multiply(students_no_classes.loc[:, "P16"], axis=0)
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
print("Students Intenship Emission", internship_emission)
