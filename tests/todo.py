

# ####################### #
# DOES NOT WORK CORRECTLY #
# ####################### #

except AnError as b:  # <- should be keyword.other
    pass
with open() as c:  # <- should be keyword.other
    pass
yield from something()  # <- should be keyword.control.flow
raise AnError() from e  # <- should be keyword.other ?

some.False  # 'False' should be invalid


def func(var='multi'
             'line'):
    pass


@ deco [2]  # no item access match
def funct‍ion():
    pass


super().__init__[2]  # [2] currently matched as list and not item-access

# inline sql string (needs .sublime-syntax)
'INSERT INTO a table INT -- inline comment\n'
'continuation?'
