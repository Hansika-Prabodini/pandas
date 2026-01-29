# Building Pandas from Source

This guide provides comprehensive instructions for compiling and installing Pandas from source code. Building from source allows you to work with the latest development version, contribute to the project, or create custom modifications.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Step 1: Clone the Repository](#step-1-clone-the-repository)
- [Step 2: Install Build Dependencies](#step-2-install-build-dependencies)
- [Step 3: Build Pandas](#step-3-build-pandas)
- [Step 4: Run Tests](#step-4-run-tests)
- [Step 5: Install Pandas](#step-5-install-pandas)
- [Troubleshooting](#troubleshooting)
- [Alternative Build Methods](#alternative-build-methods)

## Prerequisites

Before building Pandas from source, ensure you have:

- **Python 3.11 or higher** - Check with `python --version`
- **Git** - For cloning the repository
- **C/C++ Compiler** - Required for compiling extensions
  - Linux: GCC (usually pre-installed)
  - macOS: Xcode Command Line Tools (`xcode-select --install`)
  - Windows: Microsoft Visual C++ 14.0 or greater (via Visual Studio Build Tools)
- **At least 2GB of free disk space** - For source code and build artifacts

## Step 1: Clone the Repository

Clone the Pandas repository from GitHub:

```bash
# Clone the repository
git clone https://github.com/pandas-dev/pandas.git

# Navigate to the directory
cd pandas
```

If you want to work on a specific branch or version:

```bash
# List available branches
git branch -a

# Checkout a specific branch (e.g., main)
git checkout main

# Or checkout a specific tag/version
git checkout v2.2.0
```

## Step 2: Install Build Dependencies

Pandas uses **meson-python** as its build backend. You'll need to install several build dependencies.

### Option A: Using pip (Recommended)

Install the build dependencies listed in `pyproject.toml`:

```bash
# Install build dependencies
pip install meson-python meson ninja wheel Cython numpy>=2.0.0 versioneer[toml]

# Install runtime dependencies
pip install numpy python-dateutil pytz tzdata

# Install optional test dependencies
pip install pytest hypothesis pytest-xdist
```

### Option B: Using the requirements file

You can use the provided `requirements-build.txt` file:

```bash
pip install -r requirements-build.txt
```

### Option C: Using conda

If you prefer conda:

```bash
# Create a new conda environment
conda create -n pandas-dev python=3.11

# Activate the environment
conda activate pandas-dev

# Install dependencies
conda install -c conda-forge meson-python meson ninja cython numpy pytest hypothesis
```

## Step 3: Build Pandas

There are several ways to build Pandas, depending on your needs.

### Development Build (Editable Install - Recommended for Development)

This is the recommended method if you plan to modify the code:

```bash
# Build and install in editable/development mode
python -m pip install -ve . --no-build-isolation --config-settings editable-verbose=true
```

**What this does:**
- `-v`: Verbose output
- `-e`: Editable mode (changes to Python files are immediately reflected)
- `--no-build-isolation`: Uses your environment's dependencies instead of creating isolated build environment
- `--config-settings editable-verbose=true`: Provides detailed build information

### Standard Build and Install

For a regular installation:

```bash
# Build and install
pip install .
```

### Build Without Installing

To build without installing (useful for testing):

```bash
# Using pip build
pip install build
python -m build --no-isolation

# The built wheel will be in the dist/ directory
```

### Using meson directly (Advanced)

For more control over the build process:

```bash
# Configure the build
meson setup build --prefix=$PWD/install

# Compile
meson compile -C build

# Install to the prefix directory
meson install -C build
```

## Step 4: Run Tests

After building, it's important to verify that everything works correctly.

### Quick Verification

Run a quick test to ensure Pandas imports correctly:

```bash
python -c "import pandas as pd; print(pd.__version__); print('Pandas imported successfully!')"
```

### Run the Test Suite with pytest

Pandas uses pytest for testing. You can run the entire test suite or specific tests:

```bash
# Run all tests (this will take a while!)
pytest pandas

# Run tests with multiple workers (faster)
pytest -n auto pandas

# Run tests for a specific module
pytest pandas/tests/frame/

# Run a specific test file
pytest pandas/tests/test_algos.py

# Run tests with verbose output
pytest -v pandas/tests/test_algos.py

# Run only fast tests (skip slow tests)
pytest -m "not slow" pandas
```

### Using pandas' built-in test runner

Pandas provides a convenient test runner:

```python
import pandas as pd

# Run all tests
pd.test()

# Run with specific arguments
pd.test(extra_args=['-v', '-m', 'not slow'])
```

### Run the verification script

Use the provided verification script:

```bash
python verify_build.py
```

This script will test basic functionality including:
- Pandas import
- Version check
- DataFrame creation and manipulation
- Basic operations
- Data I/O operations

## Step 5: Install Pandas

If you built without installing, you can install now:

```bash
# Install from the built wheel (if you used python -m build)
pip install dist/pandas-*.whl

# Or install directly
pip install .
```

### Verify Installation

```bash
# Check installation location
python -c "import pandas; print(pandas.__file__)"

# Check version
python -c "import pandas; print(pandas.__version__)"

# Run basic functionality test
python verify_build.py
```

## Troubleshooting

### Common Issues

#### 1. Compiler Not Found

**Error:** `error: Microsoft Visual C++ 14.0 or greater is required`

**Solution (Windows):** Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

**Solution (Linux):** `sudo apt-get install build-essential` (Ubuntu/Debian) or `sudo yum groupinstall "Development Tools"` (RHEL/CentOS)

**Solution (macOS):** `xcode-select --install`

#### 2. Cython Version Issues

**Error:** `Cython version mismatch`

**Solution:**
```bash
pip install --upgrade "Cython<4.0.0a0"
```

#### 3. NumPy Version Conflicts

**Error:** `NumPy version mismatch`

**Solution:**
```bash
pip install --upgrade "numpy>=2.0.0"
```

#### 4. Meson Not Found

**Error:** `meson: command not found`

**Solution:**
```bash
pip install --upgrade meson meson-python ninja
```

#### 5. Build Fails with "Permission Denied"

**Solution:**
```bash
# Don't use sudo with pip, use user install instead
pip install --user -ve . --no-build-isolation
```

#### 6. Out of Memory During Build

**Solution:**
```bash
# Limit parallel jobs
export MESON_BUILD_JOBS=2
pip install -ve . --no-build-isolation
```

#### 7. Tests Fail to Import Pandas

**Solution:**
```bash
# Make sure you're not in the pandas source directory when running tests
cd ..
python -c "import pandas as pd; pd.test()"
```

### Clean Build

If you encounter persistent build issues, try a clean build:

```bash
# Remove build artifacts
git clean -xfd

# Or manually remove
rm -rf build/ dist/ *.egg-info

# Then rebuild
pip install -ve . --no-build-isolation
```

## Alternative Build Methods

### Using Docker

Build in a containerized environment:

```dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone and build pandas
WORKDIR /workspace
RUN git clone https://github.com/pandas-dev/pandas.git
WORKDIR /workspace/pandas
RUN pip install meson-python meson ninja wheel Cython numpy
RUN pip install -ve . --no-build-isolation

CMD ["python"]
```

### Using Virtual Environment (Recommended)

Always use a virtual environment to avoid conflicts:

```bash
# Create virtual environment
python -m venv pandas-env

# Activate (Linux/macOS)
source pandas-env/bin/activate

# Activate (Windows)
pandas-env\Scripts\activate

# Install and build
pip install -r requirements-build.txt
pip install -ve . --no-build-isolation
```

### Using conda Environment

```bash
# Create environment from environment file (if available)
conda env create -f environment.yml

# Or create manually
conda create -n pandas-dev python=3.11
conda activate pandas-dev
conda install -c conda-forge meson-python meson ninja cython numpy pytest
pip install -ve . --no-build-isolation
```

## Build Configuration Options

### Environment Variables

You can customize the build with environment variables:

```bash
# Set number of parallel build jobs
export MESON_BUILD_JOBS=4

# Enable debug build
export CFLAGS="-O0 -g"

# Disable certain optimizations
export CXXFLAGS="-O0 -g"
```

### Meson Build Options

When using meson directly:

```bash
# Debug build
meson setup build --buildtype=debug

# Release build with optimizations
meson setup build --buildtype=release

# Custom prefix
meson setup build --prefix=/custom/install/path
```

## Performance Testing

After building, you can run performance benchmarks:

```bash
# Install asv (Airspeed Velocity)
pip install asv

# Run benchmarks
cd benchmarks
asv run
```

## Contributing

If you're building from source to contribute:

1. **Fork the repository** on GitHub
2. **Clone your fork**: `git clone https://github.com/YOUR_USERNAME/pandas.git`
3. **Create a branch**: `git checkout -b my-feature`
4. **Make changes and build**: `pip install -ve . --no-build-isolation`
5. **Run tests**: `pytest pandas/tests/`
6. **Submit a pull request**

See the [contributing guide](https://pandas.pydata.org/docs/dev/development/contributing.html) for more details.

## Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Contributing Guide](https://pandas.pydata.org/docs/dev/development/contributing.html)
- [Developer Environment Setup](https://pandas.pydata.org/docs/dev/development/contributing_environment.html)
- [GitHub Repository](https://github.com/pandas-dev/pandas)
- [Issue Tracker](https://github.com/pandas-dev/pandas/issues)

## Summary

Quick reference for building from source:

```bash
# 1. Clone
git clone https://github.com/pandas-dev/pandas.git
cd pandas

# 2. Install dependencies
pip install meson-python meson ninja wheel Cython "numpy>=2.0.0" versioneer[toml]

# 3. Build and install (development mode)
python -m pip install -ve . --no-build-isolation --config-settings editable-verbose=true

# 4. Test
python -c "import pandas as pd; print(pd.__version__)"
pytest pandas -n auto

# 5. Verify
python verify_build.py
```

For more help, visit the [Pandas community](https://pandas.pydata.org/docs/dev/development/community.html) or ask on [Stack Overflow](https://stackoverflow.com/questions/tagged/pandas).
