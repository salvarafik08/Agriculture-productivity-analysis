"""
🌾 AGRICULTURAL DATASET - SORTING UTILITY FUNCTIONS
Reusable functions for sorting, filtering, and analyzing
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import List, Dict, Tuple

class AgriculturalSorter:
    """
    Utility class for sorting and analyzing agricultural data
    """
    
    def __init__(self, csv_path: str):
        """Initialize with CSV file path"""
        self.df = pd.read_csv(Path(csv_path))
        print(f"✅ Loaded {len(self.df)} records from {csv_path}")
    
    # ============= BASIC SORTING METHODS =============
    
    def sort_by_yield(self, ascending: bool = False, top_n: int = None) -> pd.DataFrame:
        """Sort by yield (descending by default)"""
        result = self.df.sort_values('Yield(tons)', ascending=ascending)
        if top_n:
            result = result.head(top_n)
        return result
    
    def sort_by_crop(self, crop_name: str) -> pd.DataFrame:
        """Get all records for a specific crop, sorted by yield"""
        return self.df[self.df['Crop_Type'] == crop_name].sort_values('Yield(tons)', ascending=False)
    
    def sort_by_season(self, season: str) -> pd.DataFrame:
        """Get all records for a specific season, sorted by yield"""
        return self.df[self.df['Season'] == season].sort_values('Yield(tons)', ascending=False)
    
    def sort_by_irrigation(self, irrig_type: str) -> pd.DataFrame:
        """Get all records for a specific irrigation type"""
        return self.df[self.df['Irrigation_Type'] == irrig_type].sort_values('Yield(tons)', ascending=False)
    
    def sort_by_soil(self, soil_type: str) -> pd.DataFrame:
        """Get all records for a specific soil type"""
        return self.df[self.df['Soil_Type'] == soil_type].sort_values('Yield(tons)', ascending=False)
    
    # ============= ADVANCED SORTING METHODS =============
    
    def sort_by_efficiency(self, top_n: int = 10) -> pd.DataFrame:
        """Sort by yield-to-fertilizer efficiency ratio"""
        df_eff = self.df.copy()
        df_eff['Efficiency'] = (df_eff['Yield(tons)'] / df_eff['Fertilizer_Used(tons)']).round(2)
        result = df_eff.sort_values('Efficiency', ascending=False)
        if top_n:
            result = result.head(top_n)
        return result[['Farm_ID', 'Crop_Type', 'Yield(tons)', 'Fertilizer_Used(tons)', 'Efficiency']]
    
    def sort_by_water_efficiency(self, top_n: int = 10) -> pd.DataFrame:
        """Sort by water efficiency (yield per water unit)"""
        df_water = self.df.copy()
        df_water['Water_Efficiency'] = (df_water['Yield(tons)'] / df_water['Water_Usage(cubic meters)']).round(6)
        result = df_water.sort_values('Water_Efficiency', ascending=False)
        if top_n:
            result = result.head(top_n)
        return result[['Farm_ID', 'Crop_Type', 'Yield(tons)', 'Water_Usage(cubic meters)', 'Water_Efficiency']]
    
    def sort_by_farm_size(self, top_n: int = 10) -> pd.DataFrame:
        """Sort by farm area"""
        return self.df.nlargest(top_n, 'Farm_Area(acres)')[['Farm_ID', 'Farm_Area(acres)', 'Crop_Type', 'Yield(tons)']]
    
    # ============= FILTERING & RANKING METHODS =============
    
    def get_top_performers(self, metric: str = 'Yield(tons)', n: int = 10) -> pd.DataFrame:
        """Get top N performers by specified metric"""
        return self.df.nlargest(n, metric)
    
    def get_bottom_performers(self, metric: str = 'Yield(tons)', n: int = 10) -> pd.DataFrame:
        """Get bottom N performers by specified metric"""
        return self.df.nsmallest(n, metric)
    
    def get_above_average(self, metric: str = 'Yield(tons)') -> pd.DataFrame:
        """Get records above average for a metric"""
        avg = self.df[metric].mean()
        return self.df[self.df[metric] > avg].sort_values(metric, ascending=False)
    
    def rank_within_group(self, group_by: str, rank_by: str = 'Yield(tons)', top_n: int = 3) -> pd.DataFrame:
        """Rank records within groups (e.g., top 3 crops per season)"""
        df_ranked = self.df.copy()
        df_ranked['Rank'] = df_ranked.groupby(group_by)[rank_by].rank(ascending=False, method='min').astype(int)
        result = df_ranked[df_ranked['Rank'] <= top_n]
        return result.sort_values([group_by, 'Rank'])[['Farm_ID', group_by, rank_by, 'Rank']]
    
    # ============= STATISTICAL METHODS =============
    
    def get_statistics_by_category(self, category: str) -> pd.DataFrame:
        """Get statistics grouped by category"""
        return self.df.groupby(category).agg({
            'Yield(tons)': ['mean', 'sum', 'count', 'max', 'min'],
            'Farm_Area(acres)': 'mean',
            'Fertilizer_Used(tons)': 'mean',
            'Water_Usage(cubic meters)': 'mean'
        }).round(2)
    
    def get_correlation_analysis(self) -> pd.DataFrame:
        """Get correlation between numeric columns"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        return self.df[numeric_cols].corr().round(3)
    
    # ============= REPORTING METHODS =============
    
    def generate_summary_report(self) -> Dict:
        """Generate comprehensive summary report"""
        return {
            'total_records': len(self.df),
            'unique_crops': self.df['Crop_Type'].nunique(),
            'unique_seasons': self.df['Season'].nunique(),
            'unique_irrigations': self.df['Irrigation_Type'].nunique(),
            'unique_soils': self.df['Soil_Type'].nunique(),
            'avg_yield': round(self.df['Yield(tons)'].mean(), 2),
            'max_yield': round(self.df['Yield(tons)'].max(), 2),
            'min_yield': round(self.df['Yield(tons)'].min(), 2),
            'total_yield': round(self.df['Yield(tons)'].sum(), 2),
            'avg_farm_area': round(self.df['Farm_Area(acres)'].mean(), 2),
            'total_farm_area': round(self.df['Farm_Area(acres)'].sum(), 2),
            'avg_fertilizer': round(self.df['Fertilizer_Used(tons)'].mean(), 2),
            'total_water_usage': round(self.df['Water_Usage(cubic meters)'].sum(), 0)
        }


