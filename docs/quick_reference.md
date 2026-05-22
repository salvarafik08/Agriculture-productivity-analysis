# 🌾 Python Sorting - Quick Reference Card

## ⚡ 30-Second Cheat Sheet

### Install
```bash
pip install pandas numpy openpyxl
```

### Load Data
```python
import pandas as pd
df = pd.read_csv('agriculture_dataset-95c6.csv')
```

---

## 🎯 One-Liners for Common Tasks

### Sorting
```python
df.sort_values('Yield(tons)', ascending=False)              # By yield
df.sort_values(['Crop_Type', 'Yield(tons)'], ascending=[True, False])  # Multi-column
df.nlargest(10, 'Yield(tons)')                              # Top 10
df.nsmallest(10, 'Yield(tons)')                             # Bottom 10
```

### Filtering
```python
df[df['Crop_Type'] == 'Rice']                               # By crop
df[df['Yield(tons)'] > 30]                                  # High yield
df[df['Yield(tons)'] > df['Yield(tons)'].mean()]            # Above average
df.query('`Yield(tons)` > 30 and `Season` == "Kharif"')   # Complex filter
```

### Calculations
```python
df['Efficiency'] = df['Yield(tons)'] / df['Fertilizer_Used(tons)']
df['Water_Efficiency'] = df['Yield(tons)'] / df['Water_Usage(cubic meters)']
df['Rank'] = df['Yield(tons)'].rank(ascending=False)
```

### Grouping & Stats
```python
df.groupby('Crop_Type')['Yield(tons)'].mean()              # Avg by crop
df.groupby('Season').agg({'Yield(tons)': ['mean', 'count']})  # Multi-stat
df.pivot_table(values='Yield(tons)', index='Crop_Type', columns='Season')  # Pivot
```

### Export
```python
df.to_csv('output.csv', index=False)                        # CSV
df.to_excel('output.xlsx')                                   # Excel
df.to_json('output.json', orient='records')                 # JSON
```

---

## 📊 Results Summary

| Metric | Value |
|--------|-------|
| **Total Records** | 50 farms |
| **Avg Yield** | 27.06 tons |
| **Best Crop** | Carrot (36.63 tons) |
| **Best Method** | Manual irrigation (34.16 tons) |
| **Best Soil** | Silty (30.89 tons) |

---

## 🚀 Run Scripts

```bash
python3 01_basic_sorting.py              # 10 basic examples
python3 02_advanced_sorting.py           # Advanced techniques
python3 03_sorting_by_category.py        # Category analysis
python3 04_sorting_with_export.py        # Export to files
python3 05_sorting_utilities.py          # Utility class demo
```

---

## 📁 Files Created

- ✅ 5 Python scripts (721 lines)
- ✅ 1 Comprehensive guide (14 KB)
- ✅ 15+ exported files (CSV, Excel, JSON)
- ✅ 50+ code examples

