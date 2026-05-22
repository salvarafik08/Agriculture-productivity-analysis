# 🌾 Python Sorting Guide for Agricultural Dataset

## 📚 Complete Python Sorting Reference & Examples

---

## 📑 Table of Contents

1. [Quick Start](#quick-start)
2. [Basic Sorting](#basic-sorting)
3. [Advanced Sorting](#advanced-sorting)
4. [Category-Based Sorting](#category-based-sorting)
5. [Sorting with Export](#sorting-with-export)
6. [Utility Functions](#utility-functions)
7. [Real-World Examples](#real-world-examples)
8. [Performance Tips](#performance-tips)

---

## 🚀 Quick Start

### Installation
```bash
pip install pandas numpy openpyxl
```

### Basic Usage
```python
import pandas as pd

# Load dataset
df = pd.read_csv('agriculture_dataset-95c6.csv')

# Sort by yield (highest first)
sorted_df = df.sort_values('Yield(tons)', ascending=False)

# Display top 10
print(sorted_df[['Farm_ID', 'Crop_Type', 'Yield(tons)']].head(10))
```

---

## 📊 Basic Sorting

### 1. Sort by Single Column (Descending)
```python
# Highest yield first
sorted_yield = df.sort_values('Yield(tons)', ascending=False)
print(sorted_yield[['Farm_ID', 'Crop_Type', 'Yield(tons)']].head(10))

# OUTPUT:
#    Farm_ID Crop_Type  Yield(tons)
# 27    F028    Tomato        48.02
# 16    F017    Carrot        47.70
# 32    F033    Barley        46.47
```

### 2. Sort by Single Column (Ascending)
```python
# Lowest yield first
sorted_ascending = df.sort_values('Yield(tons)', ascending=True)
print(sorted_ascending.head(5))
```

### 3. Sort by Farm Area
```python
sorted_area = df.sort_values('Farm_Area(acres)', ascending=False)
print(sorted_area[['Farm_ID', 'Farm_Area(acres)', 'Yield(tons)']].head())
```

### 4. Sort by Water Usage
```python
sorted_water = df.sort_values('Water_Usage(cubic meters)', ascending=False)
print(sorted_water[['Farm_ID', 'Water_Usage(cubic meters)', 'Yield(tons)']].head())
```

### 5. Sort by Fertilizer Usage
```python
sorted_fert = df.sort_values('Fertilizer_Used(tons)', ascending=False)
print(sorted_fert[['Farm_ID', 'Fertilizer_Used(tons)', 'Yield(tons)']].head())
```

---

## 🎯 Advanced Sorting

### 1. Sort by Multiple Columns
```python
# Primary: Crop Type (A-Z)
# Secondary: Yield (High to Low)
sorted_multi = df.sort_values(
    ['Crop_Type', 'Yield(tons)'],
    ascending=[True, False]
)
```

### 2. Sort with Different Order for Each Column
```python
# Season ascending, Yield descending, Area descending
sorted_complex = df.sort_values(
    ['Season', 'Yield(tons)', 'Farm_Area(acres)'],
    ascending=[True, False, False]
)
```

### 3. Calculate Efficiency and Sort
```python
# Calculate efficiency ratio
df['Efficiency'] = (df['Yield(tons)'] / df['Fertilizer_Used(tons)']).round(2)

# Sort by efficiency
top_efficient = df.sort_values('Efficiency', ascending=False)
print(top_efficient[['Farm_ID', 'Crop_Type', 'Efficiency']].head(10))

# OUTPUT:
# Farm_ID  Crop_Type  Efficiency
# F027     Cotton          45.02
# F019     Maize           36.66
# F037     Soybean         34.03
```

### 4. Water Efficiency Ranking
```python
# Water efficiency (yield per water unit)
df['Water_Efficiency'] = (df['Yield(tons)'] / df['Water_Usage(cubic meters)']).round(6)

# Top performers
top_water = df.sort_values('Water_Efficiency', ascending=False)
print(top_water[['Farm_ID', 'Water_Efficiency']].head())
```

### 5. Top Performers Within Groups
```python
# Top 3 farms per crop type
top_3_per_crop = df.sort_values(['Crop_Type', 'Yield(tons)'], ascending=[True, False])
top_3_per_crop['Rank'] = top_3_per_crop.groupby('Crop_Type').cumcount() + 1
top_3_per_crop = top_3_per_crop[top_3_per_crop['Rank'] <= 3]
```

### 6. Percentile Ranking
```python
# Create percentile buckets
df['Yield_Percentile'] = pd.qcut(df['Yield(tons)'], q=4, 
                                  labels=['Low', 'Medium-Low', 'Medium-High', 'High'])

sorted_percentile = df.sort_values('Yield(tons)', ascending=False)
print(sorted_percentile[['Farm_ID', 'Yield(tons)', 'Yield_Percentile']].head(15))
```

---

## 🗂️ Category-Based Sorting

### 1. Sort by Crop Type
```python
for crop in sorted(df['Crop_Type'].unique()):
    crop_data = df[df['Crop_Type'] == crop].sort_values('Yield(tons)', ascending=False)
    print(f"\n{crop}:")
    print(f"  Average Yield: {crop_data['Yield(tons)'].mean():.2f} tons")
    print(f"  Top Farm: {crop_data.iloc[0]['Farm_ID']}")
```

### 2. Sort by Irrigation Type
```python
for irrig in sorted(df['Irrigation_Type'].unique()):
    irrig_data = df[df['Irrigation_Type'] == irrig].sort_values('Yield(tons)', ascending=False)
    avg_yield = irrig_data['Yield(tons)'].mean()
    print(f"{irrig:12s} | Avg Yield: {avg_yield:6.2f} tons | Farms: {len(irrig_data)}")
```

### 3. Sort by Soil Type
```python
for soil in sorted(df['Soil_Type'].unique()):
    soil_data = df[df['Soil_Type'] == soil].sort_values('Yield(tons)', ascending=False)
    avg_yield = soil_data['Yield(tons)'].mean()
    print(f"{soil:10s} | Avg Yield: {avg_yield:6.2f} tons | Best: {soil_data.iloc[0]['Farm_ID']}")
```

### 4. Sort by Season
```python
for season in sorted(df['Season'].unique()):
    season_data = df[df['Season'] == season].sort_values('Yield(tons)', ascending=False)
    avg_yield = season_data['Yield(tons)'].mean()
    print(f"{season}: Avg Yield {avg_yield:.2f} tons ({len(season_data)} farms)")
```

### 5. Combination Analysis: Crop × Season
```python
# Best performing crop-season combinations
combinations = df.groupby(['Crop_Type', 'Season'])['Yield(tons)'].agg(['mean', 'count']).round(2)
combinations = combinations.sort_values('mean', ascending=False)

for idx, (combo, row) in enumerate(combinations.head(10).iterrows(), 1):
    crop, season = combo
    print(f"{idx}. {crop:12s} ({season:7s}) | Avg: {row['mean']:6.2f} tons | Farms: {int(row['count'])}")
```

### 6. Combination Analysis: Irrigation × Soil
```python
# Best irrigation-soil combinations
irrig_soil = df.groupby(['Irrigation_Type', 'Soil_Type'])['Yield(tons)'].agg(['mean', 'count']).round(2)
irrig_soil = irrig_soil.sort_values('mean', ascending=False)

for combo, row in irrig_soil.head(10).iterrows():
    irrig, soil = combo
    print(f"{irrig:12s} + {soil:10s} | Avg: {row['mean']:6.2f} tons | Count: {int(row['count'])}")
```

---

## 💾 Sorting with Export

### 1. Export to CSV
```python
# Sort and export
sorted_df = df.sort_values('Yield(tons)', ascending=False)
sorted_df.to_csv('sorted_by_yield.csv', index=False)
```

### 2. Export to Excel
```python
sorted_df = df.sort_values('Fertilizer_Used(tons)', ascending=False)
sorted_df.to_excel('sorted_by_fertilizer.xlsx')
```

### 3. Multi-Sheet Excel Export
```python
with pd.ExcelWriter('agricultural_analysis.xlsx') as writer:
    # Sheet 1: Sorted by yield
    df.sort_values('Yield(tons)', ascending=False).to_excel(writer, sheet_name='Yield')
    
    # Sheet 2: Sorted by area
    df.sort_values('Farm_Area(acres)', ascending=False).to_excel(writer, sheet_name='Area')
    
    # Sheet 3: Statistics
    stats = df.groupby('Crop_Type')['Yield(tons)'].agg(['mean', 'count'])
    stats.to_excel(writer, sheet_name='Crop Stats')
```

### 4. Export to JSON
```python
import json

sorted_df = df.sort_values('Yield(tons)', ascending=False)
json_data = sorted_df.to_dict(orient='records')

with open('sorted_data.json', 'w') as f:
    json.dump(json_data, f, indent=2)
```

### 5. Export Individual CSVs by Category
```python
# Top 10 farms per crop type
for crop in df['Crop_Type'].unique():
    crop_data = df[df['Crop_Type'] == crop].nlargest(10, 'Yield(tons)')
    crop_data.to_csv(f'crop_top10_{crop.lower()}.csv', index=False)
```

---

## 🛠️ Utility Functions

### Create Reusable Sorting Class
```python
class AgriculturalSorter:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
    
    def sort_by_yield(self, ascending=False, top_n=None):
        """Sort by yield"""
        result = self.df.sort_values('Yield(tons)', ascending=ascending)
        return result.head(top_n) if top_n else result
    
    def sort_by_crop(self, crop_name):
        """Get records for specific crop"""
        return self.df[self.df['Crop_Type'] == crop_name].sort_values('Yield(tons)', ascending=False)
    
    def sort_by_efficiency(self, top_n=10):
        """Sort by efficiency ratio"""
        df_eff = self.df.copy()
        df_eff['Efficiency'] = (df_eff['Yield(tons)'] / df_eff['Fertilizer_Used(tons)']).round(2)
        return df_eff.nlargest(top_n, 'Efficiency')[['Farm_ID', 'Crop_Type', 'Efficiency']]
    
    def get_top_performers(self, metric='Yield(tons)', n=10):
        """Get top N by metric"""
        return self.df.nlargest(n, metric)
    
    def get_statistics_by_category(self, category):
        """Get statistics grouped by category"""
        return self.df.groupby(category).agg({
            'Yield(tons)': ['mean', 'sum', 'count', 'max', 'min'],
            'Farm_Area(acres)': 'mean',
            'Fertilizer_Used(tons)': 'mean'
        }).round(2)

# Usage
sorter = AgriculturalSorter('agriculture_dataset-95c6.csv')
top_10 = sorter.sort_by_yield(top_n=10)
efficiency = sorter.sort_by_efficiency(top_n=15)
```

---

## 💡 Real-World Examples

### Example 1: Find Best Performing Farm
```python
best_farm = df.loc[df['Yield(tons)'].idxmax()]
print(f"Best Farm: {best_farm['Farm_ID']}")
print(f"Crop: {best_farm['Crop_Type']}")
print(f"Yield: {best_farm['Yield(tons)']:.2f} tons")
print(f"Season: {best_farm['Season']}")
print(f"Irrigation: {best_farm['Irrigation_Type']}")
```

### Example 2: Compare Top vs Bottom Performers
```python
top_5 = df.nlargest(5, 'Yield(tons)')
bottom_5 = df.nsmallest(5, 'Yield(tons)')

print("Top 5 Performers:")
print(top_5[['Farm_ID', 'Crop_Type', 'Yield(tons)']].to_string())

print("\nBottom 5 Performers:")
print(bottom_5[['Farm_ID', 'Crop_Type', 'Yield(tons)']].to_string())
```

### Example 3: Identify Efficiency Leaders
```python
df['Efficiency'] = (df['Yield(tons)'] / df['Fertilizer_Used(tons)']).round(2)
df['Water_Efficiency'] = (df['Yield(tons)'] / df['Water_Usage(cubic meters)']).round(6)

efficiency_leaders = df.sort_values('Efficiency', ascending=False).head(5)
print("\nEfficiency Leaders (High Yield per Fertilizer):")
print(efficiency_leaders[['Farm_ID', 'Crop_Type', 'Efficiency']].to_string())
```

### Example 4: Create Ranking System
```python
df_rank = df.copy()
df_rank['Yield_Rank'] = df_rank['Yield(tons)'].rank(ascending=False)
df_rank['Area_Rank'] = df_rank['Farm_Area(acres)'].rank(ascending=False)
df_rank['Efficiency'] = (df_rank['Yield(tons)'] / df_rank['Fertilizer_Used(tons)']).round(2)
df_rank['Efficiency_Rank'] = df_rank['Efficiency'].rank(ascending=False)
df_rank['Overall_Score'] = (df_rank['Yield_Rank'] + df_rank['Efficiency_Rank']) / 2

top_overall = df_rank.nsmallest(10, 'Overall_Score')
print(top_overall[['Farm_ID', 'Yield_Rank', 'Efficiency_Rank', 'Overall_Score']].to_string())
```

### Example 5: Performance Analysis by Crop
```python
print("Performance Analysis by Crop:\n")
for crop in sorted(df['Crop_Type'].unique()):
    crop_df = df[df['Crop_Type'] == crop]
    print(f"\n🌾 {crop.upper()}")
    print(f"  Total Farms: {len(crop_df)}")
    print(f"  Avg Yield: {crop_df['Yield(tons)'].mean():.2f} tons")
    print(f"  Max Yield: {crop_df['Yield(tons)'].max():.2f} tons")
    print(f"  Min Yield: {crop_df['Yield(tons)'].min():.2f} tons")
    print(f"  Top Farm: {crop_df.loc[crop_df['Yield(tons)'].idxmax(), 'Farm_ID']}")
```

---

## ⚡ Performance Tips

### 1. Use nlargest/nsmallest for Top/Bottom N
```python
# Fast: Gets top 10 without sorting entire dataset
top_10 = df.nlargest(10, 'Yield(tons)')

# Slower: Sorts entire dataset then slices
top_10_slow = df.sort_values('Yield(tons)', ascending=False).head(10)
```

### 2. Use Query for Complex Filters
```python
# Efficient
high_yield_large_farms = df.query('`Yield(tons)` > 30 and `Farm_Area(acres)` > 300')

# Less efficient
high_yield_large_farms = df[(df['Yield(tons)'] > 30) & (df['Farm_Area(acres)'] > 300)]
```

### 3. Avoid Copying When Unnecessary
```python
# Good - no copy
sorted_df = df.sort_values('Yield(tons)')

# Unnecessary copy
sorted_df = df.copy().sort_values('Yield(tons)')
```

### 4. Use Vectorized Operations
```python
# Vectorized (fast)
df['Efficiency'] = df['Yield(tons)'] / df['Fertilizer_Used(tons)']

# Loop (slow - avoid!)
for idx in range(len(df)):
    df.loc[idx, 'Efficiency'] = df.loc[idx, 'Yield(tons)'] / df.loc[idx, 'Fertilizer_Used(tons)']
```

### 5. Use inplace=True When Not Needed
```python
# Good for memory
df.sort_values('Yield(tons)', inplace=True)

# Creates copy in memory
sorted_df = df.sort_values('Yield(tons)')
```

---

## 📋 Common Sorting Recipes

| Task | Code |
|------|------|
| **Top 10 by Yield** | `df.nlargest(10, 'Yield(tons)')` |
| **Bottom 5 by Yield** | `df.nsmallest(5, 'Yield(tons)')` |
| **Sort A-Z by Crop** | `df.sort_values('Crop_Type')` |
| **Sort Z-A by Crop** | `df.sort_values('Crop_Type', ascending=False)` |
| **Multi-column Sort** | `df.sort_values(['Crop_Type', 'Yield(tons)'], ascending=[True, False])` |
| **Get Above Average** | `df[df['Yield(tons)'] > df['Yield(tons)'].mean()]` |
| **Get Below Average** | `df[df['Yield(tons)'] < df['Yield(tons)'].mean()]` |
| **Group and Sort** | `df.groupby('Crop_Type').apply(lambda x: x.nlargest(1, 'Yield(tons)'))` |
| **Rank within Groups** | `df.groupby('Crop_Type').rank(ascending=False)` |
| **Reset Index** | `df.sort_values('Yield(tons)').reset_index(drop=True)` |

---

## 🎓 Next Steps

1. **Run the scripts**: Execute the Python files in `scripts/`
2. **Modify for your needs**: Adapt the code to your specific requirements
3. **Export your results**: Use the export functions to save sorted data
4. **Automate**: Create scheduled sorting reports
5. **Integrate**: Use sorted data in Power BI or other dashboards

---

## 📞 Script Files Reference

| File | Purpose |
|------|---------|
| `01_basic_sorting.py` | 10 basic sorting examples |
| `02_advanced_sorting.py` | 10 advanced sorting techniques |
| `03_sorting_by_category.py` | Category-based analysis |
| `04_sorting_with_export.py` | Export to CSV, Excel, JSON |
| `05_sorting_utilities.py` | Reusable utility class |

---

**Happy Sorting! 🌾**
