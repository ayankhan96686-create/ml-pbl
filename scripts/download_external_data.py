"""
Optional helper to fetch large or external raw files not stored in Git directly.
Note: Running the main PBL notebook does NOT require downloading these files.
"""

import argparse
from pathlib import Path
import urllib.request

REPO_ROOT = Path(__file__).resolve().parent.parent


def download_file(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        print(f"Already exists: {dest} ({dest.stat().st_size / 1048576:.2f} MB)")
        return
    print(f"Downloading {url} -> {dest} ...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp, dest.open("wb") as out:
        out.write(resp.read())
    print(f"Saved {dest.stat().st_size / 1048576:.2f} MB")


def main() -> None:
    parser = argparse.ArgumentParser(description="Download optional external raw files for ml-pbl.")
    parser.add_argument("--county-zip", action="store_true", help="Download tl_2024_us_county.zip directly from US Census if Git LFS was skipped.")
    parser.add_argument("--soilgrids-vrt", action="store_true", help="Download ISRIC SoilGrids 2.0 global VRT files.")
    args = parser.parse_args()

    if args.county_zip:
        download_file(
            "https://www2.census.gov/geo/tiger/TIGER2024/COUNTY/tl_2024_us_county.zip",
            REPO_ROOT / "data" / "raw" / "county_boundaries" / "tl_2024_us_county.zip",
        )

    if args.soilgrids_vrt:
        props = ["bdod", "clay", "phh2o", "sand", "silt", "soc"]
        depths = ["0-5cm", "5-15cm", "15-30cm"]
        for p in props:
            for d in depths:
                url = f"https://files.isric.org/soilgrids/latest/data/{p}/{p}_{d}_mean.vrt"
                dest = REPO_ROOT / "data" / "raw" / "soilgrids" / p / f"{p}_{d}_mean.vrt"
                download_file(url, dest)

    print("\nNote on CDL_2020_19_Iowa.tif (124 MB):")
    print("  USDA NASS CropScape CDL state GeoTIFFs can be downloaded manually from:")
    print("  https://www.nass.usda.gov/Research_and_Science/Cropland/Release/index.php")


if __name__ == "__main__":
    main()
