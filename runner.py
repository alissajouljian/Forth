import subprocess

def compile_and_run(asm_path, bin_path):
    obj_path = asm_path.replace(".asm", ".o")

    subprocess.run(["nasm", "-felf64", asm_path, "-o", obj_path], check=True)
    subprocess.run(["ld", "-o", bin_path, obj_path], check=True)
    print("\n--- Program Output ---")
    subprocess.run([f"./{bin_path}"])

