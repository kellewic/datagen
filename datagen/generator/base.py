from abc import ABCMeta, abstractmethod
import six

@six.add_metaclass(ABCMeta)
class BaseGenerator(object):
    ## Data types allowed as arguments to contructor
    _acceptableArgs = ()

    ## Data type the generator returns
    _returnType = None

    ## Check that value is an acceptable argument type
    def _checkValue(self, value):
        if not isinstance(value, self.getAcceptableArgs()):
            raise TypeError("Expected one of {0}, but got {1} instead".format(str(self.getAcceptableArgs()), type(value)))

        return value

    ## Generator callback-producing function
    @abstractmethod
    def _gen_func(self): # pragma: no cover
        raise NotImplementedError

    ## Generate data based on sub-class generator callback
    def generate(self):
        rt = self.getReturnType()
        cb = self._gen_func()
        return rt(cb())

    ## Return class acceptable argument types
    def getAcceptableArgs(self):
        return self.__class__._acceptableArgs

    ## Return class return type
    def getReturnType(self):
        return self.__class__._returnType

