#!/usr/bin/python3
'''
finding the pime number and removing it's multiple.
Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
'''


def isWinner(x, nums):
    """_isWinner_

    Args:
        x (integer): _description_
        nums (array): _description_

    Returns:
        None: if winner is not found
        name: if winner is found
    """
    maria_wins = 0
    ben_wins = 0
    for _ in range(x):
        for n in nums:
            nums_set = set(range(2, n+1))
            while nums_set:
                p = min(filter(lambda x: all(x %
                        i != 0 for i in range(2, int(x**0.5)+1)), nums_set))
                nums_set -= set(range(p, n+1, p))
                maria_turn = None
                maria_turn = not maria_turn
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
            return "Maria" if maria_wins > ben_wins else "Ben"\
                if ben_wins > maria_wins else None
