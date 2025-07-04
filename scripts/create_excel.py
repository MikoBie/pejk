# %%
from pejk import EXCEL, DATA
import pandas as pd
import os

# %%
lst_fls = [item for item in os.scandir(EXCEL) if "xlsx" in item.name]
lst_fls = sorted(lst_fls, key=lambda x: x.name.split(".")[0])


# %%
def main() -> None:
    writer = pd.ExcelWriter(DATA / "percenteges.xlsx", engine="xlsxwriter")
    for item in lst_fls:
        temp = pd.read_excel(item)
        sheet_name = item.name.replace(".xlsx", "")
        temp.to_excel(writer, sheet_name=sheet_name, index=False)

    writer.close()


# %%
if __name__ != "__main__":
    main()
