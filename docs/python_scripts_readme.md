# 🌾 Python Sorting Scripts for Agricultural Dataset

## 📚 Complete Package Overview

This directory contains **5 production-ready Python scripts** with **721 lines of code** demonstrating comprehensive sorting, filtering, and analysis techniques for the agricultural dataset.

---

## 🎯 Quick Start

### Run All Scripts
```bash
cd scripts

# Run individual scripts
python 01_basic_sorting.py
python 02_advanced_sorting.py
python 03_sorting_by_category.py
python 04_sorting_with_export.py
python 05_sorting_utilities.py
```

### Install Dependencies
```bash
pip install -r ../requirements.txt
```

---

## 📁 Scripts Overview

### **1. 📊 01_basic_sorting.py** (80 lines)
**Basic sorting techniques with 10 examples**

```
✅ Sort by single column (yield, area, water, fertilizer)
✅ Sort by multiple columns with different order
✅ Sort by season and crop type
✅ Sort by irrigation and soil type
✅ Ascending and descending sorts
✅ Reset index after sorting
```

**Key Examples:**
```python
# Sort by yield (descending)
sorted_yield = df.sort_values('Yield(tons)', ascending=False)

# Sort by multiple columns
sorted_multi = df.sort_values(['Crop_Type', 'Yield(tons)'], 
                              ascending=[True, False])

# Top 10
print(sorted_yield.head(10))
```

**Run:** `python3 01_basic_sorting.py`

---

### **2. 🚀 02_advanced_sorting.py** (96 lines)
**Advanced sorting with ranking and filtering**

```
✅ Sort with conditional filtering
✅ Rank within groups (top 3 per crop)
✅ Percentile ranking (quartiles)
✅ Complex multi-criteria sorting
✅ Calculate efficiency rankings
✅ Water efficiency analysis
✅ Top performers by category
✅ Bottom performers identification
✅ Comprehensive ranking systems
```

**Key Examples:**
```python
# Top 3 farms per crop type
top_3_per_crop = df.sort_values(['Crop_Type', 'Yield(tons)'], 
                                ascending=[True, False])
top_3_per_crop['Rank'] = top_3_per_crop.groupby('Crop_Type').cumcount() + 1
top_3_per_crop = top_3_per_crop[top_3_per_crop['Rank'] <= 3]

# Efficiency ranking
df['Efficiency'] = (df['Yield(tons)'] / df['Fertilizer_Used(tons)']).round(2)
df_efficiency = df.sort_values('Efficiency', ascending=False)
```

**Run:** `python3 02_advanced_sorting.py`

---

### **3. 🗂️ 03_sorting_by_category.py** (132 lines)
**Category-based analysis and sorting**

```
✅ Crop type analysis (10 crops)
✅ Irrigation type sorting (5 types)
✅ Soil type analysis (5 types)
✅ Season performance ranking
✅ Crop × Season combinations
✅ Irrigation × Soil combinations
✅ Crop × Irrigation combinations
✅ Comparative statistics
```

**Key Examples:**
```python
# Crop-based sorting
for crop in sorted(df['Crop_Type'].unique()):
    crop_data = df[df['Crop_Type'] == crop].sort_values('Yield(tons)', ascending=False)
    print(f"{crop}: Avg Yield {crop_data['Yield(tons)'].mean():.2f} tons")

# Best crop-season combinations
combinations = df.groupby(['Crop_Type', 'Season']).agg({
    'Yield(tons)': ['mean', 'count']
}).round(2)
combinations = combinations.sort_values('Avg_Yield', ascending=False)
```

**Run:** `python3 03_sorting_by_category.py`

---

### **4. 💾 04_sorting_with_export.py** (224 lines)
**Sorting with export to multiple formats**

```
✅ Export sorted data to CSV
✅ Export to Excel (XLSX)
✅ Multi-sheet Excel exports
✅ Export to JSON format
✅ Individual CSVs per category
✅ Efficiency ranking export
✅ Crop summary statistics
✅ Pivot table export
✅ Bottom performers for improvement
✅ Comprehensive multi-sheet reports
```

**Output Files Created:**
```
sorted_data/
├── 01_sorted_by_yield_descending.csv
├── 02_sorted_by_fertilizer.xlsx
├── 03_water_usage_analysis.xlsx
├── 04_sorted_by_farm_area.json
├── crop_top10_*.csv (10 files)
├── 06_efficiency_ranking.xlsx
├── 07_crop_summary.xlsx
├── 08_season_irrigation_matrix.xlsx
├── 09_bottom_performers_improvement.xlsx
└── 10_comprehensive_report.xlsx (5 sheets)
```

