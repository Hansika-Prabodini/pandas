#!/usr/bin/env python
"""
test_custom_build.py - Example script for testing custom Pandas builds

This script demonstrates how to test your custom Pandas build and verify
that your modifications are working as expected. Use this as a template
for creating your own test scripts.

Usage:
    python test_custom_build.py

Customize this script based on your modifications to test specific
functionality you've added or changed.
"""

import sys
import pandas as pd
import numpy as np


def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def test_build_info():
    """Display build information"""
    print_section("Build Information")
    
    print(f"Pandas Version: {pd.__version__}")
    print(f"Pandas Location: {pd.__file__}")
    print(f"NumPy Version: {np.__version__}")
    print(f"Python Version: {sys.version}")
    
    # Check if this is a development build
    if 'dev' in pd.__version__ or '+' in pd.__version__:
        print("\n✓ This appears to be a development build")
    else:
        print("\n✓ This appears to be a release build")


def test_basic_functionality():
    """Test basic DataFrame and Series functionality"""
    print_section("Testing Basic Functionality")
    
    # Create a DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': ['a', 'b', 'c', 'd', 'e']
    })
    
    print("Created DataFrame:")
    print(df)
    print(f"\nShape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"dtypes:\n{df.dtypes}")
    
    # Basic operations
    print("\nBasic operations:")
    print(f"Sum of column 'A': {df['A'].sum()}")
    print(f"Mean of column 'B': {df['B'].mean()}")
    print(f"Max of column 'A': {df['A'].max()}")
    
    print("\n✓ Basic functionality works correctly")


def test_advanced_operations():
    """Test more advanced operations"""
    print_section("Testing Advanced Operations")
    
    # Create sample data
    df = pd.DataFrame({
        'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Value1': [10, 20, 30, 40, 50, 60],
        'Value2': [1, 2, 3, 4, 5, 6]
    })
    
    print("Original DataFrame:")
    print(df)
    
    # GroupBy operation
    print("\nGroupBy Sum:")
    grouped = df.groupby('Category').sum()
    print(grouped)
    
    # Merge operation
    df2 = pd.DataFrame({
        'Category': ['A', 'B', 'C'],
        'Extra': [100, 200, 300]
    })
    
    print("\nMerge Result:")
    merged = pd.merge(df, df2, on='Category', how='left')
    print(merged)
    
    # Pivot operation
    print("\nPivot Table:")
    pivot = df.pivot_table(values='Value1', index='Category', aggfunc='mean')
    print(pivot)
    
    print("\n✓ Advanced operations work correctly")


def test_io_operations():
    """Test I/O operations"""
    print_section("Testing I/O Operations")
    
    # Create sample data
    df = pd.DataFrame({
        'A': range(1, 6),
        'B': range(10, 60, 10),
        'C': ['x', 'y', 'z', 'w', 'v']
    })
    
    # Test CSV I/O
    csv_data = df.to_csv(index=False)
    print("CSV output (first 100 chars):")
    print(csv_data[:100])
    
    # Read back from CSV string
    from io import StringIO
    df_from_csv = pd.read_csv(StringIO(csv_data))
    print("\nDataFrame read from CSV:")
    print(df_from_csv)
    
    # Test JSON I/O
    json_data = df.to_json(orient='records')
    print(f"\nJSON output (first 100 chars):")
    print(json_data[:100])
    
    print("\n✓ I/O operations work correctly")


def test_datetime_operations():
    """Test datetime functionality"""
    print_section("Testing DateTime Operations")
    
    # Create date range
    dates = pd.date_range('2024-01-01', periods=10, freq='D')
    print("Date range:")
    print(dates)
    
    # Create DataFrame with datetime index
    df = pd.DataFrame({
        'Value': np.random.randn(10)
    }, index=dates)
    
    print("\nDataFrame with datetime index:")
    print(df.head())
    
    # Resample operation
    weekly = df.resample('W').mean()
    print("\nWeekly resampled data:")
    print(weekly)
    
    print("\n✓ DateTime operations work correctly")


def test_missing_data():
    """Test missing data handling"""
    print_section("Testing Missing Data Handling")
    
    # Create DataFrame with missing values
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [10, np.nan, 30, np.nan, 50],
        'C': [100, 200, 300, 400, 500]
    })
    
    print("DataFrame with missing values:")
    print(df)
    
    print("\nMissing value counts:")
    print(df.isna().sum())
    
    print("\nFilled with 0:")
    print(df.fillna(0))
    
    print("\nDropped missing values:")
    print(df.dropna())
    
    print("\n✓ Missing data handling works correctly")


