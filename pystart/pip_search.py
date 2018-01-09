import pip
import sys
import re
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def pip_exact_search(name):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    pip.main(['search', name, '--disable-pip-version-check'])
    sys.stdout = old_stdout
    output = mystdout.getvalue()
    r = re.compile("^{} .*$".format(name), re.I | re.M).search(output)
    return r is not None
