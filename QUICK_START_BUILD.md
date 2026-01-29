# Quick Start: Building Pandas from Source

This is a quick reference guide for building Pandas from source. For detailed instructions and troubleshooting, see [BUILDING_FROM_SOURCE.md](BUILDING_FROM_SOURCE.md).

## ⚡ TL;DR - Fast Build (5 minutes)

```bash
# 1. Clone the repository
git clone https://github.com/pandas-dev/pandas.git
cd pandas

# 2. Install build dependencies
pip install -r requirements-build.txt

# 3. Build and install (development mode)
python -m pip install -ve . --no-build-isolation --config-settings editable-verbose=true

# 4. Verify installation
python verify_build.py
```

## 📋 Prerequisites

- Python 3.11+
- Git
- C/C++ compiler (gcc/clang/MSVC)
- ~2GB free disk space

## 🚀 Step-by-Step Quick Guide

### 1. Clone Repository

```bash
git clone https://github.com/pandas-dev/pandas.git
cd pandas
```

### 2. Set Up Environment (Recommended)

```bash
# Create virtual environment
python -m venv pandas-env
source pandas-env/bin/activate  # On Windows: pandas-env\Scripts\activate
```

### 3. Install Dependencies

```bash
# Using requirements file (recommended)
pip install -r requirements-build.txt

# Or install manually
pip install meson-python meson ninja wheel Cython "numpy>=2.0.0" versioneer[toml]
```

### 4. Build Pandas

**For Development (editable install):**
```bash
python -m pip install -ve . --no-build-isolation --config-settings editable-verbose=true
```

**For Standard Install:**
```bash
pip install .
```

### 5. Verify Build

```bash
# Quick test
python -c "import pandas as pd; print(pd.__version__)"

# Comprehensive test
python verify_build.py

# Run unit tests
pytest pandas -n auto -m "not slow"
```

## 🛠️ Automated Build Script

We provide an automated build script that handles everything:

```bash
# Make script executable (Unix/Linux/macOS)
chmod +x build_and_test.sh

# Run with default options (build + quick test)
./build_and_test.sh

# Clean build
./build_and_test.sh --clean

# Build without testing
./build_and_test.sh --no-test

# Build with full test suite
./build_and_test.sh --full-test
```

## 📦 What Gets Built?

The build process:
1. **Compiles Cython extensions** (.pyx → .c → .so)
2. **Builds C extensions** for performance-critical operations
3. **Installs Python modules** in editable mode (for development)
4. **Creates importable package** ready to use

## 🧪 Testing Your Build

### Quick Verification
```bash
python verify_build.py
```

### Run Specific Tests
```bash
# Test DataFrames
pytest pandas/tests/frame/

# Test I/O operations
pytest pandas/tests/io/

# Test a specific file
pytest pandas/tests/test_algos.py -v
```

### Run Full Test Suite
```bash
# All tests (takes ~30+ minutes)
pytest pandas

# Parallel execution (faster)
pytest pandas -n auto

# Skip slow tests
pytest pandas -m "not slow" -n auto
```

## 🔧 Common Issues & Quick Fixes

### Build Fails: "No C compiler found"

**Linux:**
```bash
sudo apt-get install build-essential  # Ubuntu/Debian
sudo yum groupinstall "Development Tools"  # RHEL/CentOS
```

**macOS:**
```bash
xcode-select --install
```

**Windows:**
Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

### Import Error: "No module named pandas"

```bash
# Make sure you're not in the pandas source directory
cd ..
python -c "import pandas as pd; print(pd.__version__)"
```

### Cython Version Issues

```bash
pip install --upgrade "Cython>=3.0.0,<4.0.0a0"
```

### Clean Build (fixes most issues)

```bash
# Remove all build artifacts
rm -rf build/ dist/ *.egg-info

# Reinstall
python -m pip install -ve . --no-build-isolation
```

## 📊 Build Modes Comparison

| Mode | Command | Use Case | Rebuild Required? |
|------|---------|----------|-------------------|
| **Development** | `pip install -ve . --no-build-isolation` | Active development | Only for C/Cython changes |
| **Standard** | `pip install .` | One-time build | Yes, for any change |
| **Wheel** | `python -m build --no-isolation` | Distribution | N/A (creates .whl file) |

## 🎯 Next Steps After Building

1. **Read the docs**: Check [BUILDING_FROM_SOURCE.md](BUILDING_FROM_SOURCE.md) for detailed info
2. **Explore the code**: Navigate through `pandas/` directory
3. **Make changes**: Edit code and test immediately (dev mode)
4. **Run tests**: Use `pytest` to verify your changes
5. **Contribute**: See [Contributing Guide](https://pandas.pydata.org/docs/dev/development/contributing.html)

## 💡 Pro Tips

- **Use virtual environments** to avoid conflicts
- **Enable editable mode** (`-e`) for development work
- **Run tests in parallel** with `-n auto` for speed
- **Use `--no-build-isolation`** to speed up rebuilds
- **Keep dependencies updated** with `pip install --upgrade -r requirements-build.txt`

## 📚 Additional Resources

- **Full Build Guide**: [BUILDING_FROM_SOURCE.md](BUILDING_FROM_SOURCE.md)
- **Pandas Documentation**: https://pandas.pydata.org/docs/
- **Contributing Guide**: https://pandas.pydata.org/docs/dev/development/contributing.html
- **GitHub Repository**: https://github.com/pandas-dev/pandas
- **Issue Tracker**: https://github.com/pandas-dev/pandas/issues

## 🆘 Need Help?

- Check [BUILDING_FROM_SOURCE.md](BUILDING_FROM_SOURCE.md) for detailed troubleshooting
- Visit [Stack Overflow](https://stackoverflow.com/questions/tagged/pandas) with tag `pandas`
- Join [Pandas Slack](https://pandas.pydata.org/docs/dev/development/community.html)
- Ask on [PyData Mailing List](https://groups.google.com/forum/#!forum/pydata)

---

**Happy Building! 🐼**

For a comprehensive guide with detailed explanations and advanced topics, see [BUILDING_FROM_SOURCE.md](BUILDING_FROM_SOURCE.md).
