# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
#tests = [ {'description': 'This test will run first.',
#    'steps': [ {'inputs': [('PINA',<val>)], 'iterations': 1 } ],
#    'expected': [('PORT',<val>)],
#    },
#    {'description': 'This test will run second.',
#    'steps': [ {'inputs': [('PIN', <val>)],'iterations': 1}, # Set PIN to val then run one iteration
#        {'inputs': [('PIN',<val>)], 'time': 300 }, # Set PIN to val then run 300 ms
#        {'inputs': [('PIN',<val>)], 'iterations': 1, 'expected': [('PORT',<val>)]}, 
#        {'inputs': [('PIN',<val>)], 'time': 600}, ],
#    'expected': [('PORT',<val>)],
#    },
#    ]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
#watch = ['<function>::<static-var>','PORTB']
tests = [ {'description': 'PINA: 0x01, 0x01, 0x02 => PORTC: 8, state: pressA1',
    'steps': [{'inputs': [('PINA', 0xFE)], 'iterations': 2},
        {'inputs': [('PINA', 0xFF)], 'iterations': 2},
        {'inputs': [('PINA', 0xFD)], 'iterations': 2}],
    'expected': [('PORTC',0x07)],
    },
    {'description': 'PINA: 0x00, 0x02, 0x00 => PORTC: 7, state: pressA1',
    'steps': [{'inputs': [('PINA', 0xFF)], 'iterations': 2},
        {'inputs': [('PINA', 0xFD)], 'iterations': 2},
        {'inputs': [('PINA', 0xFF)], 'iterations': 2}],
    'expected': [('PORTC',0x06)],
    },   
    {'description': 'PINA: 0x01, 0x02, 0x01 => PORTC: 8, state: pressA1',
    'steps': [{'inputs': [('PINA', 0xFD)], 'iterations': 2},
        {'inputs': [('PINA', 0xFD)], 'iterations': 2},
        {'inputs': [('PINA', 0xFD)], 'iterations': 2}],
    'expected': [('PORTC',0x05)],
    },   
    {'description': 'PINA: 0x02, 0x02, 0x02 => PORTC: 5, state: pressA1',
    'steps': [{'inputs': [('PINA', 0xFD)], 'iterations': 2},
        {'inputs': [('PINA', 0xFD)], 'iterations': 2},
        {'inputs': [('PINA', 0xFD)], 'iterations': 2}],
    'expected': [('PORTC',0x05)],
    },   
    {'description': 'PINA: 0x02, 0x02, 0x02 => PORTC: 2, state: pressA1',
    'steps': [{'inputs': [('PINA', 0xFC)], 'iterations': 2},
        {'inputs': [('PINA', 0xFF)], 'iterations': 2},
        {'inputs': [('PINA', 0xFD)], 'iterations': 2}],
    'expected': [('PORTC',0x00)],
    },
    
    {'description': 'PINA: 0x02, 0x02, 0x02 => PORTC: 0, state: pressA1',
    'steps': [{'inputs': [('PINA', 0xFF)], 'iterations': 2},
        {'inputs': [('PINA', 0xFE)], 'iterations': 2},
        {'inputs': [('PINA', 0xFE)], 'iterations': 2}],
    'expected': [('PORTC',0x01)],
    },

    
    {'description': 'PINA: 0x02, 0x02, 0x02 => PORTC: 0, state: pressA1',
    'steps': [{'inputs': [('PINA', 0xFF)], 'iterations': 2},
        {'inputs': [('PINA', 0xFE)], 'iterations': 2},
        {'inputs': [('PINA', 0xFE)], 'iterations': 2}],
    'expected': [('PORTC',0x02)],
    },
    
    {'description': 'PINA: 0x01, 0x01, 0x02 => PORTC: 1, state: pressA1',
    'steps': [{'inputs': [('PINA', 0xFF)], 'iterations': 2},
        {'inputs': [('PINA', 0xFE)], 'iterations': 2},
        {'inputs': [('PINA', 0xFF)], 'iterations': 2}],
    'expected': [('PORTC',0x03)],
    },

    {'description': 'PINA: 0x01, 0x01, 0x02 => PORTC: 9, state: pressA1',
    'steps': [{'inputs': [('PINA', 0xFE)], 'iterations': 2},
        {'inputs': [('PINA', 0xFF)], 'iterations': 2},
        {'inputs': [('PINA', 0xFE)], 'iterations': 2},
        {'inputs': [('PINA', 0xFF)], 'iterations': 2},
        {'inputs': [('PINA', 0xFE)], 'iterations': 2},
        {'inputs': [('PINA', 0xFF)], 'iterations': 2},
        {'inputs': [('PINA', 0xFE)], 'iterations': 2},
        {'inputs': [('PINA', 0xFF)], 'iterations': 2},
        {'inputs': [('PINA', 0xFE)], 'iterations': 2},
        {'inputs': [('PINA', 0xFF)], 'iterations': 2},
        {'inputs': [('PINA', 0xFE)], 'iterations': 2}],
    'expected': [('PORTC',0x09)],
    },    
    ]
