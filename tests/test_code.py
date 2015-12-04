from . import foo
from .. import bar
from ... import baz

import ...snurp

def blah(...):
    pass



class Foo(tuple):
    @staticmethod
    def __new__(cls, initialValue=(0,0)):
        return tuple.__new__(cls, initialValue)


class Bar(tuple):
    def __init__(self, initialValue=(0,0)):
        super(tuple, self).__init__(initialValue)
        super(tuple, self).count(items, stuff="thneed")

    @staticmethod
    def somefunc(arg, arrg=pirate):
        pass

    @property

list(map(str, range(100)))
[str(i) for i in range(100)]

sâomething(arg=22)

def sâomething():
    pass

class sâomething(object):
    pass

__init__(something)

list(map(str, range(100)))
#        ^^^ support.type.python
[str(i) for i in range(100)]
#^^^ support.function.builtin.call.python

super(arg1=1)(arg2=2)
list abs, map
some.None NotImplemented

print (file=None)
print __class__
print keyword
print __init__
print(foobar)

__init__ . something()

callback(print)
callback(range)

.__init__
__init__ [2]


@ deco . __init__ (call=some)  # rator
def function():
    pass

@classmethod
def from_foo(cls, foo):
    return cls(foo, bar='baz')
# highlighting for arguments broken


mod.func()
mod.submod.func()
func().func2().attr
mod.func().attr.attr2.func2()

range(foo, bar)
(...)

__exit__
print foobar
Привет_мир() or 我喜欢奶酪() or Kolbász_finom()

bool

class MyWarning(Warning):
    def __init__(self, text='first part'
                            'second part'):
        self.args = (text,)

    foo(text="line 1"
             "line 2")

foobar(param=r"()")


def f():
    print(r"()")

f()

def hi(name):
    r""" Say hi!
    with a \) special characters.
    """
    return 'hi ' + name

print(hi('avi'))
