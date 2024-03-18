class State:
    def __init__(self, rule, dot_position, start_position):
        self.rule = rule
        self.dot_position = dot_position
        self.start_position = start_position

    def __eq__(self, other):
        return self.rule == other.rule and self.dot_position == other.dot_position and self.start_position == other.start_position

    def __str__(self):
        return f"{self.rule[0]} -> {' '.join(self.rule[1][:self.dot_position])} . {' '.join(self.rule[1][self.dot_position:])}, {self.start_position}"

    def is_complete(self):
        return self.dot_position == len(self.rule[1])

    def next_symbol(self):
        if self.is_complete():
            return None
        return self.rule[1][self.dot_position]

class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string):
        chart = [[] for _ in range(len(input_string) + 1)]
        self.predict(0, chart)
        for i in range(len(input_string) + 1):
            self.scan(i, input_string, chart)
            self.complete(i, chart)
        return chart

    def predict(self, position, chart):
        for production in self.grammar:
            lhs, rhs = production
            if len(rhs) > 0 and rhs[0].isupper():
                chart[position].append(State(production, 0, position))

    def scan(self, position, input_string, chart):
        if position >= len(input_string):
            return
        for state in chart[position]:
            next_sym = state.next_symbol()
            if next_sym and next_sym == input_string[position]:
                chart[position + 1].append(State(state.rule, state.dot_position + 1, state.start_position))

    def complete(self, position, chart):
        for state in chart[position]:
            if not state.is_complete():
                continue
            for old_state in chart[state.start_position]:
                next_sym = old_state.next_symbol()
                if next_sym and next_sym == state.rule[0]:
                    chart[position].append(State(old_state.rule, old_state.dot_position + 1, old_state.start_position))

# Example grammar: S -> NP VP, NP -> Det N, VP -> V NP, Det -> 'the', N -> 'dog', V -> 'chased'
grammar = [
    ('S', ['NP', 'VP']),
    ('NP', ['Det', 'N']),
    ('VP', ['V', 'NP']),
    ('Det', ['the']),
    ('N', ['dog']),
    ('V', ['chased'])
]

earley_parser = EarleyParser(grammar)
input_string = 'the dog chased'
chart = earley_parser.parse(input_string.split())

# Check if the start symbol S is in the final chart entry
start_symbol = 'S'
if any(state.rule[0] == start_symbol and state.start_position == 0 and state.is_complete() for state in chart[-1]):
    print("Input string is accepted by the grammar.")
else:
    print("Input string is not accepted by the grammar.")
