class PluralFiniteStateMachine:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.start_state = 'q0'
        self.accept_states = {'q2'}
        self.transitions = {
            ('q0', 's'): 'q1',
            ('q1', 'h'): 'q2',
            ('q1', 's'): 'q2',
            ('q1', 'x'): 'q2',
            ('q1', 'z'): 'q2',
            ('q1', 'y'): 'q2',
            ('q2', 'e'): 'q2'
        }

    def generate_plural(self, noun):
        current_state = self.start_state
        plural_form = noun
        for letter in noun[::-1]:  # Iterate over the noun in reverse
            current_state = self.transitions.get((current_state, letter), None)
            if current_state is None:
                break
            elif current_state in self.accept_states:
                plural_form += 'es' if letter in ['s', 'x', 'z', 'sh', 'ch'] else 's'
                break
        return plural_form

# Create an instance of the FSM
fsm = PluralFiniteStateMachine()

# Test the FSM
nouns = ['dog', 'cat', 'fox', 'bus', 'watch']
for noun in nouns:
    plural_form = fsm.generate_plural(noun)
    print(f"The plural of '{noun}' is '{plural_form}'")
