
# FORTH Compiler

A simple FORTH compiler that converts FORTH source code into x86-64 assembly. This compiler supports basic arithmetic operations, stack manipulation, variable assignments, and conditional logic. The output assembly code can be assembled and linked to produce an executable.

## Features

* **Arithmetic Operations**: Supports `+`, `-`, `*`, `/`.
* **Stack Manipulation**: Operations like `dup`, `drop`, `swap`, and `over`.
* **Control Flow**: Implements conditional branching (`IF`, `ELSE`, `THEN`, `BEGIN`, `UNTIL`), and loops (`DO`, `LOOP`).
* **Variable Handling**: Supports dynamic variable storage with `VAR`, `!`, and `@`.
* **Assembly Output**: Generates x86-64 assembly code.

## Requirements

* **Python 3.7+**
* **NASM** (Netwide Assembler)
* **LD** (GNU Linker)

## How to Use

1. **Write FORTH code** in a `.forth` file.

2. **Run the compiler**:

   ```bash
   python3 main.py
   ```
## Example



```
: square dup * ;
5 square .
```

This code defines a word `square` that squares a number and prints the result. It outputs `25`.



