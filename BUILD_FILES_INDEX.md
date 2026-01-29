# Build Files Index

This document provides an index of all files created for building Pandas from source.

## 📑 Complete File List

### Documentation Files

1. **[BUILD_README.md](BUILD_README.md)**
   - **Purpose**: Main overview of all build resources
   - **Use**: Start here to understand what's available
   - **Size**: ~10 KB
   - **For**: Everyone building from source

2. **[QUICK_START_BUILD.md](QUICK_START_BUILD.md)**
   - **Purpose**: Quick reference guide with minimal instructions
   - **Use**: Fast build without reading extensive documentation
   - **Size**: ~5 KB
   - **For**: Experienced users, quick builds

3. **[BUILDING_FROM_SOURCE.md](BUILDING_FROM_SOURCE.md)**
   - **Purpose**: Comprehensive build guide with detailed explanations
   - **Use**: Complete instructions, troubleshooting, and advanced options
   - **Size**: ~15 KB
   - **For**: First-time builders, troubleshooting issues

4. **[BUILD_FILES_INDEX.md](BUILD_FILES_INDEX.md)** (This file)
   - **Purpose**: Index and reference for all build files
   - **Use**: Quick lookup of what each file does
   - **Size**: ~3 KB
   - **For**: Reference and navigation

### Configuration Files

5. **[requirements-build.txt](requirements-build.txt)**
   - **Purpose**: List of all build dependencies
   - **Use**: Install with `pip install -r requirements-build.txt`
   - **Size**: ~500 bytes
   - **Contains**: meson-python, Cython, NumPy, etc.
   - **For**: Dependency management

### Build Scripts

6. **[build_and_test.sh](build_and_test.sh)**
   - **Purpose**: Automated build and test script for Unix/Linux/macOS
   - **Use**: `./build_and_test.sh [options]`
   - **Size**: ~6 KB
   - **Features**: 
     - Automatic dependency checking
     - Clean build option
     - Configurable testing
     - Color-coded output
   - **Platform**: Linux, macOS, Unix

7. **[build_and_test.bat](build_and_test.bat)**
   - **Purpose**: Automated build and test script for Windows
   - **Use**: `build_and_test.bat [options]`
   - **Size**: ~6 KB
   - **Features**: Same as .sh version
   - **Platform**: Windows

### Test & Verification Scripts

8. **[verify_build.py](verify_build.py)**
   - **Purpose**: Comprehensive build verification
   - **Use**: `python verify_build.py`
   - **Size**: ~10 KB
   - **Tests**:
     - Import verification
     - DataFrame operations
     - I/O operations
     - GroupBy, merge, pivot
     - DateTime functionality
     - Missing data handling
     - And 10+ more test categories
   - **For**: Post-build verification

9. **[test_custom_build.py](test_custom_build.py)**
   - **Purpose**: Template for testing custom modifications
   - **Use**: `python test_custom_build.py`
   - **Size**: ~8 KB
   - **Features**:
     - Example tests for common operations
     - Template for custom tests
     - Performance testing examples
   - **For**: Developers making custom modifications

## 🗂️ File Organization

```
pandas/
├── BUILD_README.md              # Main overview
├── QUICK_START_BUILD.md         # Quick reference
├── BUILDING_FROM_SOURCE.md      # Comprehensive guide
├── BUILD_FILES_INDEX.md         # This file
├── requirements-build.txt       # Build dependencies
├── build_and_test.sh           # Unix build script
├── build_and_test.bat          # Windows build script
├── verify_build.py             # Verification tests
└── test_custom_build.py        # Custom test template
```

## 📊 File Dependency Map

```
User wants to build Pandas
         │
         ├─► Quick build? ──► QUICK_START_BUILD.md
         │                    └─► requirements-build.txt
         │                    └─► build_and_test.sh/.bat
         │
         ├─► Detailed guide? ──► BUILDING_FROM_SOURCE.md
         │                      └─► requirements-build.txt
         │                      └─► Manual build process
         │
         ├─► Automated? ──► build_and_test.sh (or .bat)
         │                 └─► Automatically uses requirements-build.txt
         │                 └─► Automatically runs verify_build.py
         │
         └─► Verify build? ──► verify_build.py
                              └─► test_custom_build.py (for custom mods)
```

## 🎯 Quick Reference Table

