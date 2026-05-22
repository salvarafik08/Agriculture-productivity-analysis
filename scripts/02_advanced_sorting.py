"""
🌾 AGRICULTURAL DATASET - ADVANCED SORTING TECHNIQUES
Advanced sorting with filtering, ranking, and grouping
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT_DIR / "data" / "raw" / "agriculture_dataset-95c6.csv"

# Load the dataset
df = pd.read_csv(DATA_FILE)

print("=" * 100)
print("🌾 ADVANCED SORTING & RANKING TECHNIQUES")
print("=" * 100)

# ============= ADVANCED 1: Sort with Conditional Filtering =============
print("\n✨ ADVANCED 1: HIGH YIELD FARMS (>30 tons) - Sorted by Efficiency")
print("-" * 100)
high_yield = df[df['Yield(tons)'] > 30].sort_values('Yield(tons)', ascending=False)
print(high_yield[['Farm_ID', 'Crop_Type', 'Yield(tons)', 'Fertilizer_Used(tons)']].head(10))
print(f"\n📊 Found {len(high_yield)} high-yield farms")

# ============= ADVANCED 2: Rank Within Groups =============
print("\n✨ ADVANCED 2: TOP 3 FARMS PER CROP TYPE (by Yield)")
print("-" * 100)
top_3_per_crop = df.sort_values(['Crop_Type', 'Yield(tons)'], ascending=[True, False])
top_3_per_crop['Rank'] = top_3_per_crop.groupby('Crop_Type').cumcount() + 1
top_3_per_crop = top_3_per_crop[top_3_per_crop['Rank'] <= 3]
print(top_3_per_crop[['Farm_ID', 'Crop_Type', 'Yield(tons)', 'Rank']].to_string())

# ============= ADVANCED 3: Percentile Ranking =============
print("\n✨ ADVANCED 3: YIELD PERCENTILE RANKING")
print("-" * 100)
df_ranked = df.copy()
df_ranked['Yield_Percentile'] = pd.qcut(df_ranked['Yield(tons)'], q=4, labels=['Low', 'Medium-Low', 'Medium-High', 'High'])
sorted_percentile = df_ranked.sort_values('Yield(tons)', ascending=False)
print(sorted_percentile[['Farm_ID', 'Yield(tons)', 'Yield_Percentile']].head(15))

# ============= ADVANCED 4: Sort by Multiple Criteria with Different Orders =============
print("\n✨ ADVANCED 4: COMPLEX SORT - Season(Asc), Yield(Desc), Area(Desc)")
print("-" * 100)
complex_sort = df.sort_values(
    ['Season', 'Yield(tons)', 'Farm_Area(acres)'],
    ascending=[True, False, False]
)
print(complex_sort[['Farm_ID', 'Season', 'Yield(tons)', 'Farm_Area(acres)']].head(15))

# ============= ADVANCED 5: Sort by Calculated Efficiency =============
print("\n✨ ADVANCED 5: FARMS RANKED BY EFFICIENCY (Yield per Fertilizer)")
print("-" * 100)
df_efficiency = df.copy()
df_efficiency['Efficiency'] = (df_efficiency['Yield(tons)'] / df_efficiency['Fertilizer_Used(tons)']).round(2)
df_efficiency = df_efficiency.sort_values('Efficiency', ascending=False)
print(df_efficiency[['Farm_ID', 'Yield(tons)', 'Fertilizer_Used(tons)', 'Efficiency']].head(12))

# ============= ADVANCED 6: Sort by Water Efficiency =============
print("\n✨ ADVANCED 6: WATER EFFICIENCY RANKING (Yield per Water Usage)")
print("-" * 100)
df_water = df.copy()
df_water['Water_Efficiency'] = (df_water['Yield(tons)'] / df_water['Water_Usage(cubic meters)']).round(6)
df_water = df_water.sort_values('Water_Efficiency', ascending=False)
print(df_water[['Farm_ID', 'Yield(tons)', 'Water_Usage(cubic meters)', 'Water_Efficiency']].head(12))

# ============= ADVANCED 7: Top Performers by Category =============
print("\n✨ ADVANCED 7: TOP PERFORMER BY IRRIGATION TYPE")
print("-" * 100)
top_by_irrigation = df.sort_values('Yield(tons)', ascending=False).drop_duplicates('Irrigation_Type')
print(top_by_irrigation[['Farm_ID', 'Irrigation_Type', 'Yield(tons)', 'Crop_Type']])

# ============= ADVANCED 8: Top Performers by Soil Type =============
print("\n✨ ADVANCED 8: TOP PERFORMER BY SOIL TYPE")
print("-" * 100)
top_by_soil = df.sort_values('Yield(tons)', ascending=False).drop_duplicates('Soil_Type')
print(top_by_soil[['Farm_ID', 'Soil_Type', 'Yield(tons)', 'Crop_Type']])

# ============= ADVANCED 9: Bottom Performers (Improvement Candidates) =============
print("\n✨ ADVANCED 9: BOTTOM 10 PERFORMERS (Candidates for Improvement)")
print("-" * 100)
bottom_performers = df.sort_values('Yield(tons)', ascending=True).head(10)
print(bottom_performers[['Farm_ID', 'Crop_Type', 'Yield(tons)', 'Irrigation_Type', 'Soil_Type']])

# ============= ADVANCED 10: Sort by Multiple Factors with Ranking =============
print("\n✨ ADVANCED 10: COMPREHENSIVE RANKING SYSTEM")
print("-" * 100)
df_rank = df.copy()
df_rank['Yield_Rank'] = df_rank['Yield(tons)'].rank(ascending=False)
df_rank['Area_Rank'] = df_rank['Farm_Area(acres)'].rank(ascending=False)
df_rank['Efficiency'] = (df_rank['Yield(tons)'] / df_rank['Fertilizer_Used(tons)']).round(2)
df_rank['Efficiency_Rank'] = df_rank['Efficiency'].rank(ascending=False)
df_rank['Overall_Score'] = (df_rank['Yield_Rank'] + df_rank['Efficiency_Rank']) / 2
df_rank = df_rank.sort_values('Overall_Score', ascending=True)
print(df_rank[['Farm_ID', 'Yield_Rank', 'Efficiency_Rank', 'Overall_Score']].head(10))

print("\n" + "=" * 100)
print("✅ Advanced sorting techniques completed!")
print("=" * 100)
