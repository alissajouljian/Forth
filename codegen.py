import itertools

def generate_assembly(instructions, output_path):
    label_counter = itertools.count()
    asm = [
        "section .data",
        "    newline db 0xA, 0",
        "",
        "section .bss",
        "    stack resq 1024",
        "    vars resq 256",
        "",
        "section .text",
        "    global _start",
        "_start:",
        "    mov rbp, stack",
    ]

    stack = []
    vars = {}
    i = 0

    while i < len(instructions):
        token = instructions[i]

        if token.isdigit():
            asm.append(f"    mov rax, {token}")
            asm.append("    mov [rbp], rax")
            asm.append("    add rbp, 8")

        elif token == "+":
            asm.extend([
                "    sub rbp, 8",
                "    mov rbx, [rbp]",
                "    sub rbp, 8",
                "    mov rax, [rbp]",
                "    add rax, rbx",
                "    mov [rbp], rax",
                "    add rbp, 8"
            ])

        elif token == "-":
            asm.extend([
                "    sub rbp, 8",
                "    mov rbx, [rbp]",
                "    sub rbp, 8",
                "    mov rax, [rbp]",
                "    sub rax, rbx",
                "    mov [rbp], rax",
                "    add rbp, 8"
            ])

        elif token == "*":
            asm.extend([
                "    sub rbp, 8",
                "    mov rbx, [rbp]",
                "    sub rbp, 8",
                "    mov rax, [rbp]",
                "    imul rax, rbx",
                "    mov [rbp], rax",
                "    add rbp, 8"
            ])

        elif token == "/":
            asm.extend([
                "    sub rbp, 8",
                "    mov rbx, [rbp]",
                "    sub rbp, 8",
                "    mov rax, [rbp]",
                "    cqo",
                "    idiv rbx",
                "    mov [rbp], rax",
                "    add rbp, 8"
            ])

        elif token == ".":
            asm.extend([
                "    sub rbp, 8",
                "    mov rdi, [rbp]",
                "    call print_number"
            ])

        elif token == "VAR":
            var_name = instructions[i + 1]
            if var_name not in vars:
                vars[var_name] = len(vars) * 8
            i += 1

        elif token == '!':
            asm.extend([
                "    sub rbp, 8",
                "    mov rax, [rbp]",     # address
                "    sub rbp, 8",
                "    mov rbx, [rbp]",     # value
                "    mov [vars + rax], rbx"
            ])


        elif token == "@":
            asm.extend([
                "    sub rbp, 8",
                "    mov rbx, [rbp]",  # address offset
                "    mov rax, [vars + rbx]",
                "    mov [rbp], rax",
                "    add rbp, 8"
            ])

        elif token == "=":
            eq_label = f"label_{next(label_counter)}"
            end_label = f"label_{next(label_counter)}"
            asm.extend([
                "    sub rbp, 8",
                "    mov rbx, [rbp]",
                "    sub rbp, 8",
                "    mov rax, [rbp]",
                "    cmp rax, rbx",
                f"    jne {eq_label}",
                "    mov rax, 1",
                f"    jmp {end_label}",
                f"{eq_label}:",
                "    mov rax, 0",
                f"{end_label}:",
                "    mov [rbp], rax",
                "    add rbp, 8"
            ])

        elif token == "IF":
            false_label = f"label_{next(label_counter)}"
            stack.append(false_label)
            asm.extend([
                "    sub rbp, 8",
                "    mov rax, [rbp]",
                "    cmp rax, 0",
                f"    je {false_label}"
            ])

        elif token == "ELSE":
            end_label = f"label_{next(label_counter)}"
            false_label = stack.pop()
            stack.append(end_label)
            asm.extend([
                f"    jmp {end_label}",
                f"{false_label}:"
            ])

        elif token == "THEN":
            end_label = stack.pop()
            asm.append(f"{end_label}:")

        elif token == "BEGIN":
            loop_start = f"label_{next(label_counter)}"
            stack.append(loop_start)
            asm.append(f"{loop_start}:")

        elif token == "UNTIL":
            loop_start = stack.pop()
            asm.extend([
                "    sub rbp, 8",
                "    mov rax, [rbp]",
                "    cmp rax, 0",
                f"    je {loop_start}"
            ])

        elif token == "DO":
            start_label = f"label_{next(label_counter)}"
            end_label = f"label_{next(label_counter)}"
            stack.append((start_label, end_label))
            # Expect index and limit pushed before DO
            asm.extend([
                "    sub rbp, 8",
                "    mov rcx, [rbp]",  # limit
                "    sub rbp, 8",
                "    mov rdx, [rbp]",  # index
                f"{start_label}:"
            ])

        elif token == "LOOP":
            start_label, end_label = stack.pop()
            asm.extend([
                "    inc rdx",
                "    cmp rdx, rcx",
                f"    jl {start_label}",
                f"{end_label}:"
            ])

        elif token == "SQUARE":
            asm.extend([
                "    sub rbp, 8",
                "    mov rax, [rbp]",
                "    imul rax, rax",
                "    mov [rbp], rax",
                "    add rbp, 8"
            ])
        elif token in vars:
            offset = vars[token]
            asm.extend([
                f"    mov rax, {offset}",
                "    mov [rbp], rax",
                "    add rbp, 8"
            ])
        elif token.upper() == "SPACE":
             asm.append("    mov rax, 32")
             asm.append("    call print_char")


        i += 1

    asm.extend([
        "    mov rax, 60",
        "    xor rdi, rdi",
        "    syscall",
        "",
        "print_number:",
        "    mov rcx, 10",
        "    mov rsi, rsp",
        "    sub rsi, 32",
        "    mov rbx, rsi",
        ".print_loop:",
        "    xor rdx, rdx",
        "    div rcx",
        "    add dl, '0'",
        "    dec rsi",
        "    mov [rsi], dl",
        "    test rax, rax",
        "    jnz .print_loop",
        "    mov rax, 1",
        "    mov rdi, 1",
        "    mov rdx, rbx",
        "    sub rdx, rsi",
        "    mov rsi, rsi",
        "    syscall",
        "    ret",
        "print_char:",
        "    mov byte [rsp-1], al",
        "    mov rsi, rsp",
        "    sub rsi, 1",
        "    mov rdi, 1",
        "    mov rdx, 1",
        "    mov rax, 1",
        "    syscall",
        "    ret"

    ])

    with open(output_path, 'w') as f:
        f.write("\n".join(asm))

