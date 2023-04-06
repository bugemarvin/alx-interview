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
        x (integer): number of rounds
        nums (array): numbers to choosed from

    Returns:
        None: if winner is not found
        name: if winner is found
    """
    marias_wins = 0
    bens_wins = 0
    for _ in range(x):
        for n in nums:
            # initialize the set of available numbers
            nums_set = set(range(2, n+1))

            # simulate the game
            marias_turn = True
            while nums_set:
                # find the smallest prime number
                p = min(filter(lambda x: all(x %
                        i != 0 for i in range(2, int(x**0.5)+1)), nums_set))

                # remove p and its multiples from the set
                nums_set.difference_update(range(p, n+1, p))

                # switch turns
                marias_turn = not marias_turn

            # determine the winner
            if marias_turn:
                bens_wins += 1
            else:
                marias_wins += 1

        # determine the overall winner
        if marias_wins > bens_wins:
            return "Maria"
        elif bens_wins > marias_wins:
            return "Ben"
        else:
            return None
