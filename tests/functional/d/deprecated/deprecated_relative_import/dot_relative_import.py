# pylint: disable=import-error, missing-module-docstring, unused-import

# from import of stdlib optparse which should yield deprecated-module error
from optparse import OptionParser # [deprecated-module]
# from import of module internal optparse module inside this package.
# This should not yield deprecated-module error
from .optparse import Bar
