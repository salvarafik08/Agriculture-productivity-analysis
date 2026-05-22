"""
🌾 AGRICULTURAL DATASET - BASIC SORTING EXAMPLES
Demonstrates fundamental sorting techniques with Pandas
"""

import pandas as pd
import numpy as np
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT_DIR / "data" / "raw" / "agriculture_dataset-95c6.csv"

# Load the dataset
df = pd.read_csv(DATA_FILE)

print("=" * 80)
print("🌾 AGRICULTURAL DATASET - BASIC SORTING EXAMPLES")
print("=" * 80)

# ============= EXAMPLE 1: Sort by Single Column =============
print("\n1️⃣  SORT BY SINGLE COLUMN - Yield (Descending)")
print("-" * 80)
sorted_by_yield = df.sort_values('Yield(tons)', ascending=False)
print(sorted_by_yield[['Farm_ID', 'Crop_Type', 'Yield(tons)']].head(10))

# ============= EXAMPLE 2: Sort by Multiple Columns =============
print("\n2️⃣  SORT BY MULTIPLE COLUMNS - Crop Type (Ascending), then Yield (Descending)")
print("-" * 80)
sorted_multi = df.sort_values(['Crop_Type', 'Yield(tons)'], 
                              ascending=[True, False])
print(sorted_multi[['Farm_ID', 'Crop_Type', 'Yield(tons)']].head(15))

# ============= EXAMPLE 3: Sort by Numeric Columns =============
print("\n3️⃣  SORT BY FARM AREA - Largest to Smallest")
print("-" * 80)
sorted_by_area = df.sort_values('Farm_Area(acres)', ascending=False)
print(sorted_by_area[['Farm_ID', 'Farm_Area(acres)', 'Yield(tons)']].head(10))

# ============= EXAMPLE 4: Sort by Water Usage =============
print("\n4️⃣  SORT BY WATER USAGE - Highest to Lowest")
print("-" * 80)
sorted_by_water = df.sort_values('Water_Usage(cubic meters)', ascending=False)
print(sorted_by_water[['Farm_ID', 'Water_Usage(cubic meters)', 'Yield(tons)']].head(10))

# ============= EXAMPLE 5: Sort by Fertilizer =============
print("\n5️⃣  SORT BY FERTILIZER USAGE")
print("-" * 80)
sorted_by_fert = df.sort_values('Fertilizer_Used(tons)', ascending=False)
print(sorted_by_fert[['Farm_ID', 'Fertilizer_Used(tons)', 'Yield(tons)']].head(10))

# ============= EXAMPLE 6: Sort by Season and Crop =============
print("\n6️⃣  SORT BY SEASON, THEN CROP TYPE")
print("-" * 80)
sorted_by_season = df.sort_values(['Season', 'Crop_Type'])
print(sorted_by_season[['Farm_ID', 'Season', 'Crop_Type', 'Yield(tons)']].head(15))

# ============= EXAMPLE 7: Sort by Irrigation Type =============
print("\n7️⃣  SORT BY IRRIGATION TYPE")
print("-" * 80)
sorted_by_irrig = df.sort_values('Irrigation_Type')
print(sorted_by_irrig[['Farm_ID', 'Irrigation_Type', 'Yield(tons)']].head(12))

# ============= EXAMPLE 8: Sort by Soil Type =============
print("\n8️⃣  SORT BY SOIL TYPE")
print("-" * 80)
sorted_by_soil = df.sort_values('Soil_Type')
print(sorted_by_soil[['Farm_ID', 'Soil_Type', 'Yield(tons)']].head(12))

# ============= EXAMPLE 9: Reverse Sort (Ascending) =============
print("\n9️⃣  SORT BY YIELD - ASCENDING (Lowest First)")
print("-" * 80)
sorted_ascending = df.sort_values('Yield(tons)', ascending=True)
print(sorted_ascending[['Farm_ID', 'Yield(tons)', 'Crop_Type']].head(10))

# ============= EXAMPLE 10: Custom Sort with Index Reset =============
print("\n🔟 SORT AND RESET INDEX")
print("-" * 80)
sorted_reset = df.sort_values('Yield(tons)', ascending=False).reset_index(drop=True)
sorted_reset.index = sorted_reset.index + 1  # Start index from 1
print(sorted_reset[['Farm_ID', 'Crop_Type', 'Yield(tons)']].head(10))

print("\n" + "=" * 80)
print("✅ Basic sorting examples completed!")
print("=" * 80)
