"""
LAB 2 zadanie 3
Zaproponuj automat skończony rozpoznający język A = {axaya : x ∈ {b}∗, y ∈ {c}∗}. Napisz program
symulujący jego działanie. Umożliw podanie dowolnego wejścia (zgodnego z alfabetem).
"""


class StateMachine:
    def __init__(self, rules, nodes):
        self.state = None
        self.head = None
        self.tape = None
        self.rules = rules
        self.nodes = nodes

    def go_left(self):
        if self.head > 0:
            self.head -= 1

    def go_right(self):
        if self.head == len(self.tape) - 1:
            self.tape.append(' ')
            self.head += 1
        else:
            self.head += 1

    def display(self):
        print(self.tape[:self.head] + [self.state] + self.tape[self.head:])

    def run_machine(self, input_string):
        print('Starting machine for: ', input_string)
        self.tape = list(input_string)
        self.head = 0
        self.state = self.nodes[0]
        action = True

        while True:
            self.display()
            action = self.rules[self.state][self.tape[self.head]]
            if action['head'] == 'R':
                self.go_right()
            else:
                self.go_left()

            self.state = action['next']
            if self.state == 'qa':
                print(self.state, ' - accepted')
                break
            elif self.state == 'qr':
                print(self.state, ' - rejected')
                break


dict_rules = {
    'q0': {
        ' ': {
            'head': 'L',
            'next': 'qr'
        },
        'a': {
            'head': 'R',
            'next': 'q1'
        },
        'b': {
            'head': 'L',
            'next': 'qr'
        },
        'c': {
            'head': 'L',
            'next': 'qr'
        }
    },
    'q1': {
        'a': {
            'head': 'R',
            'next': 'q2'
        },
        'b': {
            'head': 'R',
            'next': 'q1'
        },
        'c': {
            'head': 'L',
            'next': 'qr'
        }
    },
    'q2': {
        'a': {
            'head': 'R',
            'next': 'q3'
        },
        'b': {
            'head': 'L',
            'next': 'qr'
        },
        'c': {
            'head': 'R',
            'next': 'q2'
        }
    },
    'q3': {
        ' ': {
            'head': 'R',
            'next': 'qa'
        },
        'a': {
            'head': 'L',
            'next': 'qr'
        },
        'b': {
            'head': 'L',
            'next': 'qr'
        },
        'c': {
            'head': 'L',
            'next': 'qr'
        }
    }
}
m = StateMachine(dict_rules, ['q0', 'q1', 'q2', 'q3'])

m.run_machine('aaa')
m.run_machine('abaa')
m.run_machine('abbacca')
m.run_machine('acaba')
