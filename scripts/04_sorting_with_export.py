"""
🌾 AGRICULTURAL DATASET - SORTING WITH EXPORT TO FILES
Sort data and save to Excel, CSV, and JSON formats
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
DATA_FILE = ROOT_DIR / "data" / "raw" / "agriculture_dataset-95c6.csv"
OUTPUT_DIR = ROOT_DIR / "outputs" / "sorted_data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load the dataset
df = pd.read_csv(DATA_FILE)

print("=" * 100)
print("🌾 SORTING & EXPORT TO MULTIPLE FORMATS")
print("=" * 100)

# ============= SORT 1: By Yield - Export to CSV =============
print("\n1️⃣  Sorting by YIELD (Descending) - Export to CSV")
print("-" * 100)
sorted_yield = df.sort_values('Yield(tons)', ascending=False).reset_index(drop=True)
sorted_yield.index = sorted_yield.index + 1
csv_file = OUTPUT_DIR / '01_sorted_by_yield_descending.csv'
sorted_yield.to_csv(csv_file)
print(f"✅ Saved to: {csv_file}")
print(f"   Records: {len(sorted_yield)}")
print(sorted_yield[['Farm_ID', 'Crop_Type', 'Yield(tons)']].head(10))

# ============= SORT 2: By Fertilizer - Export to Excel =============
print("\n2️⃣  Sorting by FERTILIZER USAGE - Export to Excel")
print("-" * 100)
sorted_fert = df.sort_values('Fertilizer_Used(tons)', ascending=False).reset_index(drop=True)
sorted_fert.index = sorted_fert.index + 1
excel_file = OUTPUT_DIR / '02_sorted_by_fertilizer.xlsx'
sorted_fert.to_excel(excel_file)
print(f"✅ Saved to: {excel_file}")
print(sorted_fert[['Farm_ID', 'Crop_Type', 'Fertilizer_Used(tons)']].head(10))

# ============= SORT 3: By Water Usage - Multi-sheet Excel =============
print("\n3️⃣  Sorting by WATER USAGE with Statistics")
print("-" * 100)
sorted_water = df.sort_values('Water_Usage(cubic meters)', ascending=False).reset_index(drop=True)
sorted_water.index = sorted_water.index + 1

# Create statistics summary
water_stats = pd.DataFrame({
    'Metric': ['Total Records', 'Average Water Usage', 'Max Water Usage', 'Min Water Usage', 'Total Water Used'],
    'Value': [
        len(sorted_water),
        f"{sorted_water['Water_Usage(cubic meters)'].mean():.2f} m³",
        f"{sorted_water['Water_Usage(cubic meters)'].max():.2f} m³",
        f"{sorted_water['Water_Usage(cubic meters)'].min():.2f} m³",
        f"{sorted_water['Water_Usage(cubic meters)'].sum():.0f} m³"
    ]
})

# Export to Excel with multiple sheets
excel_file = OUTPUT_DIR / '03_water_usage_analysis.xlsx'
with pd.ExcelWriter(excel_file) as writer:
    sorted_water.to_excel(writer, sheet_name='Sorted Data')
    water_stats.to_excel(writer, sheet_name='Statistics', index=False)
print(f"✅ Saved to: {excel_file} (2 sheets)")
print(water_stats)

# ============= SORT 4: By Farm Area - JSON Export =============
print("\n4️⃣  Sorting by FARM AREA - Export to JSON")
print("-" * 100)
sorted_area = df.sort_values('Farm_Area(acres)', ascending=False).reset_index(drop=True)
sorted_area_dict = sorted_area.to_dict(orient='records')
json_file = OUTPUT_DIR / '04_sorted_by_farm_area.json'
with open(json_file, 'w') as f:
    json.dump(sorted_area_dict, f, indent=2)
print(f"✅ Saved to: {json_file}")
print(f"   Records: {len(sorted_area_dict)}")
print(sorted_area[['Farm_ID', 'Farm_Area(acres)', 'Yield(tons)']].head(10))

# ============= SORT 5: Top 10 by Crop - Export Multiple CSVs =============
print("\n5️⃣  Top 10 Farms by CROP TYPE - Export Individual CSVs")
print("-" * 100)
for crop in sorted(df['Crop_Type'].unique()):
    crop_data = df[df['Crop_Type'] == crop].sort_values('Yield(tons)', ascending=False).head(10)
    csv_file = OUTPUT_DIR / f'crop_top10_{crop.lower()}.csv'
    crop_data.to_csv(csv_file, index=False)
    print(f"✅ {crop:12s} - {len(crop_data):2d} records -> {csv_file}")

# ============= SORT 6: Ranked Farms by Efficiency - Export with Ranks =============
print("\n6️⃣  EFFICIENCY RANKING - Export with Rank Column")
print("-" * 100)
df_efficiency = df.copy()
df_efficiency['Efficiency_Ratio'] = (df_efficiency['Yield(tons)'] / df_efficiency['Fertilizer_Used(tons)']).round(2)
df_efficiency['Efficiency_Rank'] = df_efficiency['Efficiency_Ratio'].rank(ascending=False, method='min').astype(int)
df_efficiency = df_efficiency.sort_values('Efficiency_Rank')
df_efficiency = df_efficiency[['Farm_ID', 'Crop_Type', 'Yield(tons)', 'Fertilizer_Used(tons)', 'Efficiency_Ratio', 'Efficiency_Rank']]

excel_file = OUTPUT_DIR / '06_efficiency_ranking.xlsx'
df_efficiency.to_excel(excel_file, index=False)
print(f"✅ Saved to: {excel_file}")
print(df_efficiency.head(15))

# ============= SORT 7: Grouped Summary by Category - Export Pivot Table =============
print("\n7️⃣  CATEGORY SUMMARY - Pivot Tables Export")
print("-" * 100)

# Crop summary
crop_summary = df.groupby('Crop_Type').agg({
    'Yield(tons)': ['mean', 'sum', 'count', 'max', 'min'],
    'Farm_Area(acres)': 'mean',
    'Fertilizer_Used(tons)': 'mean',
    'Water_Usage(cubic meters)': 'mean'
}).round(2)

crop_summary.columns = ['Avg_Yield', 'Total_Yield', 'Farm_Count', 'Max_Yield', 'Min_Yield', 
                         'Avg_Area', 'Avg_Fertilizer', 'Avg_Water']
crop_summary = crop_summary.sort_values('Avg_Yield', ascending=False)

excel_file = OUTPUT_DIR / '07_crop_summary.xlsx'
crop_summary.to_excel(excel_file)
print(f"✅ Saved Crop Summary to: {excel_file}")
print(crop_summary)

# ============= SORT 8: Season & Irrigation Cross Analysis =============
print("\n8️⃣  SEASON × IRRIGATION ANALYSIS - Export Matrix")
print("-" * 100)

season_irrig = df.pivot_table(
    values='Yield(tons)',
    index='Season',
    columns='Irrigation_Type',
    aggfunc='mean'
).round(2)

excel_file = OUTPUT_DIR / '08_season_irrigation_matrix.xlsx'
season_irrig.to_excel(excel_file)
print(f"✅ Saved Season-Irrigation Matrix to: {excel_file}")
print(season_irrig)

# ============= SORT 9: Bottom 10 Performers - Export for Improvement Planning =============
print("\n9️⃣  BOTTOM 10 PERFORMERS - Export for Improvement")
print("-" * 100)
bottom_10 = df.nsmallest(10, 'Yield(tons)')[['Farm_ID', 'Crop_Type', 'Yield(tons)', 'Irrigation_Type', 'Soil_Type', 'Fertilizer_Used(tons)']]
bottom_10['Improvement_Target'] = bottom_10['Yield(tons)'] * 1.25  # 25% improvement target
bottom_10['Gap_to_Target'] = (bottom_10['Improvement_Target'] - bottom_10['Yield(tons)']).round(2)

excel_file = OUTPUT_DIR / '09_bottom_performers_improvement.xlsx'
bottom_10.to_excel(excel_file, index=False)
print(f"✅ Saved Bottom Performers to: {excel_file}")
print(bottom_10)

# ============= SORT 10: Comprehensive Report - Multi-sheet Excel =============
print("\n🔟 COMPREHENSIVE REPORT - Multi-sheet Excel Export")
print("-" * 100)

excel_file = OUTPUT_DIR / '10_comprehensive_report.xlsx'
with pd.ExcelWriter(excel_file) as writer:
    # Sheet 1: All data sorted by yield
    all_sorted = df.sort_values('Yield(tons)', ascending=False).reset_index(drop=True)
    all_sorted.index = all_sorted.index + 1
    all_sorted.to_excel(writer, sheet_name='All Data by Yield')
    
    # Sheet 2: Crop statistics
    crop_stats = df.groupby('Crop_Type').agg({
        'Yield(tons)': ['mean', 'count'],
        'Farm_Area(acres)': 'mean'
    }).round(2)
    crop_stats.columns = ['Avg_Yield', 'Count', 'Avg_Area']
    crop_stats = crop_stats.sort_values('Avg_Yield', ascending=False)
    crop_stats.to_excel(writer, sheet_name='Crop Statistics')
    
    # Sheet 3: Irrigation statistics
    irrig_stats = df.groupby('Irrigation_Type').agg({
        'Yield(tons)': 'mean',
        'Water_Usage(cubic meters)': 'mean',
        'Fertilizer_Used(tons)': 'mean'
    }).round(2)
    irrig_stats = irrig_stats.sort_values('Yield(tons)', ascending=False)
    irrig_stats.to_excel(writer, sheet_name='Irrigation Statistics')
    
    # Sheet 4: Soil type statistics
    soil_stats = df.groupby('Soil_Type').agg({
        'Yield(tons)': 'mean',
        'Farm_Area(acres)': 'mean'
    }).round(2)
    soil_stats = soil_stats.sort_values('Yield(tons)', ascending=False)
    soil_stats.to_excel(writer, sheet_name='Soil Statistics')
    
    # Sheet 5: Summary statistics
    summary = pd.DataFrame({
        'Metric': ['Total Farms', 'Average Yield', 'Max Yield', 'Min Yield', 'Total Production', 'Average Farm Size'],
        'Value': [
            len(df),
            f"{df['Yield(tons)'].mean():.2f} tons",
            f"{df['Yield(tons)'].max():.2f} tons",
            f"{df['Yield(tons)'].min():.2f} tons",
            f"{df['Yield(tons)'].sum():.0f} tons",
            f"{df['Farm_Area(acres)'].mean():.2f} acres"
        ]
    })
    summary.to_excel(writer, sheet_name='Summary', index=False)

print(f"✅ Saved Comprehensive Report to: {excel_file} (5 sheets)")

# ============= SUMMARY OF EXPORTS =============
print("\n" + "=" * 100)
print("📦 EXPORT SUMMARY")
print("=" * 100)
print(f"Output Directory: {OUTPUT_DIR}")
print(f"Total files created: 10+ files")
print("\nFiles created:")
print("  1. CSV - Sorted by Yield")
print("  2. XLSX - Sorted by Fertilizer")
print("  3. XLSX - Water Usage Analysis (2 sheets)")
print("  4. JSON - Sorted by Farm Area")
print("  5. CSV - Top 10 per Crop (10 files)")
print("  6. XLSX - Efficiency Ranking")
print("  7. XLSX - Crop Summary")
print("  8. XLSX - Season × Irrigation Matrix")
print("  9. XLSX - Bottom Performers for Improvement")
print(" 10. XLSX - Comprehensive Multi-sheet Report (5 sheets)")
print("\n✅ All sorting and export operations completed!")
print("=" * 100)
