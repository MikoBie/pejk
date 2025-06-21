# `Emission study 2025`

Scripts to analyze data from PEJK study about the University of Warsaw
emission. This might also be used to analyze data to come, however, it must
have the same structure as the data from 2025 (the same questions, etc.).
Otherwise, it will have to be adjusted. Please note that if you change the
names of the variables everything will go south. Therefore, I would suggest to
keep the names of the variables as they are. 

**IMPORTANT**: the sizes of the groups are hardwired in `pejk/config.py`.

## Repo Structure

```bash
├── README.md                      # README
├── .gitignore                     # Type of files which git should ignore
├── .pre-commit.yaml               # Pre-commit hooks configuration
├── environment.yaml               # Necessary modules
├── pyproject.toml                 # Project configuration
├── pejk                           # Module with custom functions
├── tests                          # Module with unit tests of custom functions
├── data                           
│   └── raw                        # Folder for raw data, by default `raw_data.sav`
├── scripts                           
│   ├── compute_*.yaml             # Script to compute a given category
│   └── plot_*.py                  # Script to plot and create an excel file for a given category
├── png                            # Folder with plots                           
└── excel                          # Folder with excels
```

## Main dependencies

* _python3.13.5_ ([anaconda distribution](https://www.anaconda.com/products/distribution) is preferred)
* other _python_ dependencies are specified in `environment.yaml`


## Setup

1. Clone the repo: `git@github.com:MikoBie/pejk.git`.
2. Set up the proper virtual environment.
```bash
cd pejk
conda env create --file environment.yaml
```
3. Activate `pre-commit`.
```bash
pre-commit install
```
4. Cross fingers.

## Running Tests

```bash
pytest
```
