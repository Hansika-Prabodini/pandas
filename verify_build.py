#!/usr/bin/env python
"""
verify_build.py - Comprehensive verification script for Pandas build

This script tests the basic functionality of a Pandas installation to ensure
that the build was successful. It performs various tests including:
- Import verification
- Version checking
- DataFrame operations
- Series operations
- Data I/O operations
- Common computational functions
- Extension types

Usage:
    python verify_build.py
    
Exit codes:
    0 - All tests passed
    1 - One or more tests failed
"""

import sys
import traceback
from io import StringIO


class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def print_header(text):
    """Print a formatted header"""
    print(f"\n{Colors.BLUE}{Colors.BOLD}{'=' * 60}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}{text:^60}{Colors.END}")
    print(f"{Colors.BLUE}{Colors.BOLD}{'=' * 60}{Colors.END}\n")


def print_test(test_name):
    """Print test name"""
    print(f"{Colors.YELLOW}Testing: {test_name}...{Colors.END}", end=" ")
    sys.stdout.flush()


def print_pass():
    """Print pass message"""
    print(f"{Colors.GREEN}✓ PASS{Colors.END}")


def print_fail(error=None):
    """Print fail message"""
    print(f"{Colors.RED}✗ FAIL{Colors.END}")
    if error:
        print(f"{Colors.RED}  Error: {error}{Colors.END}")


def run_test(test_func, test_name):
    """
    Run a single test function and handle exceptions
    
    Parameters
    ----------
    test_func : callable
        The test function to run
    test_name : str
        Name of the test for display
        
    Returns
    -------
    bool
        True if test passed, False otherwise
    """
    print_test(test_name)
    try:
        test_func()
        print_pass()
        return True
    except Exception as e:
        print_fail(str(e))
        if "--verbose" in sys.argv or "-v" in sys.argv:
            traceback.print_exc()
        return False


def test_import():
    """Test that pandas can be imported"""
    import pandas as pd
    assert pd is not None, "Pandas import returned None"


def test_version():
    """Test that version information is available"""
    import pandas as pd
    version = pd.__version__
    assert version is not None and len(version) > 0, "Version string is empty"
    print(f"\n  Version: {version}")


def test_basic_imports():
    """Test that core pandas components can be imported"""
    from pandas import DataFrame, Series, Index
    assert DataFrame is not None
    assert Series is not None
    assert Index is not None


def test_numpy_integration():
    """Test NumPy integration"""
    import pandas as pd
    import numpy as np
    
    arr = np.array([1, 2, 3, 4, 5])
    s = pd.Series(arr)
    assert len(s) == 5, "Series length mismatch"
    assert s.sum() == 15, "Series sum incorrect"


def test_dataframe_creation():
    """Test DataFrame creation"""
    import pandas as pd
    
    # From dict
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    assert df.shape == (3, 2), f"Expected shape (3, 2), got {df.shape}"
    
    # From list
    df2 = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
    assert df2.shape == (2, 2), f"Expected shape (2, 2), got {df2.shape}"


def test_series_creation():
    """Test Series creation"""
    import pandas as pd
    
    s = pd.Series([1, 2, 3, 4, 5])
    assert len(s) == 5, f"Expected length 5, got {len(s)}"
    assert s.dtype == int, f"Expected dtype int, got {s.dtype}"


def test_indexing():
    """Test DataFrame indexing and slicing"""
    import pandas as pd
    
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    
    # Column access
    assert list(df['A']) == [1, 2, 3], "Column access failed"
    
    # Row access
    assert df.iloc[0, 0] == 1, "iloc access failed"
    assert df.loc[0, 'A'] == 1, "loc access failed"
    
    # Slicing
    subset = df[['A', 'B']]
    assert subset.shape == (3, 2), "Column slicing failed"


