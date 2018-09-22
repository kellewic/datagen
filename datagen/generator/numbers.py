import six
import random, sys

## Base class for numeric generators
class NumberGenerator(object):
    _minVal = -six.MAXSIZE - 1
    _maxVal = six.MAXSIZE

    _intLabel = "int"
    _floatLabel = "float"

    ## Determine int type based on Python version
    if six.PY2:
        intType = long
    else:
        intType = int

    ## Map of type strings to type
    _vt = {_intLabel: intType, _floatLabel: float}

    ## Default types that can be processed
    _acceptableTypes = six.integer_types + (float,)


    ## Check that value is an acceptable type
    def _checkValue(self, value):
        if not isinstance(value, self.__class__._acceptableTypes):
            raise TypeError("Expected one of {0}, but got {1} instead".format(str(self.__class__._acceptableTypes), type(value)))

        return value


    ## Init object with min/max range
    def __init__(self, minVal=None, maxVal=None):
        if minVal is None:
            minVal = self.__class__._minVal

        if maxVal is None:
            maxVal = self.__class__._maxVal

        self.minVal = self._checkValue(minVal)
        self.maxVal = self._checkValue(maxVal)

    ## Generate number based on type using min.max range
    def generate(self, typ):
        vt = self._vt

        if typ not in vt:
            raise KeyError("{0} is not a valid numeric type".format(typ))

        return vt[typ](random.uniform(self.minVal, self.maxVal))


class IntGenerator(NumberGenerator):
    ## Override types to only allow integers
    _acceptableTypes = six.integer_types

    def generate(self):
        return super(self.__class__, self).generate(typ=self.__class__._intLabel)


class FloatGenerator(NumberGenerator):
    ## Use default types and allow integers so users don't have to pass arguments like 10.0

    def generate(self):
        return super(self.__class__, self).generate(typ=self.__class__._floatLabel)


