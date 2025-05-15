import subprocess

def compile_and_run(asm_path, bin_path):
    # Compile the .s file with nasm
    obj_path = asm_path.replace(".s", ".o")

    subprocess.run(["nasm", "-f", "elf64", asm_path, "-o", obj_path], check=True)
    # Link with ld
    subprocess.run(["ld", obj_path, "-o", bin_path], check=True)
    # Run the compiled binary
    subprocess.run([f"./{bin_path}"], check=True)

