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
    for n in nums:
        # initialize the set of available numbers
        nums_set = set(range(2, n+1))

        # simulate the game
        maria_turn = True
        while nums_set:
            # find the smallest prime number
            p = min(filter(lambda x: all(x %
                    i != 0 for i in range(2, int(x**0.5)+1)), nums_set))

            # remove p and its multiples from the set
            nums_set.difference_update(range(p, n+1, p))

            # switch turns
            maria_turn = not maria_turn

        # determine the winner
        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1

    # determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