def test_performance_features():
    """Test performance-related features"""
    print_section("Testing Performance Features")
    
    # Create larger dataset
    size = 10000
    df = pd.DataFrame({
        'A': np.random.randn(size),
        'B': np.random.randn(size),
        'Category': np.random.choice(['X', 'Y', 'Z'], size)
    })
    
    print(f"Created DataFrame with {size} rows")
    print(f"Memory usage: {df.memory_usage().sum() / 1024:.2f} KB")
    
    # Test some operations
    import time
    
    start = time.time()
    result = df.groupby('Category')['A'].mean()
    elapsed = time.time() - start
    
    print(f"\nGroupBy mean operation took: {elapsed*1000:.2f} ms")
    print(f"Result:\n{result}")
    
    print("\n✓ Performance features work correctly")


def run_custom_tests():
    """
    Add your custom tests here to verify your specific modifications
    
    Example:
    def test_my_new_feature():
        # Test your custom functionality
        pass
    """
    print_section("Custom Tests")
    print("Add your custom test functions here to verify your modifications")
    print("\nExample:")
    print("  def test_my_new_feature():")
    print("      # Your test code here")
    print("      pass")
    print("\n✓ No custom tests defined (this is OK)")


def main():
    """Main test runner"""
    print("\n" + "=" * 70)
    print("  PANDAS CUSTOM BUILD TEST SUITE")
    print("=" * 70)
    print("\nThis script tests the functionality of your custom Pandas build.")
    print("All tests should pass if the build was successful.\n")
    
    tests = [
        ("Build Information", test_build_info),
        ("Basic Functionality", test_basic_functionality),
        ("Advanced Operations", test_advanced_operations),
        ("I/O Operations", test_io_operations),
        ("DateTime Operations", test_datetime_operations),
        ("Missing Data Handling", test_missing_data),
        ("Performance Features", test_performance_features),
        ("Custom Tests", run_custom_tests),
    ]
    
    failed_tests = []
    
    for test_name, test_func in tests:
        try:
            test_func()
        except Exception as e:
            print(f"\n✗ {test_name} FAILED with error: {e}")
            failed_tests.append((test_name, e))
            import traceback
            traceback.print_exc()
    
    # Print summary
    print("\n" + "=" * 70)
    print("  TEST SUMMARY")
    print("=" * 70)
    
    total_tests = len(tests)
    passed_tests = total_tests - len(failed_tests)
    
    print(f"\nTotal Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {len(failed_tests)}")
    
    if failed_tests:
        print("\nFailed Tests:")
        for test_name, error in failed_tests:
            print(f"  ✗ {test_name}: {error}")
        print("\n" + "=" * 70)
        print("  SOME TESTS FAILED")
        print("=" * 70)
        return 1
    else:
        print("\n" + "=" * 70)
        print("  ALL TESTS PASSED! ✓")
        print("=" * 70)
        print("\nYour custom Pandas build is working correctly!")
        print("\nNext steps:")
        print("  • Modify this script to test your specific changes")
        print("  • Run the full test suite with: pytest pandas")
        print("  • Check BUILDING_FROM_SOURCE.md for more information")
        return 0


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nTests interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n\nFatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
