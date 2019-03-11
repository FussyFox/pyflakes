"""Lambda function that executes pyflakes, a static file linter."""
import logging
import sys

from lintipy import CheckRun

root_logger = logging.getLogger('')
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(logging.StreamHandler(sys.stdout))


handle = CheckRun.as_handler('pyflakes', 'pyflakes', '.')
