from stack import Stack

class ForthInterpreter:
    def __init__(self):
        self.stack = Stack()
        self.words = {}
        self.builtins = {
            '+': self.add, '-': self.sub, '*': self.mul, '/': self.div,
            'dup': self.dup, 'drop': self.drop, 'swap': self.swap, 'over': self.over,
            '.': self.dot, '.S': self.print_stack,
        }

    def run(self, code):
        tokens = code.replace('\n', ' ').split()
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == ':':
                name = tokens[i+1]
                body = []
                i += 2
                while tokens[i] != ';':
                    body.append(tokens[i])
                    i += 1
                self.words[name] = body
            elif token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                self.stack.push(int(token))
            elif token in self.builtins:
                self.builtins[token]()
            elif token in self.words:
                self.run(' '.join(self.words[token]))
            else:
                raise Exception(f"Unknown word: {token}")
            i += 1

    def add(self): self.stack.push(self.stack.pop() + self.stack.pop())
    def sub(self): a, b = self.stack.pop(), self.stack.pop(); self.stack.push(b - a)
    def mul(self): self.stack.push(self.stack.pop() * self.stack.pop())
    def div(self): a, b = self.stack.pop(), self.stack.pop(); self.stack.push(b // a)

    def dup(self): val = self.stack.peek(); self.stack.push(val)
    def drop(self): self.stack.pop()
    def swap(self): a, b = self.stack.pop(), self.stack.pop(); self.stack.push(a); self.stack.push(b)
    def over(self): a = self.stack.pop(); b = self.stack.peek(); self.stack.push(a); self.stack.push(b)

    def dot(self): print(self.stack.pop())
    def print_stack(self): print("Stack:", self.stack.items)


