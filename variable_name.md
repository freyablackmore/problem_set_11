# Q1: Variable name via functional programming (30 marks)


---

## Background information

In this question, you are asked to solve the problem set 4 "variable name" question again, but this time you are required to solve it using "functional programming" tools we introduced in this course.

Recall that a valid variable name in Python needs to be non-empty and satisfy the following rules:
1. It must be composed of letters (`a-zA-Z`), digits (`0-9`) and/or underscore `_` (see remark)
2. It cannot start with a digit
3. It must not be one of the Python keywords: `['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']`

In this course, we further impose the following rules:

4. No mixing case (letters are either all lowercase for variables that are supposed to vary, or all uppercase for variables that are supposed to be constants)
5. Meaningful names

While it is difficult to check rule 5 ("meaningful" is situational-wise), it is possible to check other rules by a program.

---

## Instructions

In [src/variable_name.py](src/variable_name.py), define a function `is_valid_variable_name()` to take _any_ `str` as an argument and return `bool` for which it represents whether the given string satisfies the first 4 rules.

**Please read the "Requirements" section and ensure your implementation fulfils the specific requirements of this question. You are unlikely to get a good mark if your submission does not fulfil the requirements (even if it provides the right outcome).**

---

## Requirements

Your implementation must fulfil the following requirements:
* Any functions written must be pure functions
* No change in variable value or modification of objects
* Must make use of at least one of the following appropriately:
    * `map()`
    * `filter()`
    * `functools.reduce()`

  and also make use of at least one anonymous lambda function (a function with no name) as an argument for at least one of them
* Only the following can be used:
    * Built-in functions
        * `ord()`
        * `len()`
        * `map()`
        * `filter()`
    * Basics like:
        * assignment and conditional statements
        * comparison (e.g. `==`, `<=`) and logical operators (`and`, `or`, `not`)
        * built-in types and data structures covered in the course
        * indexing and slicing
        * membership checking with the use of `in` and `not in`
    * Functions available from the modules from the Python standard library:
        * `reduce()` from `functools`
  
  If you want to use any other functionality, please consult the lecturer to avoid penalty.
* The following cannot be used:
    * Loops, list comprehension or dictionary comprehension
    * String methods like `isdigit()`, `isalpha()`, etc
* You can reuse and/or update the function definitions you have written for problem set 4, or the solution of problem set 4. If you do so, ensure your final submission fulfils the requirements above

---

## Note

* You may find the question quite artificial in the sense that there are quite a lot of restrictions, and some of them are not very natural
    * The question is designed to assess students' ability to apply some specific "functional programming" tools we covered in the course, and therefore students are restricted to a limited set of functionalities to use
* In the problem set 4 solution, quite a few evaluations are "short-circuit" in the sense that the checks will stop once we find out the answer. For example, if the first character is already invalid, we know immediately the given string cannot be a valid variable name, so we do not need to check the rest of the string
  * However, you may find that difficult to do the same with the limited set of functions you can use. **Therefore, you will not be penalised if there are some unnecessary calculations due to the unavailability of some tools to write short-circuit evaluations**

---

## Remark
* Note that Python actually accepts some other characters like Γ, but we do not accept them in this course (so as this question)