# ============= DEMO USAGE =============
if __name__ == "__main__":
    print("=" * 100)
    print("🌾 AGRICULTURAL DATASET - SORTING UTILITY DEMO")
    print("=" * 100)
    
    # Initialize sorter
    ROOT_DIR = Path(__file__).resolve().parents[1]
    DATA_FILE = ROOT_DIR / "data" / "raw" / "agriculture_dataset-95c6.csv"
    sorter = AgriculturalSorter(DATA_FILE)
    
    # Test 1: Sort by yield
    print("\n1️⃣  TOP 10 FARMS BY YIELD")
    print("-" * 100)
    top_yield = sorter.sort_by_yield(top_n=10)
    print(top_yield[['Farm_ID', 'Crop_Type', 'Yield(tons)']].to_string())
    
    # Test 2: Sort by efficiency
    print("\n2️⃣  TOP 10 FARMS BY EFFICIENCY (Yield/Fertilizer)")
    print("-" * 100)
    top_eff = sorter.sort_by_efficiency(top_n=10)
    print(top_eff.to_string())
    
    # Test 3: Sort by water efficiency
    print("\n3️⃣  TOP 10 FARMS BY WATER EFFICIENCY")
    print("-" * 100)
    top_water = sorter.sort_by_water_efficiency(top_n=10)
    print(top_water.to_string())
    
    # Test 4: Specific crop analysis
    print("\n4️⃣  RICE FARMS SORTED BY YIELD")
    print("-" * 100)
    rice_farms = sorter.sort_by_crop('Rice')
    print(rice_farms[['Farm_ID', 'Season', 'Yield(tons)', 'Irrigation_Type']].to_string())
    
    # Test 5: Statistics by category
    print("\n5️⃣  STATISTICS BY CROP TYPE")
    print("-" * 100)
    crop_stats = sorter.get_statistics_by_category('Crop_Type')
    print(crop_stats)
    
    # Test 6: Above average performance
    print("\n6️⃣  ABOVE AVERAGE YIELD FARMS")
    print("-" * 100)
    above_avg = sorter.get_above_average('Yield(tons)')
    print(f"Found {len(above_avg)} farms above average yield")
    print(above_avg[['Farm_ID', 'Crop_Type', 'Yield(tons)']].head(10).to_string())
    
    # Test 7: Top performers by category
    print("\n7️⃣  TOP 3 CROPS PER SEASON")
    print("-" * 100)
    top_3 = sorter.rank_within_group('Season', 'Yield(tons)', top_n=3)
    print(top_3.to_string())
    
    # Test 8: Summary report
    print("\n8️⃣  SUMMARY REPORT")
    print("-" * 100)
    report = sorter.generate_summary_report()
    for key, value in report.items():
        print(f"{key:25s}: {value}")
    
    print("\n" + "=" * 100)
    print("✅ Sorting utility demo completed!")
    print("=" * 100)