**Key Examples:**
```python
# Export to Excel with statistics
with pd.ExcelWriter('output.xlsx') as writer:
    df.sort_values('Yield(tons)').to_excel(writer, sheet_name='Sorted')
    stats.to_excel(writer, sheet_name='Statistics')

# Export to JSON
json_data = df.sort_values('Yield(tons)', ascending=False).to_dict(orient='records')
with open('data.json', 'w') as f:
    json.dump(json_data, f, indent=2)
```

**Run:** `python3 04_sorting_with_export.py`

---

### **5. 🛠️ 05_sorting_utilities.py** (189 lines)
**Reusable utility class for sorting and analysis**

```
✅ Sort by yield
✅ Sort by specific crop
✅ Sort by season
✅ Sort by irrigation type
✅ Sort by soil type
✅ Efficiency ranking
✅ Water efficiency ranking
✅ Farm size sorting
✅ Top/bottom performers
✅ Above average filtering
✅ Rank within groups
✅ Category statistics
✅ Correlation analysis
✅ Summary reports
```

**Usage:**
```python
from sorting_utilities import AgriculturalSorter

# Initialize
sorter = AgriculturalSorter('agriculture_dataset-95c6.csv')

# Use methods
top_yield = sorter.sort_by_yield(top_n=10)
top_efficiency = sorter.sort_by_efficiency(top_n=10)
rice_farms = sorter.sort_by_crop('Rice')
stats = sorter.get_statistics_by_category('Crop_Type')
report = sorter.generate_summary_report()
```

**Run:** `python3 05_sorting_utilities.py`

---

## 📖 Comprehensive Guide

### **PYTHON_SORTING_GUIDE.md** (14 KB)

Complete reference documentation with:
- Quick start guide
- 50+ code examples
- Real-world use cases
- Performance tips
- Recipe reference table

**Topics Covered:**
- Basic sorting (5 examples)
- Advanced sorting (6 examples)
- Category-based sorting (6 examples)
- Export techniques (5 examples)
- Utility functions
- Real-world examples
- Performance optimization

---

## 📊 Dataset Statistics

### Quick Summary
```
Total Records: 50 farms
Unique Crops: 10 (Barley, Carrot, Cotton, Maize, Potato, Rice, Soybean, Sugarcane, Tomato, Wheat)
Unique Seasons: 3 (Kharif, Rabi, Zaid)
Unique Irrigation Types: 5 (Drip, Flood, Manual, Rain-fed, Sprinkler)
Unique Soil Types: 5 (Loamy, Clay, Sandy, Silty, Peaty)

Performance Metrics:
- Average Yield: 27.06 tons/farm
- Total Production: 1,353 tons
- Total Farm Area: 12,748 acres
- Average Farm Size: 254.96 acres
```

---

## 🎯 Top Results from Scripts

### Top 10 Farms by Yield
```
1. F028 (Tomato)    - 48.02 tons
2. F017 (Carrot)    - 47.70 tons
3. F033 (Barley)    - 46.47 tons
4. F040 (Cotton)    - 46.19 tons
5. F038 (Barley)    - 45.95 tons
6. F050 (Tomato)    - 45.14 tons
7. F007 (Soybean)   - 44.93 tons
8. F005 (Tomato)    - 43.28 tons
9. F002 (Carrot)    - 42.91 tons
10. F037 (Soybean)  - 40.15 tons
```

### Top Crops by Average Yield
```
1. Carrot:    36.63 tons avg
2. Tomato:    33.63 tons avg
3. Soybean:   32.31 tons avg
4. Sugarcane: 26.95 tons avg
5. Barley:    26.40 tons avg
```

### Top Irrigation Methods by Yield
```
1. Manual:      34.16 tons avg
2. Rain-fed:    31.98 tons avg
3. Sprinkler:   27.89 tons avg
4. Drip:        26.77 tons avg
5. Flood:       20.89 tons avg
```

### Best Soil Types
```
1. Silty:  30.89 tons avg
2. Loamy:  27.48 tons avg
3. Sandy:  27.03 tons avg
4. Clay:   25.04 tons avg
5. Peaty:  23.47 tons avg
```

---

