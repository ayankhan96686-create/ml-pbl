# County-Level Maize (Corn) Grain Yield Prediction (PBL)

Practical Machine Learning PBL project predicting county-level maize grain yield (`corn_yield_bu_acre`) across 9 US Corn Belt states (`IA`, `IL`, `IN`, `MN`, `MO`, `NE`, `OH`, `SD`, `WI`) from 2002 to 2025 using USDA NASS, NOAA ClimDiv, PRISM, ISRIC SoilGrids, and USDA RMA datasets.

## Repository Structure

```text
ml-pbl/
├── ML project/
│   └── Maize_Yield_Prediction_PBL.ipynb   # Main executable PBL notebook
├── data/
│   ├── raw/                               # Original source datasets grouped by agency
│   ├── processed/                         # Cleaned domain CSVs and integrated tables
│   ├── data_manifest.csv                  # File inventory, sizes, licenses, SHA-256
│   ├── raw_url_manifest.csv               # Direct verified GitHub Raw / LFS URLs
│   └── README.md                          # Data documentation & attribution
├── outputs/                               # Generated charts and result CSVs
├── scripts/
│   └── download_external_data.py          # Optional helper for large omitted files
├── requirements.txt
├── .gitattributes
├── .gitignore
└── README.md
```

## Quick Setup & Execution

1. **Install dependencies (Local or Google Colab):**
   ```bash
   pip install -r https://raw.githubusercontent.com/ayankhan96686-create/ml-pbl/main/requirements.txt
   ```
2. **Open and Run All:**
   Open `ML project/Maize_Yield_Prediction_PBL.ipynb` in Jupyter Notebook, VS Code, or Google Colab and run all cells from top to bottom. All required datasets load directly from verified GitHub Raw URLs listed in `data/raw_url_manifest.csv`.

3. **(Optional) Clone the repository locally:**
   ```bash
   git lfs install
   git -c http.version=HTTP/1.1 clone --depth 1 https://github.com/ayankhan96686-create/ml-pbl.git
   ```

## Notebook Highlights

- **Per-Dataset Analytics & Cleaning:** Inspects all 8 source tables (`head`, `tail`, `shape`, `info`, `describe`, missing %, duplicates, `nunique`, `dtypes`) and enforces 5-digit `county_fips` string keys (`zfill(5)`).
- **Step-by-Step Dataset Joining:** Demonstrates 5 explicit joins (`USDA Yield`, `NOAA`, `PRISM`, `USDA RMA`, `SoilGrids`, and state-level `Crop Condition/Progress`) with before/after row and column counts.
- **2012 Drought & Heat Case Study:** Compares `2011`, `2012`, and `2013` across consistent counties, evaluates state and county yield losses, and computes June/July/August temperature anomalies and rainfall deficits relative to `2002–2011` baselines.
- **Machine Learning & Evaluation:** Evaluates `LinearRegression`, `Ridge`, `Lasso`, `DecisionTreeRegressor`, `RandomForestRegressor`, `GradientBoostingRegressor`, and `XGBoost` on an 80:20 random holdout split (`2002–2025`), plus a supplementary `Low/Medium/High` yield classification confusion matrix and `f_regression` F-tests.
