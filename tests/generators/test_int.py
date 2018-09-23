import pytest

try:
    from datagen.generator import IntGenerator
except ImportError:
    from ..datagen.generator import IntGenerator


def test_type_str():
    with pytest.raises(TypeError, message="Expecting TypeError", match="Expected one of"):
        IntGenerator("10")

def test_type_float():
    with pytest.raises(TypeError, message="Expecting TypeError", match="Expected one of"):
        IntGenerator(10.5)

def test_type_int():
    IntGenerator(10)

def test_return_val():
    g = IntGenerator(10)
    assert isinstance(g.generate(), IntGenerator._acceptableTypes)

def test_range():
    minVal = IntGenerator._minVal
    maxVal = 1546
    g = IntGenerator(minVal, maxVal)

    for x in range(1, 101):
        i = g.generate()
        assert i >= minVal and i <= maxVal

def test_init_no_args():
    minVal = IntGenerator._minVal
    maxVal = IntGenerator._maxVal
    g = IntGenerator()
    i = g.generate()
    assert i >= minVal and i <= maxVal

