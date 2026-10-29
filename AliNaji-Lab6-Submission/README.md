# Lab 6 calculator using PyBuilder

Exercise 1 implements a calculator and automates unit testing and packaging with
PyBuilder. The project and Python package are named `calculator_Ali_Naji`.
Exercise 2 (Makefile) is optional and is not included.

## Calculator operations

`src/main/python/calculator_Ali_Naji/__init__.py` provides:

- `add(x, y)`: addition.
- `subtract(x, y)`: subtraction.
- `multiply(x, y)`: multiplication.
- `divide(x, y)`: division; raises `ValueError` for a zero divisor.
- `modulus(x, y)`: Python remainder (`%`); raises `ValueError` for a zero divisor.
- `power(x, y)`: exponentiation (`**`).
- `square_root(x)`: real square root; raises `ValueError` for a negative input.

For modulus, the result follows Python's sign convention: `-10 % 3 == 2` and
`10 % -3 == -2`. The test suite contains 25 tests for normal inputs, decimals,
negative values, zero, and the specified error cases.

## Setup on a new computer

Install Python 3.10 or newer. Open PowerShell in this project directory, then run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\pyb.exe run_unit_tests
.\.venv\Scripts\pyb.exe
```

These commands use the virtual environment directly and do not require changing
PowerShell's execution policy. On macOS/Linux, use `.venv/bin/python` and
`.venv/bin/pyb` instead of the Windows paths.

## How the build works

`build.py` loads `python.core`, `python.unittest`, and `python.distutils`.
It declares the project name, version `0.1`, and default task `publish`.
PyBuilder prepares its isolated build environments and required plugin tools.
`run_unit_tests` discovers and executes the calculator tests. The default build
also tests the code, copies the source into `target/dist`, and creates a source
archive and wheel locally. It does not upload anything to a package registry.

The test directory is explicitly configured as
`tests/unittest/calculator_Ali_Naji`, and `unittest_module_glob` is `test_*`.
This preserves the handout's layout and filename while enabling PyBuilder to
discover the tests. Pointing directly at that folder avoids a name collision
between the calculator source package and the test package.

The tests can also be run with the handout's standard Python command:

```powershell
python -m unittest tests.unittest.calculator_Ali_Naji.test_calculator_Ali_Naji -v
```

Generated reports are under `target/reports`; the packaged calculator is under
`target/dist`. Virtual environments, caches, and generated directories can be
recreated and do not need to be submitted with the source project.

## Verified results

Both `pyb run_unit_tests` and the default `pyb` build completed with
`BUILD SUCCESSFUL`, 25 passing tests, and no errors or failures. The default
build created a source archive and wheel and passed its Twine artifact check.
The wheel was also imported separately and all seven operations were checked.
Copies of the wheel and source archive are in `artifacts`; build logs and test
reports are in `evidence`.

## Reference

PyBuilder plugin documentation: https://pybuilder.io/documentation/plugins