def test_basic_operations():
    """Test basic arithmetic and statistical operations"""
    import pandas as pd
    
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Arithmetic
    df['C'] = df['A'] + df['B']
    assert list(df['C']) == [5, 7, 9], "Addition failed"
    
    # Statistics
    assert df['A'].mean() == 2.0, "Mean calculation failed"
    assert df['A'].sum() == 6, "Sum calculation failed"
    assert df['A'].std() > 0, "Std calculation failed"


def test_groupby():
    """Test groupby operations"""
    import pandas as pd
    
    df = pd.DataFrame({
        'Category': ['A', 'B', 'A', 'B', 'A'],
        'Values': [1, 2, 3, 4, 5]
    })
    
    grouped = df.groupby('Category')['Values'].sum()
    assert grouped['A'] == 9, "Groupby sum for 'A' failed"
    assert grouped['B'] == 6, "Groupby sum for 'B' failed"


def test_merge_join():
    """Test merge and join operations"""
    import pandas as pd
    
    df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'val1': [1, 2, 3]})
    df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'val2': [4, 5, 6]})
    
    merged = pd.merge(df1, df2, on='key', how='inner')
    assert len(merged) == 2, "Merge failed"
    assert list(merged['key']) == ['A', 'B'], "Merge keys incorrect"


def test_missing_data():
    """Test handling of missing data"""
    import pandas as pd
    import numpy as np
    
    s = pd.Series([1, 2, np.nan, 4, 5])
    assert s.isna().sum() == 1, "NA detection failed"
    
    filled = s.fillna(0)
    assert filled.isna().sum() == 0, "fillna failed"
    
    dropped = s.dropna()
    assert len(dropped) == 4, "dropna failed"


def test_datetime():
    """Test datetime functionality"""
    import pandas as pd
    
    dates = pd.date_range('2024-01-01', periods=5, freq='D')
    assert len(dates) == 5, "Date range creation failed"
    
    df = pd.DataFrame({'date': dates, 'value': [1, 2, 3, 4, 5]})
    df.set_index('date', inplace=True)
    assert df.index.dtype == 'datetime64[ns]', "Datetime index failed"


def test_csv_io():
    """Test CSV read/write operations"""
    import pandas as pd
    from io import StringIO
    
    # Create test data
    csv_data = StringIO("A,B,C\n1,2,3\n4,5,6\n7,8,9")
    df = pd.read_csv(csv_data)
    
    assert df.shape == (3, 3), "CSV read failed"
    assert list(df.columns) == ['A', 'B', 'C'], "CSV columns incorrect"
    
    # Test write
    output = StringIO()
    df.to_csv(output, index=False)
    assert len(output.getvalue()) > 0, "CSV write failed"


def test_categorical():
    """Test categorical data type"""
    import pandas as pd
    
    s = pd.Series(['a', 'b', 'c', 'a', 'b'], dtype='category')
    assert s.dtype.name == 'category', "Categorical creation failed"
    assert len(s.cat.categories) == 3, "Category count incorrect"


def test_string_operations():
    """Test string operations"""
    import pandas as pd
    
    s = pd.Series(['hello', 'world', 'pandas'])
    upper = s.str.upper()
    assert list(upper) == ['HELLO', 'WORLD', 'PANDAS'], "String upper failed"
    
    contains = s.str.contains('and')
    assert contains[2] == True, "String contains failed"


def test_pivot():
    """Test pivot operations"""
    import pandas as pd
    
    df = pd.DataFrame({
        'A': ['foo', 'foo', 'bar', 'bar'],
        'B': ['one', 'two', 'one', 'two'],
        'C': [1, 2, 3, 4]
    })
    
    pivot = df.pivot_table(values='C', index='A', columns='B', aggfunc='sum')
    assert pivot.shape[0] == 2, "Pivot failed"


def test_sorting():
    """Test sorting operations"""
    import pandas as pd
    
    df = pd.DataFrame({'A': [3, 1, 2], 'B': [6, 4, 5]})
    sorted_df = df.sort_values('A')
    assert list(sorted_df['A']) == [1, 2, 3], "Sort by column failed"


