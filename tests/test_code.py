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


list(map(str, range(100)))
[str(i) for i in range(100)]

sâomething(arg=22)

def sâomething():
    pass

class sâomething(object):
    pass


list(map(str, range(100)))
[str(i) for i in range(100)]

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
