"""Lambda function that executes pyflakes, a static file linter."""
from lintipy import CheckRun


handle = CheckRun.as_handler('pyflakes', 'pyflakes', '.')
