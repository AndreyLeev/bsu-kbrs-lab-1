from itertools import repeat


def generate_key(initial_str: str, key_word: str):
    """
    This function generates the key in a cyclic manner
    until it's length isn't equal to the length of original text

    Example:

    >>> generate_key('CRYPTOGRAPHYANDDATASECURITY', 'MOUSE')
    'MOUSEMOUSEMOUSEMOUSEMOUSEMO'
    """
    key_word_len = len(key_word)
    initial_string_len = len(initial_str)

    generated_list = list(repeat(key_word, initial_string_len // key_word_len + 1))

    return "".join(generated_list)[:initial_string_len]


def encrypt(initial_str, key_str):
    """
    This function returns the encrypted text generated with the help of the key

    Example:

    >>> encrypt('CRYPTOGRAPHYANDDATASECURITY', 'MOUSEMOUSEMOUSEMOUSEMOUSEMO')
    'OFSHXAULSTTMUFHPONSWQQOJMFM'
    """
    encrypted_text = [
        chr((ord(initial_str[i]) + ord(key_str[i])) % 26 + ord('A'))
        for i in range(len(initial_str))
    ]
    return "".join(encrypted_text)


def decrypt(encrypted_str, key_str):
    """
    This function decrypts the encrypted text and returns the original text

    Example:

    >>> decrypt('OFSHXAULSTTMUFHPONSWQQOJMFM', 'MOUSEMOUSEMOUSEMOUSEMOUSEMO')
    'CRYPTOGRAPHYANDDATASECURITY'
    """
    decrypted_text = [
        chr((ord(encrypted_str[i]) - ord(key_str[i]) + 26) % 26 + ord('A'))
        for i in range(len(encrypted_str))
    ]
    return "".join(decrypted_text)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
