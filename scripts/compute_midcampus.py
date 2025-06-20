# %%
import pyreadstat
from pejk import RAW
from pejk.config import EMISSION, N_TEACHERS, N_STUDENTS, N_NON_TEACHERS
from pejk.utils import compute_transport_days, compute_emission

# %%
## Prepare data
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")

df.loc[:, "P10"] = (
    df.loc[:, "P10"].map(mappings.variable_value_labels["P10"]).map(EMISSION)
)

df["students"] = df.loc[:, "P1_1":"P1_5"].sum(axis=1)
n_students = df.query("students > 0").shape[0]
df["non_teachers"] = df.loc[:, "P1_7"]
n_non_teachers = df.query("non_teachers > 0").shape[0]
df["teachers"] = df.loc[:, "P1_6"]
n_teachers = df.query("teachers > 0").shape[0]
# %%
students = df.query("students > 0").reset_index(drop=True)
students.loc[:, "P1_1":"P1_4"] = students.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_1", t="P1_4", days="P9", times_semester=(40, 0)
    ),
    axis=1,
)

students["emission"] = (
    students.loc[:, "P1_1":"P1_4"]
    .max(axis=1)
    .multiply(students.loc[:, "P10"], axis=0)
    .multiply(students.loc[:, "P11"], axis=0)
)

# %%
teachers = df.query("teachers > 0").reset_index(drop=True)
teachers.loc[:, "P1_6"] = teachers.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_6", t="P1_6", days="P9", times_semester=(45, 0)
    ),
    axis=1,
)

teachers["emission"] = (
    teachers.loc[:, "P1_6"]
    .multiply(teachers.loc[:, "P10"], axis=0)
    .multiply(teachers.loc[:, "P11"], axis=0)
)

# %%
non_teachers = df.query("non_teachers > 0").reset_index(drop=True)
non_teachers.loc[:, "P1_7"] = non_teachers.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_7", t="P1_7", days="P9", times_semester=(48, 0)
    ),
    axis=1,
)

non_teachers["emission"] = (
    non_teachers.loc[:, "P1_7"]
    .multiply(non_teachers.loc[:, "P10"], axis=0)
    .multiply(non_teachers.loc[:, "P11"], axis=0)
)

# %%
students_emission = compute_emission(
    df=students, N_GROUP=N_STUDENTS, n_group=n_students
)
print("Students emission:", students_emission)

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

# %%
