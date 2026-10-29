"""PyBuilder configuration for the Lab 6 calculator."""

from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.distutils")

name = "calculator_Ali_Naji"
version = "0.1"
summary = "Lab 6 calculator with seven operations and unit tests"
author = "Ali Naji"
default_task = "publish"


@init
def initialize(project):
    project.set_property("dir_source_main_python", "src/main/python")
    # The lab uses test_*.py rather than PyBuilder's default *_tests.py.
    # Scan the test folder directly to avoid a package-name collision.
    project.set_property(
        "dir_source_unittest_python", "tests/unittest/calculator_Ali_Naji"
    )
    project.set_property("unittest_module_glob", "test_*")
