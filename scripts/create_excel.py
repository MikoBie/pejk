# %%
from pejk import EXCEL, DATA
import pandas as pd
import os
import re

# %%
rgx = re.compile(r"\d+")
lst_fls = [
    item for item in os.scandir(EXCEL) if "xlsx" in item.name and rgx.search(item.name)
]
lst_fls = sorted(lst_fls, key=lambda x: int(rgx.search(x.name).group()))


# %%
writer = pd.ExcelWriter(DATA / "data.xlsx", engine="xlsxwriter")
for item in lst_fls:
    temp = pd.read_excel(item)
    sheet_name = item.name.replace(".xlsx", "")
    temp.to_excel(writer, sheet_name=sheet_name, index=False)

writer.close()
