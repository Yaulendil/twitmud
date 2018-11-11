from numpy import random as npr


def normalize(in_):
    s = sum(in_)
    return [float(i) / s for i in in_]


def choose_from(choices, q=1, probability: list = None):
    """
    Choices will be a list. Each item of the list may also be a list or a tuple.
        If an item of Choices is a tuple, it will be a list of subchoices and a list of probabilities.
    Probability will be a list of numbers and overrides a probability list packed with the choices.
    Choose Q objects from Choices and return them.
    """
    if type(choices) not in [tuple, list, range]:
        # If Choices is a single item, return it immediately.
        return choices

    prob = None
    if type(choices) == tuple:
        (choices, prob) = choices

    if not probability:
        probability = prob or [1 for _ in choices]

    choice: list = npr.choice(
        choices, size=q, replace=False, p=normalize(probability)
    ).tolist()
    for i in range(len(choice)):
        if type(choice[i]) == tuple:
            # If a tuple, 0 is list and 1 is prob; Choose
            choice[i] = choose_from(choice[i][0], 1, choice[i][1])
        while type(choice[i]) == list and len(choice[i]) > 1 and q == 1:
            # If a list of >1, choose one; Repeat
            choice[i] = choose_from(choice[i])
        while type(choice[i]) == list and len(choice[i]) == 1:
            # Remove all recursion from final result
            choice[i] = choice[i][0]
    return choice
