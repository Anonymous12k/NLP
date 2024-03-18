import re

class FOPCParser:
    def __init__(self):
        self.tokens = []
        self.pos = 0

    def parse(self, expression):
        self.tokens = re.findall(r'\(|\)|\w+|¬|∧|∨|→|∀|∃', expression)
        self.pos = 0
        return self.parse_expression()

    def parse_expression(self):
        token = self.tokens[self.pos]
        if token == '(':
            self.pos += 1
            left = self.parse_expression()
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_expression()
            self.pos += 1
            return (op, left, right)
        elif token == '∀' or token == '∃':
            quantifier = token
            var = self.tokens[self.pos + 1]
            self.pos += 2
            formula = self.parse_expression()
            return (quantifier, var, formula)
        else:
            return token

# Example usage
if __name__ == '__main__':
    parser = FOPCParser()
    expression = '(∀x(P(x)→Q(x)))'
    parsed_expression = parser.parse(expression)
    print(parsed_expression)
