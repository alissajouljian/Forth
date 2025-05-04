# FORTH Compiler

A lightweight FORTH interpreter implemented in Python. This project was created as a final project for the **Advanced Programming Languages** course, and it supports a subset of the FORTH language, including stack operations, arithmetic, and user-defined words.

## 📁 Project Structure

```

forth-compiler/
├── main.py                  # Entry point (REPL or file runner)
├── compiler.py              # Interpreter logic
├── stack.py                 # Stack implementation
├── examples/
│   └── hello.fs             # Sample FORTH program
└── tests/
└── test\_core.py         # Unit tests

````

---

## ▶️ Usage

### 1. Run a FORTH file

```bash
python3 main.py examples/hello.fs
````

### 2. Use REPL (interactive mode)

```bash
python3 main.py
```

Then type FORTH code directly:

```
> 2 3 + .
5
> : square dup * ; 
> 4 square .
16
> exit
```

---

## 🧪 Run Tests

Make sure everything is working:

```bash
python3 -m unittest discover tests
```

You should see:

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

---

## 📜 Features

✅ Arithmetic operations: `+ - * /`
✅ Stack operations: `dup drop swap over`
✅ Word definitions: `: name ... ;`
✅ Output: `.` and `.S`
🚧 Note: `emit` is not yet implemented in core interpreter, but used in example.

---

## 📂 Example Program: `hello.fs`

```forth
: hello
  72 emit 101 emit 108 emit 108 emit 111 emit
  44 emit 32 emit
  87 emit 111 emit 114 emit 108 emit 100 emit 33 emit ;

hello
```



