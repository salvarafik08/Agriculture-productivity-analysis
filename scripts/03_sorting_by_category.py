"""
🌾 AGRICULTURAL DATASET - CATEGORY-BASED SORTING
Sort and analyze by specific farm characteristics
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT_DIR / "data" / "raw" / "agriculture_dataset-95c6.csv"

# Load the dataset
df = pd.read_csv(DATA_FILE)

print("=" * 100)
print("🌾 SORTING BY CATEGORY - COMPREHENSIVE ANALYSIS")
print("=" * 100)

# ============= CROP-BASED SORTING =============
print("\n📍 CROP TYPE ANALYSIS")
print("-" * 100)

crops = df['Crop_Type'].unique()
print(f"\nAvailable Crops: {sorted(crops)}\n")

for crop in sorted(crops):
    crop_data = df[df['Crop_Type'] == crop].sort_values('Yield(tons)', ascending=False)
    avg_yield = crop_data['Yield(tons)'].mean()
    max_yield = crop_data['Yield(tons)'].max()
    min_yield = crop_data['Yield(tons)'].min()
    count = len(crop_data)
    
    print(f"🌾 {crop:12s} | Count: {count:2d} | Avg: {avg_yield:6.2f} | Max: {max_yield:6.2f} | Min: {min_yield:6.2f} tons")
    print(f"   Top Farm: {crop_data.iloc[0]['Farm_ID']} ({crop_data.iloc[0]['Yield(tons)']:.2f} tons)")
    print()

# ============= IRRIGATION-TYPE SORTING =============
print("\n💧 IRRIGATION TYPE ANALYSIS")
print("-" * 100)

irrigation_types = df['Irrigation_Type'].unique()
print(f"\nAvailable Irrigation Types: {sorted(irrigation_types)}\n")

for irrig in sorted(irrigation_types):
    irrig_data = df[df['Irrigation_Type'] == irrig].sort_values('Yield(tons)', ascending=False)
    avg_yield = irrig_data['Yield(tons)'].mean()
    avg_water = irrig_data['Water_Usage(cubic meters)'].mean()
    count = len(irrig_data)
    
    print(f"💧 {irrig:12s} | Farms: {count:2d} | Avg Yield: {avg_yield:6.2f} tons | Avg Water: {avg_water:10.0f} m³")
    print(f"   Most Efficient: {irrig_data.iloc[0]['Farm_ID']} ({irrig_data.iloc[0]['Yield(tons)']:.2f} tons)")
    print()

# ============= SOIL-TYPE SORTING =============
print("\n🌱 SOIL TYPE ANALYSIS")
print("-" * 100)

soil_types = df['Soil_Type'].unique()
print(f"\nAvailable Soil Types: {sorted(soil_types)}\n")

for soil in sorted(soil_types):
    soil_data = df[df['Soil_Type'] == soil].sort_values('Yield(tons)', ascending=False)
    avg_yield = soil_data['Yield(tons)'].mean()
    avg_fert = soil_data['Fertilizer_Used(tons)'].mean()
    count = len(soil_data)
    
    print(f"🌱 {soil:10s} | Farms: {count:2d} | Avg Yield: {avg_yield:6.2f} tons | Avg Fertilizer: {avg_fert:5.2f} tons")
    print(f"   Best Performer: {soil_data.iloc[0]['Farm_ID']} ({soil_data.iloc[0]['Yield(tons)']:.2f} tons)")
    print()

# ============= SEASON-BASED SORTING =============
print("\n🌾 SEASON ANALYSIS")
print("-" * 100)

seasons = df['Season'].unique()
print(f"\nAvailable Seasons: {sorted(seasons)}\n")

for season in sorted(seasons):
    season_data = df[df['Season'] == season].sort_values('Yield(tons)', ascending=False)
    avg_yield = season_data['Yield(tons)'].mean()
    total_area = season_data['Farm_Area(acres)'].sum()
    count = len(season_data)
    
    print(f"🌾 {season:10s} | Farms: {count:2d} | Avg Yield: {avg_yield:6.2f} tons | Total Area: {total_area:10.0f} acres")
    print(f"   Top Farm: {season_data.iloc[0]['Farm_ID']} ({season_data.iloc[0]['Yield(tons)']:.2f} tons)")
    print()

# ============= COMBINATION ANALYSIS: CROP + SEASON =============
print("\n🔄 CROP × SEASON COMBINATION (Top 3 by Yield)")
print("-" * 100)

combinations = df.groupby(['Crop_Type', 'Season']).agg({
    'Yield(tons)': ['mean', 'count']
}).round(2)
combinations.columns = ['Avg_Yield', 'Count']
combinations = combinations.sort_values('Avg_Yield', ascending=False)

print("\n Top 15 Best Performing Crop-Season Combinations:")
for idx, (combo, row) in enumerate(combinations.head(15).iterrows(), 1):
    crop, season = combo
    print(f"{idx:2d}. {crop:12s} ({season:7s}) | Avg Yield: {row['Avg_Yield']:6.2f} tons | Farms: {int(row['Count'])}")

# ============= COMBINATION ANALYSIS: IRRIGATION + SOIL =============
print("\n🔄 IRRIGATION × SOIL COMBINATION (Top 10)")
print("-" * 100)

irrig_soil = df.groupby(['Irrigation_Type', 'Soil_Type']).agg({
    'Yield(tons)': ['mean', 'count']
}).round(2)
irrig_soil.columns = ['Avg_Yield', 'Count']
irrig_soil = irrig_soil.sort_values('Avg_Yield', ascending=False)

print("\nTop 10 Best Performing Irrigation-Soil Combinations:")
for idx, (combo, row) in enumerate(irrig_soil.head(10).iterrows(), 1):
    irrig, soil = combo
    print(f"{idx:2d}. {irrig:12s} + {soil:10s} | Avg Yield: {row['Avg_Yield']:6.2f} tons | Farms: {int(row['Count'])}")

# ============= COMBINATION ANALYSIS: CROP + IRRIGATION =============
print("\n🔄 CROP × IRRIGATION COMBINATION (Top 10)")
print("-" * 100)

crop_irrig = df.groupby(['Crop_Type', 'Irrigation_Type']).agg({
    'Yield(tons)': ['mean', 'count']
}).round(2)
crop_irrig.columns = ['Avg_Yield', 'Count']
crop_irrig = crop_irrig.sort_values('Avg_Yield', ascending=False)

print("\nTop 10 Best Performing Crop-Irrigation Combinations:")
for idx, (combo, row) in enumerate(crop_irrig.head(10).iterrows(), 1):
    crop, irrig = combo
    print(f"{idx:2d}. {crop:12s} + {irrig:12s} | Avg Yield: {row['Avg_Yield']:6.2f} tons | Farms: {int(row['Count'])}")

print("\n" + "=" * 100)
print("✅ Category-based sorting analysis completed!")
print("=" * 100)
