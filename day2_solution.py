input = [l.strip() for l in open('day2_input.txt')]
strategy_one = 0
strategy_two = 0
for x in input:
    opponent,me = x.split()
    strategy_one += {'X': 1, 'Y': 2, 'Z': 3}[me]
    strategy_one += {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
            ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
            ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
            }[(opponent, me)]

    strategy_two += {'X': 0, 'Y': 3, 'Z': 6}[me]
    strategy_two += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
            ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
            ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
            }[(opponent, me)]
print(strategy_one)
print(strategy_two)