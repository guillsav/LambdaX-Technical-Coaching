# O(n + m) time | O(1) space
def smallest_string(char_a: str, char_b: str) -> str:

    # Build a dictionary of letters.
    letters_dict = {"a": "b", "b": "c", "c": "d", "d": "e", "e": "f", "f": "g", "g": "h", "h": "i", "i": "j", "j": "k", "k": "l", "l": "m",
                    "m": "n", "n": "o", "o": "p", "p": "q", "q": "r", "r": "s", "s": "t", "t": "u", "u": "v", "v": "w", "w": "x", "x": "y", "y": "z", "z": "a"
                    }

    if len(char_a) > 1 or len(char_b) > 1:
        smallest = smallest_string_helper(list(char_a), list(char_b))
        return smallest

    if letters_dict[char_a] == char_b:
        return char_a
    elif letters_dict[char_b] == char_a:
        return char_b
    else:
        return char_a


def smallest_string_helper(list_a: list, list_b: list) -> str:
    a_pointer = b_pointer = 0
    while a_pointer < len(list_a) and b_pointer < len(list_b):

        if len(list_a) < len(list_b):
            return ''.join(list_a)
        elif len(list_a) > len(list_b):
            return ''.join(list_b)

        a_pointer += 1
        b_pointer += 1

        return ''.join(list_a)


print(smallest_string("a", "b"))
print(smallest_string("a1", "a2"))
print(smallest_string("a10", "a2"))
