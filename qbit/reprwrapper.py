"""
   @copyright: 2020 by Pauli Rikula
   @license: MIT <http://www.opensource.org/licenses/mit-license.php>
"""
import functools


# Some dark python magic for the custom function representation.
# Hopefully not needed at the end and can be removed
class _reprwrapper(object):
    def __init__(self, repr, func):
        self._repr = repr
        self._func = func
        functools.update_wrapper(self, func)
    def __call__(self, *args, **kw):
        return self._func(*args, **kw)
    def __repr__(self):
        return self._repr(self._func)

def _withrepr(reprfun):
    def _wrap(func):
        return _reprwrapper(reprfun, func)
    return _wrap
