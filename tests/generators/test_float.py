import pytest

try:
    from datagen.generator import FloatGenerator
except ImportError:
    from ..datagen.generator import FloatGenerator


def test_type_str():
    with pytest.raises(TypeError, message="Expecting TypeError", match="Expected one of"):
        FloatGenerator("10")

def test_type_int():
    FloatGenerator(10)

def test_type_float():
    FloatGenerator(1000.5297)

def test_return_val1():
    g = FloatGenerator(10)
    assert isinstance(g.generate(), FloatGenerator._acceptableTypes)

def test_return_val2():
    g = FloatGenerator(10.55, 90089.5465)
    assert isinstance(g.generate(), FloatGenerator._acceptableTypes)

def test_range():
    minVal = FloatGenerator._minVal
    maxVal = 734567.9812
    g = FloatGenerator(minVal, maxVal)

    for x in range(1, 101):
        i = g.generate()
        assert i >= minVal and i <= maxVal

