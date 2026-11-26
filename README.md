# County-Level Maize (Corn) Grain Yield Prediction (PBL)

Practical Machine Learning project predicting county-level maize grain yield (`corn_yield_bu_acre`) across 9 US Corn Belt states (`IA`, `IL`, `IN`, `MN`, `MO`, `NE`, `OH`, `SD`, `WI`) from 2002 to 2025 using agricultural, climate, soil, and crop insurance data.

## Repository Structure

```text
ml-pbl/
├── ML project/
│   └── Maize_Yield_Prediction_PBL.ipynb   # Main executable PBL notebook
├── data/
│   ├── raw/                               # Original source data grouped by agency
│   ├── processed/                         # Cleaned domain CSVs and integrated tables
│   ├── data_manifest.csv                  # SHA-256 checksums, sizes, licenses, URLs
│   └── README.md                          # Detailed data inventory & attribution
├── outputs/                               # Generated charts and result tables
├── scripts/
│   └── download_external_data.py          # Optional downloader for large omitted files
├── requirements.txt
├── .gitattributes
├── .gitignore
└── README.md
```

## Quick Setup (Local or Google Colab)

1. **Clone the repository (with Git LFS for the 80 MB county boundary ZIP):**
   ```bash
   git lfs install
   git -c http.version=HTTP/1.1 clone --depth 1 https://github.com/ayankhan96686-create/ml-pbl.git
   cd ml-pbl
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the notebook:**
   Open `ML project/Maize_Yield_Prediction_PBL.ipynb` in Jupyter Notebook, VS Code, or Google Colab and run all cells from top to bottom.
   - If the notebook is opened outside a local clone (for example, directly inside Google Colab), its setup cell automatically clones this public repository so all datasets load cleanly.

## Key Methodological Rules Followed

- **Chronological Validation:** Models train on `2002–2020` and are tested on future unseen years `2021–2025` (no random shuffling across years).
- **Zero Data Leakage:** Missing-value imputation, scaling, one-hot encoding, statistical feature screening (`f_regression`), and classification thresholds are fitted on training data (`2002–2020`) only. Post-harvest columns (`rma_postharvest_*`, `state_progress_postharvest_*`, `noaa_prcp_annual_in`) are excluded from predictors.
- **PRISM Window Check:** Historical `2002–2025` PRISM tables contain full-year averages, so growing-season heat and rainfall analyses use monthly `NOAA ClimDiv` (`May–September`) series instead.
- **No Fabricated Data:** Unavailable satellite datasets (`MODIS`, `Landsat`, `Sentinel-2`, `ERA5-Land`, `gSSURGO`) are documented clearly and never simulated.
