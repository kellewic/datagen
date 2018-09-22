from six import print_
from datagen.generator import IntGenerator, FloatGenerator

ig = IntGenerator(10)
fg = FloatGenerator(10, 20.9997)

print_(ig.generate())
print_(fg.generate())

