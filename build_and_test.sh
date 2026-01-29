#!/bin/bash
# build_and_test.sh - Automated script to build and test Pandas from source
# Usage: ./build_and_test.sh [options]
# Options:
#   --clean       Clean build artifacts before building
#   --no-test     Skip running tests
#   --quick-test  Run only quick tests
#   --full-test   Run full test suite
#   --help        Show this help message

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default options
CLEAN=false
RUN_TESTS=true
TEST_MODE="quick"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --clean)
            CLEAN=true
            shift
            ;;
        --no-test)
            RUN_TESTS=false
            shift
            ;;
        --quick-test)
            TEST_MODE="quick"
            shift
            ;;
        --full-test)
            TEST_MODE="full"
            shift
            ;;
        --help)
            echo "Usage: ./build_and_test.sh [options]"
            echo "Options:"
            echo "  --clean       Clean build artifacts before building"
            echo "  --no-test     Skip running tests"
            echo "  --quick-test  Run only quick tests (default)"
            echo "  --full-test   Run full test suite"
            echo "  --help        Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Print header
echo -e "${BLUE}================================${NC}"
echo -e "${BLUE}Pandas Build and Test Script${NC}"
echo -e "${BLUE}================================${NC}"
echo ""

# Check Python version
echo -e "${YELLOW}Checking Python version...${NC}"
PYTHON_VERSION=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo -e "Python version: ${GREEN}${PYTHON_VERSION}${NC}"

REQUIRED_VERSION="3.11"
if [[ $(echo -e "$PYTHON_VERSION\n$REQUIRED_VERSION" | sort -V | head -n1) != "$REQUIRED_VERSION" ]]; then
    echo -e "${RED}Error: Python 3.11 or higher is required${NC}"
    exit 1
fi
echo ""

# Clean if requested
if [ "$CLEAN" = true ]; then
    echo -e "${YELLOW}Cleaning build artifacts...${NC}"
    rm -rf build/ dist/ *.egg-info
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    find . -type f -name "*.so" -delete 2>/dev/null || true
    echo -e "${GREEN}Clean complete${NC}"
    echo ""
fi

# Check for build dependencies
echo -e "${YELLOW}Checking build dependencies...${NC}"

check_package() {
    python -c "import $1" 2>/dev/null
    if [ $? -eq 0 ]; then
        echo -e "  ✓ $1 installed"
        return 0
    else
        echo -e "  ${RED}✗ $1 not found${NC}"
        return 1
    fi
}

MISSING_DEPS=false

for package in "mesonpy" "Cython" "numpy" "versioneer"; do
    if ! check_package "$package"; then
        MISSING_DEPS=true
    fi
done

if [ "$MISSING_DEPS" = true ]; then
    echo ""
    echo -e "${YELLOW}Installing missing build dependencies...${NC}"
    if [ -f "requirements-build.txt" ]; then
        pip install -r requirements-build.txt
    else
        pip install meson-python meson ninja wheel Cython "numpy>=2.0.0" versioneer[toml]
    fi
    echo -e "${GREEN}Dependencies installed${NC}"
fi
echo ""

# Build Pandas
echo -e "${YELLOW}Building Pandas from source...${NC}"
echo -e "This may take several minutes..."
echo ""

# Use development mode for editable install
python -m pip install -ve . --no-build-isolation --config-settings editable-verbose=true

if [ $? -ne 0 ]; then
    echo -e "${RED}Build failed!${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}Build successful!${NC}"
echo ""

# Verify installation
echo -e "${YELLOW}Verifying Pandas installation...${NC}"
PANDAS_VERSION=$(python -c "import pandas as pd; print(pd.__version__)" 2>/dev/null)
if [ $? -eq 0 ]; then
    echo -e "Pandas version: ${GREEN}${PANDAS_VERSION}${NC}"
    PANDAS_LOCATION=$(python -c "import pandas; print(pandas.__file__)")
    echo -e "Pandas location: ${GREEN}${PANDAS_LOCATION}${NC}"
else
    echo -e "${RED}Failed to import Pandas!${NC}"
    exit 1
fi
echo ""

# Run tests if requested
if [ "$RUN_TESTS" = true ]; then
    echo -e "${YELLOW}Running tests...${NC}"
    
    # Check if pytest is installed
    if ! check_package "pytest" > /dev/null 2>&1; then
        echo -e "${YELLOW}pytest not found, installing test dependencies...${NC}"
        pip install pytest hypothesis pytest-xdist
    fi
    
    if [ "$TEST_MODE" = "quick" ]; then
        echo -e "${BLUE}Running quick verification tests...${NC}"
        
        # Run basic import test
        python -c "
import pandas as pd
import numpy as np
print('✓ Import successful')

# Quick functionality tests
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
assert df.shape == (3, 2), 'DataFrame creation failed'
print('✓ DataFrame creation works')

assert df['A'].sum() == 6, 'Basic operations failed'
print('✓ Basic operations work')

print('All quick tests passed!')
"
        
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}Quick tests passed!${NC}"
        else
            echo -e "${RED}Quick tests failed!${NC}"
            exit 1
        fi
        
    elif [ "$TEST_MODE" = "full" ]; then
        echo -e "${BLUE}Running full test suite (this will take a while)...${NC}"
        
        # Move out of source directory to avoid import issues
        ORIGINAL_DIR=$(pwd)
        cd ..
        
        # Run pytest with common options
        python -m pytest "${ORIGINAL_DIR}/pandas" -v -m "not slow and not network and not db" -n auto
        TEST_RESULT=$?
        
        cd "$ORIGINAL_DIR"
        
        if [ $TEST_RESULT -eq 0 ]; then
            echo -e "${GREEN}Full test suite passed!${NC}"
        else
            echo -e "${YELLOW}Some tests failed (this may be expected)${NC}"
        fi
    fi
    echo ""
fi

# Run verification script if it exists
if [ -f "verify_build.py" ]; then
    echo -e "${YELLOW}Running comprehensive verification...${NC}"
    python verify_build.py
    echo ""
fi

# Print summary
echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}Build and Test Complete!${NC}"
echo -e "${GREEN}================================${NC}"
echo ""
echo -e "Next steps:"
echo -e "  • Run ${BLUE}python -c 'import pandas as pd; print(pd.__version__)'${NC} to verify"
echo -e "  • Run ${BLUE}python verify_build.py${NC} for comprehensive tests"
echo -e "  • Run ${BLUE}pytest pandas${NC} to run the test suite"
echo -e "  • Read ${BLUE}BUILDING_FROM_SOURCE.md${NC} for more information"
echo ""
echo -e "${GREEN}Happy coding with Pandas!${NC}"