| Task | File(s) to Use | Command |
|------|---------------|---------|
| **First time building** | BUILDING_FROM_SOURCE.md | Read the guide |
| **Quick build** | QUICK_START_BUILD.md | Follow steps |
| **Automated build (Unix)** | build_and_test.sh | `./build_and_test.sh` |
| **Automated build (Windows)** | build_and_test.bat | `build_and_test.bat` |
| **Install dependencies** | requirements-build.txt | `pip install -r requirements-build.txt` |
| **Verify installation** | verify_build.py | `python verify_build.py` |
| **Test custom changes** | test_custom_build.py | `python test_custom_build.py` |
| **Troubleshooting** | BUILDING_FROM_SOURCE.md | See "Troubleshooting" section |
| **Overview of files** | BUILD_README.md | Read for full overview |

## 🔄 Typical Workflow

### For New Users

1. Read **BUILD_README.md** (3 min)
2. Read **BUILDING_FROM_SOURCE.md** (15-20 min)
3. Run `pip install -r requirements-build.txt` (2-5 min)
4. Build using instructions from guide (10-15 min)
5. Run `python verify_build.py` (1-2 min)

**Total time**: ~30-45 minutes

### For Experienced Users

1. Skim **QUICK_START_BUILD.md** (1 min)
2. Run `./build_and_test.sh` (10-15 min)
3. Done!

**Total time**: ~10-15 minutes

### For Automated Build

1. Run `./build_and_test.sh` or `build_and_test.bat`
2. Script handles everything automatically

**Total time**: ~10-15 minutes (unattended)

## 📝 File Descriptions by Use Case

### I want to understand the build process
→ Read **BUILDING_FROM_SOURCE.md**

### I want to build as fast as possible
→ Run **build_and_test.sh** (or .bat)

### I want a middle ground
→ Follow **QUICK_START_BUILD.md**

### I want to verify my build works
→ Run **verify_build.py**

### I made custom modifications
→ Customize and run **test_custom_build.py**

### I need to install dependencies
→ Use **requirements-build.txt**

### I want an overview of everything
→ Read **BUILD_README.md**

### I want to see what files exist
→ You're reading it! (**BUILD_FILES_INDEX.md**)

## 🛠️ Maintenance Notes

### Updating Build Dependencies

When build dependencies change, update:
- `requirements-build.txt` - Add/update package versions
- `BUILDING_FROM_SOURCE.md` - Update dependency section
- `build_and_test.sh` and `build_and_test.bat` - Update package checks

### Adding New Tests

When adding verification tests:
- Add to `verify_build.py` for core functionality
- Add examples to `test_custom_build.py` for new features
- Update `BUILDING_FROM_SOURCE.md` with test instructions

### Platform-Specific Updates

When updating build process:
- Update both `build_and_test.sh` AND `build_and_test.bat`
- Test on all platforms (Linux, macOS, Windows)
- Update documentation for all platforms

## 📚 Related Files (Already in Repository)

These files already exist in the Pandas repository and work with our build files:

- **pyproject.toml** - Project metadata and build system config
- **meson.build** - Meson build configuration
- **README.md** - Main Pandas README
- **setup.py** - Legacy setup file (deprecated, use meson-python)

## 🔗 External Resources

### Build System Documentation
- [Meson Build System](https://mesonbuild.com/)
- [meson-python](https://meson-python.readthedocs.io/)
- [Cython](https://cython.readthedocs.io/)

### Pandas Resources
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Contributing Guide](https://pandas.pydata.org/docs/dev/development/contributing.html)
- [GitHub Repository](https://github.com/pandas-dev/pandas)

## ✅ Checklist for Users

Before building, make sure you have:
- [ ] Python 3.11 or higher
- [ ] C/C++ compiler installed
- [ ] Read appropriate documentation
- [ ] Installed build dependencies
- [ ] ~2GB free disk space

After building, verify:
- [ ] Pandas imports successfully
- [ ] Version shows correctly
- [ ] Basic operations work
- [ ] Tests pass (run verify_build.py)

## 📞 Support

If you have issues:

1. **Check troubleshooting**: BUILDING_FROM_SOURCE.md has extensive troubleshooting
2. **Run verification**: `python verify_build.py` to identify issues
3. **Clean and rebuild**: `./build_and_test.sh --clean`
4. **Check documentation**: All guides have troubleshooting sections
5. **Ask community**: GitHub Issues, Stack Overflow, Slack

## 🎉 Summary

You now have **9 comprehensive files** to help you build Pandas from source:

- **4 documentation files** (guides and references)
- **1 configuration file** (dependencies)
- **2 build scripts** (automated building)
- **2 test scripts** (verification and custom tests)

Everything you need to successfully build, test, and verify Pandas from source! 🐼
