#!/bin/python3
from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone',
    'phony', 'peony', 'penny', 'benny',
    'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote',
    'shots', 'soots', 'hoots', 'hooty',
    'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if start_word == end_word:  # same word
        return [end_word]

    if _adjacent(start_word, end_word):
        return [start_word, end_word]

    f = open(dictionary_file, "r").read().split('\n')
    dictionary = []
    for word in f:
        dictionary += [word]

    stack = []
    stack.append(start_word)
    queue = deque([])
    queue.append(stack)

    while len(queue) != 0:
        dict_copy = list(dictionary)    # cant iterate + remove from same list
        ladder = queue.popleft()
        for dict_word in dict_copy:
            if _adjacent(ladder[-1], dict_word):
                if dict_word == end_word:
                    ladder.append(dict_word)
                    return ladder
                stackcopy = list(ladder)
                stackcopy.append(dict_word)
                queue.append(stackcopy)
                dictionary.remove(dict_word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 0:
        return False
    if len(ladder) == 1:
        return True
    for i in range(len(ladder)-1):
        if not _adjacent(ladder[i], ladder[i+1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    diff = 0
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1
    return diff == 1
