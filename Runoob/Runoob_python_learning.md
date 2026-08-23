# Ruboob Python Learning

## Basics

- Open the terminal of this program, and write `python3 hello.py` to run it.

- If the statement is very long, we can use a backslash `\` to split it into multiple lines.

  -  Within `[]`, `{}`, `()` , no need to use `\`.

- `''` and `""` are the same.

- Triple quotes `'''` or `"""` can be used to specify a multiline string.

  - Use `;` to separate sentences in one line, like `a = 0; b = 0`

- `\` can be used for escaping, and using `r` prevents the backslash from being interpreted as an escape character.

  - For example :`print(r"this is a line with \n")` output would be `this is a line with \n`.

- Strings can be concatenated using `+` and repeated using `*`.

- Strings support two indexing methods: from left to right starting at 0, and from right to left starting at -1.

- **Strings can't be changed.**

- There is no `char` type, a character is just a string of length 1.

- In string slicing `str[start:end]`, `start` is inclusive and `end` is exclusive.

  - `str[start:end:step]`, no `step` means `step = 1`.

- Statements such as `if`, `while`, `def`, and `class` begin with a keyword on the first line, which ends with`:`. The line or lines of code that follow constitute a code block. We refer to the first line together with the following code block as a clause.

- `print()` outputs with a newline.

  - To prevent this, you need to add `end=""` at the end of the arguments, such as :

    ```python
    print("Hello, world!", end = "")
    ```

- Use `import` or `from ... import` to import modules.

  - To import the wholel module : `import somemodule`
  - To import a single function from a module : `from somemodule import somefunction`
  - To import several functions from a module : `from somemodule import func1, func2, func3`
  - To import all functions in a module : `from somemodule import *`

### Basic data type

- **Variables themselves are untyped**, the type we speak of belongs to the object in memory, not the variable.
  - We can use `type()` to check the type of the variable.
- Allows multiple variable assignment at once, such as `a = b = c = 1` or `a, b, c = 1, 2, "runoob"`.
- There are 6 standard data types in Python 3 : Number, String, Bool (sometimes as part of int), List, Tuple, Set, Dictionary
  - Unchangable data type : Number, String, Bool, Tuple
  - Changable data type : List, Set, Dictionary

#### Number

- There are four types of numbers : `int`, `bool`, `float`, `complex`.
  - We can use `type()` to check the type, such as `print(type(a))`.
  - We can also use `isinstance()` to check, such as `isinstance(a, int)`, it will answer `True` or `False`.
  - The difference is that, `type()` doesn't recognize subclass relationships, but `isinstance()` does.
    - This is beyond what we've covered.
- There is only one integer type `int`, which is represented as a long integer.
- A variable can point to objects of different types through assignment.
- In mixed-type calculations, `int` is automatically converted to `float`.
- **`/` returns a float**, while `//` returns an integer (**floor** division).
- A complex number can be represented as `a + bj` or `complex(a, b)`.
  - Both the real part `a` and the imaginary part `b` are `float`.