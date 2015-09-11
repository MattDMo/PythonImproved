# SYNTAX TEST "Packages/PythonImproved/PythonImproved.tmLanguage"
# <- source.python comment

# ident/dotted-name stuff and function calls
list(map(str, range(100)))
# ^ meta.dotted-name support.type
#     ^ meta.dotted-name support.function.builtin
#        ^ meta.dotted-name support.type
#              ^ meta.dotted-name support.function.builtin
#                    ^ meta.function-call meta.function-call.arguments meta.function-call meta.function-call.arguments meta.function-call meta.function-call.arguments constant.numeric.integer.decimal

[str(i) for i in range(100)]
# ^ meta.dotted-name support.type
#    ^ meta.dotted-name meta.generic-name
#                ^ support.function.builtin

super(arg1=1)(arg2=2)
# ^ meta.dotted-name support.type
#      ^ variable.parameter.function.keyword
#              ^ variable.parameter.function.keyword

list, abs, map, some.map
# ^ meta.dotted-name support.type
#     ^ meta.dotted-name support.function.builtin
#          ^ meta.dotted-name support.function.builtin
#               ^ meta.dotted-name meta.generic-name
#                   ^ meta.dotted-name meta.dot - meta.generic-name
#                    ^ meta.dotted-name meta.generic-name

True, None, False, NotImplemented
# ^ constant.language
#     ^ constant.language
#           ^ constant.language
#                  ^ constant.language

some.Ellipsis, other.NotImplemented  # must be root element
# ^ -constant.language
#    ^ -constant.language
#              ^ -constant.language
#                    ^ -constant.language


__init__ . something(arg=22)
# ^ meta.function-call meta.dotted-name support.function.magic
#        ^ meta.dotted-name meta.dot
#          ^ meta.dotted-name meta.generic-name
__init__ [2]
# ^ meta.item-access meta.dotted-name support.function.magic
super().__init__[2]
#      ^ meta.dotted-name meta.dot
#       ^ meta.dotted-name support.function.magic
ident = (value.dotted
#            ^ meta.dotted-name meta.generic-name
#             ^ meta.dotted-name meta.dot
#              ^ meta.dotted-name meta.generic-name
         .__init__)
#        ^ meta.dotted-name meta.dot
#           ^ meta.dotted-name support.function.magic


some.Error  # should match entire line, by design
y.s.e.SomeException



# "print" keyword vs statement
print (file=None)
# ^ meta.function-call meta.dotted-name support.function.builtin
# ^ meta.function-call meta.dotted-name support.function.builtin
#      ^ meta.function-call meta.function-call.arguments variable.parameter.function.keyword

print . __class__
# ^ meta.dotted-name support.function.builtin
#     ^ meta.dotted-name meta.dot
#         ^ meta.dotted-name support.variable.magic

print keyword
# ^ keyword.other.print

print __init__
# ^ keyword.other.print
#     ^ support.function.magic

callback(print, print , print
#        ^ support.function.builtin
#               ^ support.function.builtin
#                       ^ support.function.builtin
         ,
         print)
#        ^ support.function.builtin

# ALL_CAPS constants
CONSTANT
# ^ constant.other.allcaps
dotted.CONSTANT
# ^ -constant.other.allcaps
#      ^ constant.other.allcaps
constant.after().FUNCTION
#            ^ -constant.other.allcaps
#                ^ constant.other.allcaps
CONSTANT[1]
#  ^ constant.other.allcaps

# in theory, these could be constants as well, but they are not highlighted
# for now (they prolly should)
CONSTANT()
CONSTANT.s


# functions
def func(var1,
         # <- variable.parameter.function
         # comment
         # <- comment
         var2=123):
         # <- variable.parameter.function
    pass


# classes
class Demo(
        Base Fun):
        # <- entity.other.inherited-class
    pass


# decorators
@ deco . __init__ (call=some)  # rator
# <- meta.function.decorator-call entity.name.function.decorator punctuation.definition.decorator
#  ^ entity.name.function.decorator meta.dotted-name meta.generic-name
#      ^ entity.name.function.decorator meta.dotted-name meta.dot
#        ^ entity.name.function.decorator meta.dotted-name support.function.magic
#                  ^ meta.function.decorator.arguments variable.parameter.function.keyword
def function():
    pass


@normal.decorator
# <- meta.function.decorator entity.name.function.decorator punctuation.definition.decorator
#  ^ entity.name.function.decorator meta.dotted-name meta.generic-name
class Class():

    @wraps(method, 12)# comment
#    ^ entity.name.function.decorator meta.dotted-name meta.generic-name
#                  ^ meta.function.decorator.arguments constant
#                     ^ comment
    def wrapper(self):
        (self, __class__)
        pass


# imports
from . import sublimerepl_build_system_hack  # this is legit
#        ^ -invalid.illegal.name
from .s. import repl  # but this is invalid
#     ^ meta.dotted-name meta.generic-name
#        ^ meta.dotted-name invalid.illegal.name
from a import s as b
# ^ keyword.control.import
#       ^ keyword.control.import
#               ^ keyword.control.import


# unicode
ccesŝ[2]
#   ^ meta.item-access meta.dotted-name meta.generic-name
sômething(arg=22)
#   ^ meta.function-call meta.dotted-name meta.generic-name


@dêco(func=call)
# ^ meta.function.decorator-call meta.dotted-name meta.generic-name
def sômething():
#    ^ entity.name.function meta.generic-name
    pass
