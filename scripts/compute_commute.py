# %%
import pyreadstat
from pejk import RAW
from pejk.config import EMISSION, N_TEACHERS, N_STUDENTS, N_NON_TEACHERS
from pejk.utils import compute_transport_days, compute_emission, weight_absence

# %%
## Prepare data
df, mappings = pyreadstat.read_sav(RAW / "raw_data.sav")
df.loc[:, "P4"] = df.loc[:, "P4"].apply(lambda x: x if x < 8 else 0)
df.loc[:, "P5"] = df.loc[:, "P5"].apply(lambda x: x if x < 8 else 0)

df.loc[:, "P8"] = (
    df.loc[:, "P8"].map(mappings.variable_value_labels["P8"]).map(EMISSION)
)
df.loc[:, "P8b"] = (
    df.loc[:, "P8b"].map(mappings.variable_value_labels["P8b"]).map(EMISSION)
)
df["students"] = df.loc[:, "P1_1":"P1_5"].sum(axis=1)
n_students = df.query("students > 0").shape[0]
df["non_teachers"] = df.loc[:, "P1_7"]
n_non_teachers = df.query("non_teachers > 0").shape[0]
df["teachers"] = df.loc[:, "P1_6"]
n_teachers = df.query("teachers > 0").shape[0]

# %%
## Students Summer emissions
students_summer = df.query("students > 0").reset_index(drop=True)

students_summer.loc[:, "P1_1":"P1_5"] = students_summer.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_1", t="P1_5", days="P4", times_semester=(15, 5)
    ),
    axis=1,
)

students_summer["emission"] = (
    students_summer.loc[:, "P1_1":"P1_5"]
    .max(axis=1)
    .multiply(students_summer.loc[:, "P6"], axis=0)
    .multiply(students_summer.loc[:, "P8"], axis=0)
)

# %%
## Students Winter emissions
students_winter = df.query("students > 0").reset_index(drop=True)

students_winter.loc[:, "P1_1":"P1_5"] = students_winter.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_1", t="P1_5", days="P5", times_semester=(15, 5)
    ),
    axis=1,
)

students_winter.loc[:, "emission"] = (
    students_winter.loc[:, "P1_1":"P1_5"]
    .max(axis=1)
    .multiply(students_winter.loc[:, "P6"], axis=0)
    .multiply(students_winter.loc[:, "P8b"], axis=0)
)

## Students Winter emissions
students_winter_corrected = df.query("students > 0").reset_index(drop=True)

students_winter_corrected.loc[:, "P1_1":"P1_5"] = students_winter_corrected.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_1", t="P1_5", days="P5", times_semester=(15, 5)
    ),
    axis=1,
)

students_winter_corrected.loc[:, "emission"] = (
    students_winter_corrected.loc[:, "P1_1":"P1_5"]
    .max(axis=1)
    .sub(
        students_winter_corrected.apply(
            lambda x: weight_absence(x=x, condition="P25", absence="P26"),
            axis=1,
        ).fillna(0),
        axis=0,
    )
    .sub(
        students_winter_corrected.apply(
            lambda x: weight_absence(
                x=x, condition="P20", absence="P21b", weight=(7, 0)
            ),
            axis=1,
        ).fillna(0),
        axis=0,
    )
    .multiply(students_winter_corrected.loc[:, "P6"], axis=0)
    .multiply(students_winter_corrected.loc[:, "P8b"], axis=0)
)

# %%
## Teachers Summer emissions
teachers_summer = df.query("teachers > 0").reset_index(drop=True)
teachers_summer.loc[:, "P1_6"] = teachers_summer.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_6", t="P1_6", days="P4", times_semester=(22.5, 5)
    ),
    axis=1,
)
teachers_summer.loc[:, "emission"] = (
    teachers_summer.loc[:, "P1_6"]
    .multiply(teachers_summer.loc[:, "P6"], axis=0)
    .multiply(teachers_summer.loc[:, "P8"], axis=0)
)

# %%
## Teachers Winter emissions
teachers_winter = df.query("teachers > 0").reset_index(drop=True)
teachers_winter.loc[:, "P1_6"] = teachers_winter.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_6", t="P1_6", days="P5", times_semester=(22.5, 5)
    ),
    axis=1,
)
teachers_winter.loc[:, "emission"] = (
    teachers_winter.loc[:, "P1_6"]
    .multiply(teachers_winter.loc[:, "P6"], axis=0)
    .multiply(teachers_winter.loc[:, "P8b"], axis=0)
)

# %%
teachers_winter_corrected = df.query("teachers > 0").reset_index(drop=True)

teachers_winter_corrected.loc[:, "P1_6"] = teachers_winter_corrected.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_6", t="P1_6", days="P5", times_semester=(22, 5.5)
    ),
    axis=1,
)

