# Pandas Build Documentation & Tools

Welcome! This directory contains comprehensive documentation and tools for building Pandas from source code.

## 📁 Available Resources

### Documentation

| File | Description | Best For |
|------|-------------|----------|
| **[QUICK_START_BUILD.md](QUICK_START_BUILD.md)** | Quick reference guide | Users who want to build quickly |
| **[BUILDING_FROM_SOURCE.md](BUILDING_FROM_SOURCE.md)** | Comprehensive build guide | Detailed instructions and troubleshooting |
| **[README.md](README.md)** | Main project README | General Pandas information |

### Build Scripts

| File | Platform | Description |
|------|----------|-------------|
| **[build_and_test.sh](build_and_test.sh)** | Linux/macOS | Automated build and test script |
| **[build_and_test.bat](build_and_test.bat)** | Windows | Automated build and test script |

### Dependency & Test Files

| File | Purpose |
|------|---------|
| **[requirements-build.txt](requirements-build.txt)** | Build dependencies list |
| **[verify_build.py](verify_build.py)** | Comprehensive build verification script |

## 🚀 Quick Start

Choose your path:

### Option 1: Automated Build (Recommended for Beginners)

**Linux/macOS:**
```bash
chmod +x build_and_test.sh
./build_and_test.sh
```

**Windows:**
```cmd
build_and_test.bat
```

### Option 2: Manual Build (For More Control)

```bash
# 1. Install dependencies
pip install -r requirements-build.txt

# 2. Build and install
python -m pip install -ve . --no-build-isolation --config-settings editable-verbose=true

# 3. Verify
python verify_build.py
```

### Option 3: Quick Reference

See [QUICK_START_BUILD.md](QUICK_START_BUILD.md) for command-by-command instructions.

## 📖 Which Guide Should I Use?

```
┌─────────────────────────────────────────────┐
│ START: I want to build Pandas from source  │
└─────────────────────────────────────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │ How much time do you  │
        │ have?                 │
        └───────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
┌──────────────┐        ┌──────────────┐
│ 5 minutes    │        │ 30+ minutes  │
│ Quick build  │        │ Deep dive    │
└──────────────┘        └──────────────┘
        │                       │
        ▼                       ▼
┌──────────────┐        ┌──────────────┐
│ Use:         │        │ Use:         │
│ QUICK_START  │        │ BUILDING_    │
│ _BUILD.md    │        │ FROM_SOURCE  │
│              │        │ .md          │
│ OR           │        │              │
│ Run script:  │        │ For:         │
│ build_and_   │        │ - Detailed   │
│ test.sh      │        │   steps      │
└──────────────┘        │ - Trouble-   │
                        │   shooting   │
                        │ - Advanced   │
                        │   options    │
                        └──────────────┘
```

## 🛠️ Build Script Features

The automated build scripts (`build_and_test.sh` / `build_and_test.bat`) provide:

- ✅ Automatic dependency checking and installation
- ✅ Clean build option (`--clean`)
- ✅ Configurable testing (`--quick-test`, `--full-test`, `--no-test`)
- ✅ Color-coded output for easy reading
- ✅ Error handling and reporting
- ✅ Build verification

**Example Usage:**

```bash
# Clean build with quick tests
./build_and_test.sh --clean --quick-test

# Build without running tests
./build_and_test.sh --no-test

# Build with full test suite
./build_and_test.sh --full-test
```

## 🧪 Build Verification

After building, use `verify_build.py` to test your installation:

```bash
python verify_build.py
```

This script tests:
- ✓ Import functionality
- ✓ DataFrame/Series operations
- ✓ I/O operations (CSV, etc.)
- ✓ GroupBy operations
- ✓ Missing data handling
- ✓ DateTime functionality
- ✓ String operations
- ✓ And much more...

**Sample Output:**
```
============================================================
                Pandas Build Verification
============================================================

Testing: Import Pandas... ✓ PASS
Testing: Version Information... ✓ PASS
  Version: 2.3.0.dev0+1234.g5678abc
Testing: Core Components Import... ✓ PASS
...

============================================================
                     Test Summary
============================================================
Total Tests: 19
Passed: 19
Failed: 0

============================================================
ALL TESTS PASSED! ✓
============================================================
```

## 📋 Requirements

### System Requirements
- **Python**: 3.11 or higher
- **Disk Space**: ~2GB free
- **RAM**: 4GB recommended (8GB for running full test suite)
- **C/C++ Compiler**: GCC, Clang, or MSVC

