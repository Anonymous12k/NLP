class FSA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.start_state = 'q0'
        self.accept_states = {'q2'}
        self.transitions = {
            ('q0', 'a'): 'q0',
            ('q0', 'b'): 'q1',
            ('q1', 'a'): 'q0',
            ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q0',
            ('q2', 'b'): 'q1'
        }
    
    def run(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            current_state = self.transitions.get((current_state, symbol), None)
            if current_state is None:
                return False
        return current_state in self.accept_states

# Create an instance of the FSA
fsa = FSA()

# Test the FSA
test_strings = ['aab', 'abb', 'abab', 'baab']
for test_string in test_strings:
    print(f"'{test_string}' is accepted: {fsa.run(test_string)}")
