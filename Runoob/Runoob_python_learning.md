# Ruboob Python Learning

## Basics

- Open the terminal of this program, and write `python3 hello.py` to run it.

- If the statement is very long, we can use a backslash `\` to split it into multiple lines.

  -  Within `[]`, `{}`, `()` , no need to use `\`.

- There are four types of numbers : `int`, `bool`, `float`, `complex`.

- `''` and `""` are the same.

- Triple quotes `'''` or `"""` can be used to specify a multiline string.

- `\` can be used for escaping, and using `r` prevents the backslash from being interpreted as an escape character.

  ```python
  r"this is a line with \n" 
  ```

  - The output would be `this is a line with \n`.

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