@echo off
REM build_and_test.bat - Automated script to build and test Pandas from source (Windows)
REM Usage: build_and_test.bat [options]
REM Options:
REM   --clean       Clean build artifacts before building
REM   --no-test     Skip running tests
REM   --quick-test  Run only quick tests
REM   --full-test   Run full test suite
REM   --help        Show this help message

setlocal enabledelayedexpansion

REM Default options
set CLEAN=false
set RUN_TESTS=true
set TEST_MODE=quick

REM Parse command line arguments
:parse_args
if "%1"=="" goto end_parse
if "%1"=="--clean" (
    set CLEAN=true
    shift
    goto parse_args
)
if "%1"=="--no-test" (
    set RUN_TESTS=false
    shift
    goto parse_args
)
if "%1"=="--quick-test" (
    set TEST_MODE=quick
    shift
    goto parse_args
)
if "%1"=="--full-test" (
    set TEST_MODE=full
    shift
    goto parse_args
)
if "%1"=="--help" (
    echo Usage: build_and_test.bat [options]
    echo Options:
    echo   --clean       Clean build artifacts before building
    echo   --no-test     Skip running tests
    echo   --quick-test  Run only quick tests (default^)
    echo   --full-test   Run full test suite
    echo   --help        Show this help message
    exit /b 0
)
echo Unknown option: %1
echo Use --help for usage information
exit /b 1

:end_parse

REM Print header
echo ================================
echo Pandas Build and Test Script
echo ================================
echo.

REM Check Python version
echo Checking Python version...
python -c "import sys; print(f'Python version: {sys.version_info.major}.{sys.version_info.minor}')"
if errorlevel 1 (
    echo Error: Python not found!
    exit /b 1
)

python -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)"
if errorlevel 1 (
    echo Error: Python 3.11 or higher is required
    exit /b 1
)
echo.

REM Clean if requested
if "%CLEAN%"=="true" (
    echo Cleaning build artifacts...
    if exist build rmdir /s /q build
    if exist dist rmdir /s /q dist
    for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
    for /r . %%f in (*.pyc) do @if exist "%%f" del /q "%%f"
    for /r . %%f in (*.pyd) do @if exist "%%f" del /q "%%f"
    echo Clean complete
    echo.
)

REM Check for build dependencies
echo Checking build dependencies...

REM Check each package
python -c "import mesonpy" 2>nul
if errorlevel 1 (
    echo   X mesonpy not found
    set MISSING_DEPS=true
) else (
    echo   + mesonpy installed
)

python -c "import Cython" 2>nul
if errorlevel 1 (
    echo   X Cython not found
    set MISSING_DEPS=true
) else (
    echo   + Cython installed
)

python -c "import numpy" 2>nul
if errorlevel 1 (
    echo   X numpy not found
    set MISSING_DEPS=true
) else (
    echo   + numpy installed
)

python -c "import versioneer" 2>nul
if errorlevel 1 (
    echo   X versioneer not found
    set MISSING_DEPS=true
) else (
    echo   + versioneer installed
)

if defined MISSING_DEPS (
    echo.
    echo Installing missing build dependencies...
    if exist requirements-build.txt (
        pip install -r requirements-build.txt
    ) else (
        pip install meson-python meson ninja wheel Cython "numpy>=2.0.0" versioneer[toml]
    )
    if errorlevel 1 (
        echo Failed to install dependencies!
        exit /b 1
    )
    echo Dependencies installed
)
echo.

REM Build Pandas
echo Building Pandas from source...
echo This may take several minutes...
echo.

python -m pip install -ve . --no-build-isolation --config-settings editable-verbose=true

if errorlevel 1 (
    echo Build failed!
    exit /b 1
)

echo.
echo Build successful!
echo.

REM Verify installation
echo Verifying Pandas installation...
python -c "import pandas as pd; print(f'Pandas version: {pd.__version__}')"
if errorlevel 1 (
    echo Failed to import Pandas!
    exit /b 1
)

python -c "import pandas; print(f'Pandas location: {pandas.__file__}')"
echo.

REM Run tests if requested
if "%RUN_TESTS%"=="true" (
    echo Running tests...
    
    REM Check if pytest is installed
    python -c "import pytest" 2>nul
    if errorlevel 1 (
        echo pytest not found, installing test dependencies...
        pip install pytest hypothesis pytest-xdist
    )
    
    if "%TEST_MODE%"=="quick" (
        echo Running quick verification tests...
        
        python -c "import pandas as pd; import numpy as np; df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}); assert df.shape == (3, 2); assert df['A'].sum() == 6; print('All quick tests passed!')"
        
        if errorlevel 1 (
            echo Quick tests failed!
            exit /b 1
        ) else (
            echo Quick tests passed!
        )
        
    ) else if "%TEST_MODE%"=="full" (
        echo Running full test suite (this will take a while^)...
        
        REM Run pytest with common options
        python -m pytest pandas -v -m "not slow and not network and not db" -n auto
        
        if errorlevel 1 (
            echo Some tests failed (this may be expected^)
        ) else (
            echo Full test suite passed!
        )
    )
    echo.
)

REM Run verification script if it exists
if exist verify_build.py (
    echo Running comprehensive verification...
    python verify_build.py
    echo.
)

REM Print summary
echo ================================
echo Build and Test Complete!
echo ================================
echo.
echo Next steps:
echo   * Run 'python -c "import pandas as pd; print(pd.__version__)"' to verify
echo   * Run 'python verify_build.py' for comprehensive tests
echo   * Run 'pytest pandas' to run the test suite
echo   * Read BUILDING_FROM_SOURCE.md for more information
echo.
echo Happy coding with Pandas!

endlocal
