import pytest

try:
    from datagen.generator.numbers import NumberGenerator
except ImportError:
    from ..datagen.generator.numbers import NumberGenerator

def test_generate():
    g = NumberGenerator()
    typVal = "bad"

    with pytest.raises(KeyError, message="Expecting KeyError", match="{0} is not a valid numeric type".format(typVal)):
        g.generate(typ=typVal)

