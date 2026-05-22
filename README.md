# Agriculture Data Analysis Workspace

This workspace is now organized into clear, purpose-driven folders:

- `data/`
  - `raw/` contains source datasets
  - `processed/` contains cleaned or dashboard-ready exports
- `scripts/` contains Python analysis scripts
- `reports/` contains dashboard files, Excel reports, and HTML visualizations
- `outputs/` contains generated exports such as `sorted_data/`
- `docs/` contains markdown documentation and usage guides
- `Agriculture-productivity-analysis/` remains as a separate legacy project folder

## Current structure

- `data/raw/agriculture_dataset-95c6.csv`
- `data/processed/agriculture_data_for_powerbi.csv`
- `data/processed/dashboard_data.json`
- `scripts/01_basic_sorting.py`
- `scripts/02_advanced_sorting.py`
- `scripts/03_sorting_by_category.py`
- `scripts/04_sorting_with_export.py`
- `scripts/05_sorting_utilities.py`
- `outputs/sorted_data/`
- `reports/Agriculture_PowerBI_Dashboard.xlsx`
- `reports/Agriculture_Dataset_With_Formulas.xlsx`
- `reports/Agriculture_Dataset_Professional.xlsx`
- `reports/powerbi_dashboard.html`
- `reports/index.html`
- `docs/` for supporting documentation

## How to run the Python scripts

From the repository root:

```bash
cd "d:\\Data analysis"
cd scripts
py 01_basic_sorting.py
py 02_advanced_sorting.py
py 03_sorting_by_category.py
py 04_sorting_with_export.py
py 05_sorting_utilities.py
```

## Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Notes

- The raw dataset is now in `data/raw/`.
- Dashboard-ready files are in `data/processed/`.
- Reports and visualization files are in `reports/`.
- Generated output files remain under `outputs/sorted_data/`.

## Recommended next step

If you want to continue refining the project, keep the scripts in `scripts/`, keep source data in `data/raw/`, and keep generated and exported files in `outputs/`.
