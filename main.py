from compiler import ForthInterpreter
import sys

def run_file(filename):
    with open(filename) as f:
        code = f.read()
    interp = ForthInterpreter()
    interp.run(code)

def repl():
    interp = ForthInterpreter()
    print("Welcome to miniFORTH. Type 'exit' to quit.")
    while True:
        try:
            line = input("> ")
            if line.strip() == "exit":
                break
            interp.run(line)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        repl()


