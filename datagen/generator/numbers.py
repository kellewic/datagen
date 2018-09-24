import six
import random

from .base import BaseGenerator

## Base class for numeric generators
class NumberGenerator(BaseGenerator):
    _minVal = -six.MAXSIZE - 1
    _maxVal = six.MAXSIZE

    ## Init object with min/max range
    def __init__(self, minVal=None, maxVal=None):
        if minVal is None:
            minVal = self.__class__._minVal

        if maxVal is None:
            maxVal = self.__class__._maxVal

        self.minVal = self._checkValue(minVal)
        self.maxVal = self._checkValue(maxVal)

    @classmethod
    def getMinValue(cls):
        return cls._minVal

    @classmethod
    def getMaxValue(cls):
        return cls._maxVal

    ## Generate number using min/max range
    def _gen_func(self):
        def g():
            return random.uniform(self.minVal, self.maxVal)
        return g


class IntGenerator(NumberGenerator):
    _acceptableArgs = six.integer_types
    _returnType = int

    if six.PY2: # pragma: no cover
        _returnType = long


class FloatGenerator(NumberGenerator):
    ## Allow ints and floats as arguments to avoid having to pass numbers like 10.0
    _acceptableArgs = six.integer_types + (float,)
    _returnType = float