def test_apply():
    """Test apply operations"""
    import pandas as pd
    
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = df['A'].apply(lambda x: x * 2)
    assert list(result) == [2, 4, 6], "Apply failed"


def test_concatenate():
    """Test concatenation"""
    import pandas as pd
    
    df1 = pd.DataFrame({'A': [1, 2]})
    df2 = pd.DataFrame({'A': [3, 4]})
    
    result = pd.concat([df1, df2], ignore_index=True)
    assert len(result) == 4, "Concatenation failed"
    assert list(result['A']) == [1, 2, 3, 4], "Concatenation values incorrect"


def main():
    """Main test runner"""
    print_header("Pandas Build Verification")
    
    print(f"{Colors.BOLD}This script will verify your Pandas installation{Colors.END}")
    print(f"{Colors.BOLD}by running a series of functionality tests.{Colors.END}\n")
    
    # Define all tests
    tests = [
        (test_import, "Import Pandas"),
        (test_version, "Version Information"),
        (test_basic_imports, "Core Components Import"),
        (test_numpy_integration, "NumPy Integration"),
        (test_dataframe_creation, "DataFrame Creation"),
        (test_series_creation, "Series Creation"),
        (test_indexing, "Indexing and Slicing"),
        (test_basic_operations, "Basic Operations"),
        (test_groupby, "GroupBy Operations"),
        (test_merge_join, "Merge/Join Operations"),
        (test_missing_data, "Missing Data Handling"),
        (test_datetime, "DateTime Functionality"),
        (test_csv_io, "CSV I/O Operations"),
        (test_categorical, "Categorical Data Type"),
        (test_string_operations, "String Operations"),
        (test_pivot, "Pivot Operations"),
        (test_sorting, "Sorting Operations"),
        (test_apply, "Apply Operations"),
        (test_concatenate, "Concatenation"),
    ]
    
    # Run all tests
    results = []
    for test_func, test_name in tests:
        result = run_test(test_func, test_name)
        results.append((test_name, result))
    
    # Print summary
    print_header("Test Summary")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    failed = total - passed
    
    print(f"Total Tests: {total}")
    print(f"{Colors.GREEN}Passed: {passed}{Colors.END}")
    if failed > 0:
        print(f"{Colors.RED}Failed: {failed}{Colors.END}")
        print(f"\n{Colors.YELLOW}Failed tests:{Colors.END}")
        for test_name, result in results:
            if not result:
                print(f"  {Colors.RED}✗ {test_name}{Colors.END}")
    else:
        print(f"{Colors.GREEN}Failed: 0{Colors.END}")
    
    # Print overall result
    print()
    if failed == 0:
        print(f"{Colors.GREEN}{Colors.BOLD}{'=' * 60}{Colors.END}")
        print(f"{Colors.GREEN}{Colors.BOLD}ALL TESTS PASSED! ✓{Colors.END}")
        print(f"{Colors.GREEN}{Colors.BOLD}{'=' * 60}{Colors.END}")
        print(f"\n{Colors.GREEN}Your Pandas build is working correctly!{Colors.END}\n")
        return 0
    else:
        print(f"{Colors.RED}{Colors.BOLD}{'=' * 60}{Colors.END}")
        print(f"{Colors.RED}{Colors.BOLD}SOME TESTS FAILED! ✗{Colors.END}")
        print(f"{Colors.RED}{Colors.BOLD}{'=' * 60}{Colors.END}")
        print(f"\n{Colors.YELLOW}Please check the errors above and consult BUILDING_FROM_SOURCE.md{Colors.END}\n")
        return 1


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Verification interrupted by user{Colors.END}")
        sys.exit(130)
    except Exception as e:
        print(f"\n{Colors.RED}Fatal error during verification:{Colors.END}")
        print(f"{Colors.RED}{str(e)}{Colors.END}")
        traceback.print_exc()
        sys.exit(1)