## 💡 Common Use Cases

### Use Case 1: Find Top Performing Farms
```bash
python3 -c "
import pandas as pd
df = pd.read_csv('data/raw/agriculture_dataset-95c6.csv')
top_10 = df.nlargest(10, 'Yield(tons)')
print(top_10[['Farm_ID', 'Crop_Type', 'Yield(tons)']])
"
```

### Use Case 2: Compare Irrigation Methods
```bash
python3 -c "
import pandas as pd
df = pd.read_csv('data/raw/agriculture_dataset-95c6.csv')
by_irrigation = df.groupby('Irrigation_Type')['Yield(tons)'].agg(['mean', 'count'])
print(by_irrigation.sort_values('mean', ascending=False))
"
```

### Use Case 3: Efficiency Analysis
```bash
python3 -c "
import pandas as pd
df = pd.read_csv('data/raw/agriculture_dataset-95c6.csv')
df['Efficiency'] = (df['Yield(tons)'] / df['Fertilizer_Used(tons)']).round(2)
print(df.nlargest(10, 'Efficiency')[['Farm_ID', 'Crop_Type', 'Efficiency']])
"
```

### Use Case 4: Identify Improvement Opportunities
```bash
python3 -c "
import pandas as pd
df = pd.read_csv('data/raw/agriculture_dataset-95c6.csv')
bottom_10 = df.nsmallest(10, 'Yield(tons)')
print(bottom_10[['Farm_ID', 'Crop_Type', 'Yield(tons)', 'Irrigation_Type']])
"
```

---

## 📋 Complete Script Execution Flow

```
1. Run 01_basic_sorting.py
   ↓
   Output: 10 sorting techniques
   
2. Run 02_advanced_sorting.py
   ↓
   Output: Advanced rankings, percentiles, efficiency
   
3. Run 03_sorting_by_category.py
   ↓
   Output: Category analysis, combinations
   
4. Run 04_sorting_with_export.py
   ↓
   Output: 15+ exported files in sorted_data/
   
5. Run 05_sorting_utilities.py
   ↓
   Output: Reusable utility functions demo
```

---

## 🔄 Data Processing Pipeline

```
Raw CSV Data
    ↓
[Load with Pandas]
    ↓
[Clean & Validate]
    ↓
[Sort & Filter]
    ↓
[Calculate Metrics]
    ↓
[Export Results]
    ↓
Output: CSV, Excel, JSON
```

---

## 📊 Export Locations

All sorted data exported to: `outputs/sorted_data/`

```
sorted_data/
├── CSV Files (4)
├── Excel Files (7)
├── JSON File (1)
└── Individual Crop CSVs (10)
```

---

## ✨ Key Features

### Data Sorting
- ✅ Single & multi-column sorting
- ✅ Ascending & descending order
- ✅ Complex multi-criteria sorts
- ✅ Custom ranking systems

### Filtering
- ✅ Category-based filtering
- ✅ Conditional filtering
- ✅ Top/bottom N selection
- ✅ Above/below average filtering

### Analysis
- ✅ Efficiency calculations
- ✅ Category statistics
- ✅ Group-based ranking
- ✅ Percentile analysis

### Export
- ✅ CSV export
- ✅ Excel export (single & multi-sheet)
- ✅ JSON export
- ✅ Individual category exports

---

## 🚀 Next Steps

1. **Run Scripts** - Execute each Python script to see examples
2. **Read Guide** - Study PYTHON_SORTING_GUIDE.md for detailed explanations
3. **Modify Code** - Adapt scripts for your specific needs
4. **Export Data** - Use export functions to save sorted datasets
5. **Integrate** - Use sorted data in Power BI or other tools

---

## 📞 Support

**Question?** Check:
- PYTHON_SORTING_GUIDE.md for detailed examples
- Individual script comments
- Output from running the scripts

**Need Help?** Each script includes:
- Comments explaining code
- Print statements showing results
- Example usage patterns

---

## 📈 Performance Metrics

**Total Code:** 721 lines
**Number of Scripts:** 5
**Number of Examples:** 50+
**Export Formats:** 3 (CSV, Excel, JSON)
**Sorting Techniques:** 15+
**Use Cases:** 10+

---

**Happy Sorting! 🌾**

*Created: May 21, 2026*
*Dataset: 50 Farms | 10 Crops | 3 Seasons | 5 Irrigation Types | 5 Soil Types*