teachers_winter_corrected.loc[:, "emission"] = (
    teachers_winter_corrected.loc[:, "P1_6"]
    .sub(
        teachers_winter_corrected.apply(
            lambda x: weight_absence(x=x, condition="P25", absence="P26"),
            axis=1,
        ).fillna(0),
        axis=0,
    )
    .sub(
        teachers_winter_corrected.apply(
            lambda x: weight_absence(
                x=x, condition="P20", absence="P21b", weight=(7, 0)
            ),
            axis=1,
        ).fillna(0),
        axis=0,
    )
    .multiply(teachers_winter_corrected.loc[:, "P6"], axis=0)
    .multiply(teachers_winter_corrected.loc[:, "P8b"], axis=0)
)
# %%
## Non-teachers Summer emissions
non_teachers_summer = df.query("non_teachers > 0").reset_index(drop=True)
non_teachers_summer.loc[:, "P1_7"] = non_teachers_summer.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_7", t="P1_7", days="P4", times_semester=(24, 5.5)
    ),
    axis=1,
)
non_teachers_summer.loc[:, "emission"] = (
    non_teachers_summer.loc[:, "P1_7"]
    .multiply(non_teachers_summer.loc[:, "P6"], axis=0)
    .multiply(non_teachers_summer.loc[:, "P8"], axis=0)
)

# %%
## Non-teachers Winter emissions
non_teachers_winter = df.query("non_teachers > 0").reset_index(drop=True)
non_teachers_winter.loc[:, "P1_7"] = non_teachers_winter.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_7", t="P1_7", days="P5", times_semester=(24, 5.5)
    ),
    axis=1,
)

non_teachers_winter.loc[:, "emission"] = (
    non_teachers_winter.loc[:, "P1_7"]
    .multiply(non_teachers_winter.loc[:, "P6"], axis=0)
    .multiply(non_teachers_winter.loc[:, "P8b"], axis=0)
)
# %%
non_teachers_winter_corrected = df.query("non_teachers > 0").reset_index(drop=True)

non_teachers_winter_corrected.loc[:, "P1_7"] = non_teachers_winter_corrected.apply(
    lambda x: compute_transport_days(
        x=x, f="P1_7", t="P1_7", days="P5", times_semester=(24, 5.5)
    ),
    axis=1,
)

non_teachers_winter_corrected.loc[:, "emission"] = (
    non_teachers_winter_corrected.loc[:, "P1_7"]
    .sub(
        non_teachers_winter_corrected.apply(
            lambda x: weight_absence(x=x, condition="P25", absence="P26"),
            axis=1,
        ).fillna(0),
        axis=0,
    )
    .sub(
        non_teachers_winter_corrected.apply(
            lambda x: weight_absence(
                x=x, condition="P20", absence="P21b", weight=(7, 0)
            ),
            axis=1,
        ).fillna(0),
        axis=0,
    )
    .multiply(non_teachers_winter_corrected.loc[:, "P6"], axis=0)
    .multiply(non_teachers_winter_corrected.loc[:, "P8b"], axis=0)
)

# %%
students_summer_emission = compute_emission(
    df=students_summer, N_GROUP=N_STUDENTS, n_group=n_students
)
print("Students Summer Emission:", students_summer_emission)
students_winter_emission = compute_emission(
    df=students_winter, N_GROUP=N_STUDENTS, n_group=n_students
)
print("Students Winter Emission:", students_winter_emission)

students_winter_corrected_emission = compute_emission(
    df=students_winter_corrected.query("emission >=0"),
    N_GROUP=N_STUDENTS,
    n_group=n_students,
)
print("Students Corrected Winter Emission:", students_winter_corrected_emission)


# %%
teachers_summer_emission = compute_emission(
    df=teachers_summer, N_GROUP=N_TEACHERS, n_group=n_teachers
)
print("Teachers Summer Emission:", teachers_summer_emission)
teachers_winter_emission = compute_emission(
    df=teachers_winter, N_GROUP=N_TEACHERS, n_group=n_teachers
)
print("Teachers Winter Emission:", teachers_winter_emission)

teachers_winter_corrected_emission = compute_emission(
    df=teachers_winter_corrected.query("emission >=0"),
    N_GROUP=N_TEACHERS,
    n_group=n_teachers,
)
print("Teachers Corrected Winter Emission:", teachers_winter_corrected_emission)

# %%
non_teachers_summer_emission = compute_emission(
    df=non_teachers_summer, N_GROUP=N_NON_TEACHERS, n_group=n_non_teachers
)
print("Non-teachers Summer Emission:", non_teachers_summer_emission)
non_teachers_winter_emission = compute_emission(
    df=non_teachers_winter, N_GROUP=N_NON_TEACHERS, n_group=n_non_teachers
)
print("Non-teachers Winter Emission:", non_teachers_winter_emission)

non_teachers_winter_corrected_emission = compute_emission(
    df=non_teachers_winter_corrected.query("emission >=0"),
    N_GROUP=N_NON_TEACHERS,
    n_group=n_non_teachers,
)
print("Non-teachers Corrected Winter Emission:", non_teachers_winter_corrected_emission)
# %%
