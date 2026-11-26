# Dataset Inventory and Provenance (`data/`)

This folder holds the authentic raw and processed datasets used in the **County-Level Maize (Corn) Grain Yield Prediction** PBL project across 9 US Corn Belt states (`IA`, `IL`, `IN`, `MN`, `MO`, `NE`, `OH`, `SD`, `WI`) for `2002–2025` (with `2026` kept unlabeled).

See [data_manifest.csv](data_manifest.csv) for the full file-by-file inventory, SHA-256 checksums, sizes, licensing terms, and hosting status.

## Folder Structure

| Path | Contents | Granularity | Hosting |
| :--- | :--- | :--- | :--- |
| `processed/cleaned/` | 8 cleaned domain CSVs (`USDA_Yield_Cleaned.csv`, `NOAA_Climate_Cleaned.csv`, `PRISM_Climate_Cleaned.csv`, `SoilGrids_Cleaned.csv`, `RMA_Cleaned.csv`, `Crop_Condition_Cleaned.csv`, `Crop_Progress_Cleaned.csv`, `Fertilizer_Cleaned.csv`) | County-Year / County / State-Year | Standard Git |
| `processed/integrated/` | 3 merged tables (`County_Year_Feature_Table.csv`, `County_Year_Master_Dataset.csv`, `Future_2026_Feature_Table.csv`) | County-Year | Standard Git |
| `raw/usda_nass/` | Raw USDA NASS QuickStats corn yield CSVs | County-Year | Standard Git |
| `raw/noaa_climate/` | NOAA ClimDiv raw snapshot (`20261006`) + extracted 9-state CSVs | County-Month / Year | Standard Git |
| `raw/prism/` | PRISM 4 km annual ZIPs (`2002–2025`, note `2023 ppt` absent) and provisional `2026` monthly ZIPs | 4 km Grid | Standard Git |
| `raw/soilgrids/` | ISRIC SoilGrids 2.0 Corn Belt regional GeoTIFFs (`0–5`, `5–15`, `15–30 cm`) | 250 m Grid (Static) | Standard Git |
| `raw/usda_rma/` | USDA RMA Summary of Business archives (`sobcov_2002..2026.zip`) | County-Policy-Year | Standard Git |
| `raw/crop_condition_progress/` | USDA NASS weekly Crop Condition & Crop Progress CSVs | State-Week | Standard Git |
| `raw/fertilizer/` | USDA NASS Chemical Use CSV & USDA ERS fertilizer workbook | State-Year (sparse) | Standard Git |
| `raw/county_boundaries/` | `Study_Area_Counties_FIPS.csv`, `national_county2020.txt`, `tl_2024_us_state.zip`, and `tl_2024_us_county.zip` | County / State Polygons | Standard Git + Git LFS (`tl_2024_us_county.zip`, 80.03 MB) |
| `raw/usda_cdl/` | USDA CDL crop codes & legend (`CDL_2020_19_Iowa.tif` omitted, see below) | Metadata only | Standard Git |
| `raw/nasa_power/` | Single-centroid daily agroclimatology CSV (`lat=42.0, lon=-93.5`) | Point Daily | Standard Git |

## Files Not Hosted Directly in Git (Size / Quota Limits)

1. **`CDL_2020_19_Iowa.tif` (`124.00 MB`)**
   - **Why not uploaded:** Exceeds GitHub's 100 MB standard Git limit, and omitted from Git LFS so the account stays safely within GitHub's 1 GB Free LFS storage and bandwidth allowance.
   - **How to obtain:** Public domain USDA NASS Cropland Data Layer (`https://www.nass.usda.gov/Research_and_Science/Cropland/Release/index.php` or `https://croplandcros.scinet.usda.gov/`). Note: not needed to execute the PBL notebook.
2. **ISRIC SoilGrids Global `.vrt` Files (`18` files, `88.1 MB` total)**
   - **Why not uploaded:** Global virtual tile indexes pointing to ISRIC servers; the extracted Corn Belt GeoTIFFs (`regional_rasters/*.tif`, `9.23 MB`) are included directly instead.
   - **How to obtain:** Run `python scripts/download_external_data.py --soilgrids-vrt` or fetch from `https://files.isric.org/soilgrids/latest/data/`.

## Unavailable Sources (Not Collected Locally)

The following external products existed only as README access notes in the original project and have **zero data files** here (no synthetic replacements were created):
- **ERA5-Land** (`https://cds.climate.copernicus.eu/`)
- **MODIS NDVI/EVI & LAI/FPAR** (`https://appeears.earthdatacloud.nasa.gov/`)
- **Landsat Collection 2** (`https://earthexplorer.usgs.gov/`)
- **Sentinel-2 MSI** (`https://dataspace.copernicus.eu/`)
- **USDA NRCS gSSURGO** (`https://www.nrcs.usda.gov/resources/data-and-reports/gridded-soil-survey-geographic-database-gssurgo`)

## Attribution & Licensing

- **USDA NASS, NOAA NCEI, USDA RMA, USDA ERS, US Census Bureau, NASA POWER:** US Government Public Domain / Open Data.
- **PRISM Climate Group (Oregon State University):** Free academic reproduction and distribution with attribution (`https://prism.oregonstate.edu`, Daly et al., 2008).
- **ISRIC SoilGrids 2.0:** Licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) (Poggio et al., 2021).
