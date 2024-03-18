class Grammar:
    def __init__(self, productions):
        self.productions = productions

    def get_productions_for_lhs(self, lhs):
        return [prod for prod in self.productions if prod[0] == lhs]

def parse(grammar, input_string):
    def parse_nonterminal(nonterminal, remaining_input):
        productions = grammar.get_productions_for_lhs(nonterminal)
        for production in productions:
            if len(production) == 2:  # E.g., A -> BC
                B, C = production[1]
                for i in range(len(remaining_input) + 1):
                    if parse_nonterminal(B, remaining_input[:i]) and parse_nonterminal(C, remaining_input[i:]):
                        return True
            elif len(production) == 1 and production[0] == '':  # Epsilon production
                return True
            elif production[0] == remaining_input[0]:
                return True
        return False

    start_symbol = grammar.productions[0][0]
    return parse_nonterminal(start_symbol, input_string)

# Example Grammar: S -> AB | BC, A -> a, B -> b, C -> c
productions = [
    ('S', [('A', 'B'), ('B', 'C')]),
    ('A', [('a',)]),
    ('B', [('b',)]),
    ('C', [('c',)])
]
grammar = Grammar(productions)

# Example Input String
input_string = 'abbc'

# Parsing
if parse(grammar, input_string):
    print("Input string is accepted by the grammar.")
else:
    print("Input string is not accepted by the grammar.")