### Build Dependencies
All listed in [requirements-build.txt](requirements-build.txt):
- meson-python (build backend)
- meson (build system)
- ninja (build tool)
- Cython (C extension compiler)
- NumPy 2.0+
- And more...

## 🔧 Troubleshooting

Common issues and solutions:

### Build Fails

1. **Try clean build**: `./build_and_test.sh --clean` or manually remove `build/`, `dist/` directories
2. **Check dependencies**: `pip install -r requirements-build.txt`
3. **Verify compiler**: Ensure C/C++ compiler is installed

### Import Fails

1. **Check you're not in source directory**: `cd ..` then try importing
2. **Verify installation**: `python -c "import pandas; print(pandas.__file__)"`
3. **Run verification**: `python verify_build.py`

### Tests Fail

1. **Some test failures are normal** in development builds
2. **Check specific test**: `pytest pandas/tests/test_algos.py -v`
3. **Skip slow tests**: `pytest pandas -m "not slow"`

For detailed troubleshooting, see the **Troubleshooting** section in [BUILDING_FROM_SOURCE.md](BUILDING_FROM_SOURCE.md).

## 🎯 Build Modes

Pandas supports different build modes for different use cases:

| Mode | Command | Use Case |
|------|---------|----------|
| **Development (Editable)** | `pip install -ve . --no-build-isolation` | Active development, code changes reflect immediately |
| **Standard Install** | `pip install .` | Production use, one-time build |
| **Wheel Build** | `python -m build --no-isolation` | Create distributable .whl file |

## 📚 Additional Resources

### Official Pandas Documentation
- [Contributing Environment](https://pandas.pydata.org/docs/dev/development/contributing_environment.html)
- [Contributing Guide](https://pandas.pydata.org/docs/dev/development/contributing.html)
- [Developer Documentation](https://pandas.pydata.org/docs/dev/)

### Community
- [GitHub Issues](https://github.com/pandas-dev/pandas/issues)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/pandas)
- [Pandas Slack](https://pandas.pydata.org/docs/dev/development/community.html)

### Build System
- [Meson Documentation](https://mesonbuild.com/)
- [meson-python](https://meson-python.readthedocs.io/)
- [Cython Documentation](https://cython.readthedocs.io/)

## 🤝 Contributing

If you're building from source to contribute to Pandas:

1. **Read**: [BUILDING_FROM_SOURCE.md](BUILDING_FROM_SOURCE.md)
2. **Build**: Use development mode (`pip install -ve . --no-build-isolation`)
3. **Test**: Run relevant tests before submitting PR
4. **Submit**: Follow [contributing guidelines](https://pandas.pydata.org/docs/dev/development/contributing.html)

## 💡 Tips for Success

- **Always use virtual environments** to avoid dependency conflicts
- **Use development mode (`-e`)** if you're modifying code
- **Run verification script** after building to ensure everything works
- **Read error messages carefully** - they often indicate exactly what's wrong
- **Check the detailed guides** when you encounter issues

## 📞 Need Help?

1. **Check documentation first**: [BUILDING_FROM_SOURCE.md](BUILDING_FROM_SOURCE.md) has detailed troubleshooting
2. **Run verification**: `python verify_build.py` to identify issues
3. **Search existing issues**: [GitHub Issues](https://github.com/pandas-dev/pandas/issues)
4. **Ask the community**: Stack Overflow, Slack, or PyData mailing list

## 📄 File Summary

```
.
├── BUILD_README.md              # This file - overview of build resources
├── QUICK_START_BUILD.md         # Quick reference for building
├── BUILDING_FROM_SOURCE.md      # Comprehensive build guide
├── requirements-build.txt       # Build dependencies
├── build_and_test.sh           # Automated build script (Unix)
├── build_and_test.bat          # Automated build script (Windows)
└── verify_build.py             # Build verification tests
```

## ✅ Summary

You now have everything needed to build Pandas from source:

1. **📖 Documentation** - Quick start and comprehensive guides
2. **🔧 Tools** - Automated build scripts for all platforms
3. **📦 Dependencies** - Pre-configured requirements file
4. **🧪 Verification** - Comprehensive test suite

**Start building now:**
- Quick path: Run `./build_and_test.sh` (or `.bat` on Windows)
- Guided path: Follow [QUICK_START_BUILD.md](QUICK_START_BUILD.md)
- Detailed path: Read [BUILDING_FROM_SOURCE.md](BUILDING_FROM_SOURCE.md)

Happy coding! 🐼
