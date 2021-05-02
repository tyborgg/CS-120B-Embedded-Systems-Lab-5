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
tests = [ {'description': 'Test 0',
    'steps': [ {'inputs': [('PINA',0xFF)], 'iterations': 5 }],
    'expected': [('PORTC',0x00)],
    },  
    {'description': 'Test 1',
    'steps': [ {'inputs': [('PINA',0xFE)], 'iterations': 5 }],
    'expected': [('PORTC',0x60)],
    }, 
    {'description': 'Test 2',
    'steps': [ {'inputs': [('PINA',0xFD)], 'iterations': 5 }],
    'expected': [('PORTC',0x60)],
    },
    {'description': 'Test 3',
    'steps': [ {'inputs': [('PINA',0xFC)], 'iterations': 5 }],
    'expected': [('PORTC',0x70)],
    },
    {'description': 'Test 4',
    'steps': [ {'inputs': [('PINA',0xFB)], 'iterations': 5 }],
    'expected': [('PORTC',0x70)],
    },   
    {'description': 'Test 5',
    'steps': [ {'inputs': [('PINA',0xFA)], 'iterations': 5 }],
    'expected': [('PORTC',0x38)],
    },
    {'description': 'Test 6',
    'steps': [ {'inputs': [('PINA',0xF9)], 'iterations': 5 }],
    'expected': [('PORTC',0x38)],
    },   
    {'description': 'Test 7',
    'steps': [ {'inputs': [('PINA',0x0F8)], 'iterations': 5 }],
    'expected': [('PORTC',0x3C)],
    },
    {'description': 'Test 8',
    'steps': [ {'inputs': [('PINA',0xF7)], 'iterations': 5 }],
    'expected': [('PORTC',0x3C)],
    },   
    {'description': 'Test 9',
    'steps': [ {'inputs': [('PINA',0xF6)], 'iterations': 5 }],
    'expected': [('PORTC',0x3C)],
    },
    {'description': 'Test 10',
    'steps': [ {'inputs': [('PINA',0xF5)], 'iterations': 5 }],
    'expected': [('PORTC',0x3E)],
    },   
    {'description': 'Test 11',
    'steps': [ {'inputs': [('PINA',0xF4)], 'iterations': 5 }],
    'expected': [('PORTC',0x3E)],
    },
    {'description': 'Test 12',
    'steps': [ {'inputs': [('PINA',0xF3)], 'iterations': 5 }],
    'expected': [('PORTC',0x3E)],
    },   
    {'description': 'Test 13',
    'steps': [ {'inputs': [('PINA',0xF2)], 'iterations': 5 }],
    'expected': [('PORTC',0x3F)],
    },
    {'description': 'Test 14',
    'steps': [ {'inputs': [('PINA',0xF1)], 'iterations': 5 }],
    'expected': [('PORTC',0x3F)],
    },   
    {'description': 'Test 15',
    'steps': [ {'inputs': [('PINA',0xF0)], 'iterations': 5 }],
    'expected': [('PORTC',0x3F)],
    },
    ]
