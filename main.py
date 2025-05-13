from lexer import tokenize
from parser import parse
from codegen import generate_assembly
from runner import compile_and_run

def main():
    with open("samples/test1.fth", "r") as f:
        source = f.read()

    tokens = tokenize(source)
    instructions = parse(tokens)
    generate_assembly(instructions, "output/program.asm")
    compile_and_run("output/program.asm", "output/program")

if __name__ == "__main__":
    main()

