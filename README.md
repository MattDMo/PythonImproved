# ***NOTE:***
Because of reasons, I haven't been able to devote ~~much of~~ any time to supporting and maintaining my open source projects since late 2016. I'm not dead :skull:, dying :mask:, in prison :oncoming_police_car:, in exile :no_entry:, in space :alien:, hiding under a rock :mountain:, boycotting the interwebs :no_entry_sign: :computer:, or anything like that; life has just... been very busy :weary:. Hopefully I'll have more time for nerding in the not-too-distant future, but until then my development work will just have to remain more or less on hold, as unfortunately it doesn't pay any bills, provide any food, take care of my kids, or keep my car on the road. Of course, if anyone would like to donate to the cause, the link is below :moneybag:

All the best,

Matt

---

# Python Improved

A better Python `.tmLanguage` syntax highlighting definition for [Sublime Text](http://www.sublimetext.com) and [TextMate](http://www.macromates.com). It includes support for both Python 2 and Python 3, and unlike any other Python syntax definition now fully supports Unicode identifiers anywhere in your code! It also provides its own improved regex syntax definition for inline highlighting of raw string literals.

Inspired by:

- the original TextMate and Sublime Text `Python.tmLanguage` files
- facelessuser's [Better Python](https://github.com/facelessuser/sublime-languages)
- Peter Varo's [Python 3](https://github.com/petervaro/python) syntax definition

as well as a number of my own changes to make things more consistent and understandable. For customized syntax highlighting taking advantage of all the new scopes, use **PythonImproved** with the [Neon Color Scheme](https://packagecontrol.io/packages/Neon%20Color%20Scheme), or modify your own favorite color scheme with the scopes below.

## Installation and Use

If you haven't already, [install Package Control](https://packagecontrol.io/installation), then select `Python Improved` from the `Package Control: Install Package` option in the Command Palette. To use PythonImproved as your default Python syntax, open a `.py` file, then select **`View -> Syntax -> Open all with current extension as... -> PythonImproved`**.

While I haven't yet tried to install PythonImproved with TextMate, I can't think of a good reason as to why it wouldn't work. You could try putting it in the same directory as the standard `Python.tmbundle` package, in the `Syntaxes` subdirectory. Then, just pick `PythonImproved` from the syntax menu.

## New/Changed Scopes

If you prefer to modify your own color scheme, here is a list of new/modified scopes, along with some examples. It's not perfectly complete, but it's a start.

- `support.ipython.in` and `support.ipython.out`: [IPython](http://ipython.org) `In [1]:`/`Out [1]:` fields &mdash; designed for use with [SublimeREPL](https://packagecontrol.io/packages/SublimeREPL). The cell number can be themed with a different color using `support.ipython.cell-number`.
- `constant.numeric.integer.(long).binary.python`: binary literals `0b00101010`, `0b00101010L`
- `keyword.control.import.python` now contains `import`, `from`, _and_ `as`
- `support.type.exception.python` now matches any identifier that ends with `Exception` or `Error`, not just the built-in ones like `IndentationError` or `RuntimeException`, allowing for the highlighting of custom exceptions such as those included in third-party modules.
- [Function annotation](http://www.python.org/dev/peps/pep-3107/) support for Python 3, thanks to [@facelessuser](https://github.com/facelessuser).  New scopes added: `punctuation.separator.annotation.python`, `punctuation.separator.annotation.result.python`, `punctuation.definition.parameters-group.begin.python`, and `punctuation.definition.parameters-group.end.python`.
- You can now have comments in multi-line function definitions:

```python
def myfunc(self,            # gotta have self
           param1="value",  # values are cool
           param2=True,     # or False, whatever
           *args,           # I'm here for an argument
           **kwargs):       # you never know
```

![Multi-line comments and function annotations](http://pigimal.com/img/github/python_annotations.png)

- New scopes for bytes, unicode, and raw/regex strings, thanks to [@simonzack](https://github.com/simonzack): `string.quoted.(single|double).(block|single-line).(bytes|bytes-raw|bytes-raw-regex).python`
- Also from @simonzack, highlighting of `self|cls` in parameter strings: `variable.parameter.function.(keyword|language)`
- `comment.line.note.python` is a comment line that contains `(BUG|FIXME|TODO|XXX)` at the beginning. `comment.line.note.notation.python` matches the actual word itself, so you can differentially highlight the word and the whole line:

![BUG FIXME TODO XXX line highlighting](http://pigimal.com/img/comment.line.note.png)

- `constant.other.allcaps.python` captures variable names that are in all caps (`OPENING_PORT`, for example), assuming the convention that these are generally treated as constants in the code. Matches `CONSTANT`, `class.CONSTANT` and the `CONSTANT` part of `CLASS.CONSTANT`, but not `CLASS.function()`, `class.FUNCTION()`, or `FUNCTION()`.
- Fixed the octal integers so the Python 3-style `0o123` is matched as well as the old-style `0123`
- Built-in functions like `any()`, `dict()`, `len()`, `raw_input()`, etc. now have their arguments highlighted just like any other function. Many thanks to [@facelessuser](https://github.com/facelessuser) for the regex, and [@FichteFoll](https://github.com/FichteFoll) for valuable discussion. For those working with Python 2, `print` is still a standalone keyword (as are `assert` and `del`).
- `support.function.magic` and `support.function.builtin` have now been split in two &mdash; `name` and `call`, so that `__init__` (`support.function.magic.name.python`), for example, can be themed differently than `__init__()` (`support.function.magic.call.python`).
- Relatedly, magic function names (and calls), also known as the "dunder" methods for being surrounded by double underscores, have been collated from the [2.7](https://docs.python.org/2/reference/datamodel.html) and [3.5](https://docs.python.org/3/reference/datamodel.html) Data Model docs and cleaned up so that as much as possible is included there, but outdated or incorrect things are not. The same is true of the magic variables (`support.variable.magic`).
- `support.type` now contains *only* what's defined in https://docs.python.org/X/library/functions.html and stdtypes.html (where `X` is `2` or `3`) *where the item is a class*. They are highlighted as such only if not followed by an opening parenthesis &mdash; if it is, it's highlighted as `support.function.builtin.call`. This addresses [#16](https://github.com/MattDMo/PythonImproved/issues/16).
- Defined escaped characters (like `\n`, `\'`, `\\`, etc.) are now individually named as `constant.character.escape.*`, where `*` is `newline`, `single-quote`, `backslash`, etc.
- And probably some more stuff I forgot about...


## Notes

- To facilitate hacking, I'm also including my `.YAML-tmLanguage` file in the repo, which I use for my day-to-day work (I really hate debugging regexes embedded in XML). Install [`PackageDev`](https://packagecontrol.io/packages/PackageDev) for syntax highlighting, and tools for converting between YAML, JSON, and XML/Plist formats. [Neon](https://packagecontrol.io/packages/Neon%20Color%20Scheme) of course has great coloring for the `.YAML-tmLanguage` format, and especially the regexes :)
- Speaking of which, for raw/regex strings, regexes will be scoped according to the accompanying `Regular Expressions (Python Improved).tmLanguage` file, instead of the builtin Python regular expressions definition. If you're using **Neon** for syntax highlighting (or any color scheme that highlights regexes), use a lowercase `r` to denote your string as containing a regex (i.e., `r"\b(?i:(0[o]?[0-7]+))"`). However, if you're just using a raw string literal to, for example, define a Windows path and you *don't* want regex highlighing for all the back slashes and whatnot, use an uppercase `R` (`R"C:\Users\MattDMo"`). Python can't tell the difference, but it will look nicer in your editor.
- All Django-related stuff has been removed. If you want it back, just dig through the repo's history and you can find it. It was just too distracting.
- I removed the SQL-related stuff from the string definitions, because 1) somebody complained, and 2) like Django, it was distracting. It didn't cover all of SQL, only highlighted some keywords, and just wasn't worth it.
- Unicode escapes should now appear correctly in all strings, as with Python 3 all strings are Unicode. I think I got it right, if you think otherwise just let me know.
- I've begun working on correctly highlighting all the various elements of the new-style string formatting mini-language, but I haven't applied it to the most recent release while I work out the kinks. Feel free to [join the discussion](https://github.com/MattDMo/PythonImproved/issues/38).
- Now that the [ST3 public beta](https://sublimetext.com/3) supports `.sublime-syntax` files, I'm going to begin transitioning PI over to that format. If you'd like to contribute, chime in on [this issue](https://github.com/MattDMo/PythonImproved/issues/54). One major advantage will be fixing [this bug](https://github.com/MattDMo/PythonImproved/issues/34) with raw string literals.

## Issues

If you have questions, concerns, or suggested improvements, I'd love to hear from you! Feel free to [open an issue](https://github.com/MattDMo/PythonImproved/issues/new) or send a [pull request](https://github.com/MattDMo/PythonImproved/compare/) and I'll get back to you as soon as I can. You can also email me at <mattdmo@mattdmo.com> or find me on Twitter [@MattDMo](https://twitter.com/MattDMo).


## License

&copy; 2013-2018 Matt Morrison <mattdmo@mattdmo.com>.

This is free software. It is licensed under the [MIT License](http://opensource.org/licenses/MIT). Feel free to use this in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and distribute your work under this or a similar license. A shout-out or a beer would be appreciated.

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=R97MGGYES6GAJ&lc=US&item_name=Matthew%20D%2e%20Morrison&item_number=PythonImproved&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif" border="0" name="Donate" alt="PayPal - The safer, easier way to pay online!"></a>
<p>
You can also give on [Gratipay](https://www.gratipay.com/on/github/MattDMo/).
