section .data
    newline db 0xA, 0

section .bss
    stack resq 1024
    vars resq 256

section .text
    global _start
_start:
    mov rbp, stack
    mov rax, 10
    mov [rbp], rax
    add rbp, 8
    mov rax, 5
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    sub rbp, 8
    mov rax, [rbp]
    add rax, rbx
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rdi, [rbp]
    call print_number
    mov rax, 32
    call print_char
    mov rax, 20
    mov [rbp], rax
    add rbp, 8
    mov rax, 4
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    sub rbp, 8
    mov rax, [rbp]
    sub rax, rbx
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rdi, [rbp]
    call print_number
    mov rax, 32
    call print_char
    mov rax, 6
    mov [rbp], rax
    add rbp, 8
    mov rax, 3
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    sub rbp, 8
    mov rax, [rbp]
    imul rax, rbx
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rdi, [rbp]
    call print_number
    mov rax, 32
    call print_char
    mov rax, 20
    mov [rbp], rax
    add rbp, 8
    mov rax, 4
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    sub rbp, 8
    mov rax, [rbp]
    cqo
    idiv rbx
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rdi, [rbp]
    call print_number
    mov rax, 32
    call print_char
    mov rax, 10
    mov [rbp], rax
    add rbp, 8
    mov rax, 0
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rax, [rbp]
    sub rbp, 8
    mov rbx, [rbp]
    mov [vars + rax], rbx
    mov rax, 0
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    mov rax, [vars + rbx]
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rdi, [rbp]
    call print_number
    mov rax, 32
    call print_char
    mov rax, 5
    mov [rbp], rax
    add rbp, 8
    mov rax, 8
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rax, [rbp]
    sub rbp, 8
    mov rbx, [rbp]
    mov [vars + rax], rbx
    mov rax, 0
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    mov rax, [vars + rbx]
    mov [rbp], rax
    add rbp, 8
    mov rax, 8
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    mov rax, [vars + rbx]
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    sub rbp, 8
    mov rax, [rbp]
    add rax, rbx
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rdi, [rbp]
    call print_number
    mov rax, 32
    call print_char
    mov rax, 20
    mov [rbp], rax
    add rbp, 8
    mov rax, 16
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rax, [rbp]
    sub rbp, 8
    mov rbx, [rbp]
    mov [vars + rax], rbx
    mov rax, 16
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    mov rax, [vars + rbx]
    mov [rbp], rax
    add rbp, 8
    mov rax, 0
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    mov rax, [vars + rbx]
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    sub rbp, 8
    mov rax, [rbp]
    sub rax, rbx
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rdi, [rbp]
    call print_number
    mov rax, 32
    call print_char
    mov rax, 5
    mov [rbp], rax
    add rbp, 8
    mov rax, 24
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rax, [rbp]
    sub rbp, 8
    mov rbx, [rbp]
    mov [vars + rax], rbx
    mov rax, 24
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rbx, [rbp]
    mov rax, [vars + rbx]
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rax, [rbp]
    imul rax, rax
    mov [rbp], rax
    add rbp, 8
    sub rbp, 8
    mov rdi, [rbp]
    call print_number
    mov rax, 32
    call print_char
    mov rax, 60
    xor rdi, rdi
    syscall

print_number:
    mov rcx, 10
    mov rsi, rsp
    sub rsi, 32
    mov rbx, rsi
.print_loop:
    xor rdx, rdx
    div rcx
    add dl, '0'
    dec rsi
    mov [rsi], dl
    test rax, rax
    jnz .print_loop
    mov rax, 1
    mov rdi, 1
    mov rdx, rbx
    sub rdx, rsi
    mov rsi, rsi
    syscall
    ret
print_char:
    mov byte [rsp-1], al
    mov rsi, rsp
    sub rsi, 1
    mov rdi, 1
    mov rdx, 1
    mov rax, 1
    syscall
    ret