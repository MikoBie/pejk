__all__ = ["utils"]
from pathlib import Path
import os

ROOT = Path(__file__).absolute().parent.parent
DATA = ROOT / "data"
RAW = DATA / "raw"
PROC = DATA / "processed"
PNG = ROOT / "png"
EXCEL = ROOT / "excel"
if not os.path.exists(PNG):
    os.makedirs(PNG)
if not os.path.exists(EXCEL):
    os.makedirs(EXCEL)
