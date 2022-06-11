"""This module provides one class and one function to encoding and decoding string by keyword for latin alphabet.

It uses string module.

Functions:
    crypter(crypto_dict, words):

Class:
    Cipher
"""

from string import ascii_lowercase


class Cipher:
    """The Cipher provides constructor and 3 methods: crypter, encode and decode.

    Constructor uses a keyword to rearrange the letters in the alphabet.

    Encode method create a dict, where keys are letters of the latin alphabet and
    values are letters of the rearranged alphabet.

    Decode method create a dict, where keys are letters of the rearranged alphabet and
    values are letters of the latin alphabet.

    Crypter method uses dict it received from encode/decode methods and return encoded/decoded string.
    """

    def __init__(self, keyword):
        """Add the provided keyword at the begin of the latin alphabet and create alphabet_with_keyword.

        A keyword is used as the key, and it determines the letter matching of the cipher alphabet and
        the plain alphabet. Repeats of letters in the word are removed, then the cipher alphabet is
        generated with the keyword matching to A, B, C etc. until the keyword is used up.
        Whereupon the rest of the ciphertext letters are used in alphabetical order,
        excluding those already used in the key.

        Parameters:
            keyword: a string received when instance instantiated
        """
        self.alphabet_with_keyword = self._form_crypted_alphabet(keyword=keyword)

    def encode(self, words_to_encode):
        """Encode method.

        Create a dict, where keys are Latin alphabet letters and values are rearranged alphabet letters.
        Call crypter method with this dict and return its result.

        Parameters:
            words_to_encode: a words that needs to be encoded

        Returns:
            encoded words
        """
        encoding_dict = dict(zip(ascii_lowercase, self.alphabet_with_keyword))
        return self._crypt(encoding_dict, words_to_encode)

    def decode(self, words_to_decode):
        """Decode method.

        Create a dict, where keys are rearranged alphabet letters and values are Latin alphabet letters.
        Call crypter method with this dict and return its result.

        Parameters:
            words_to_decode: a words that needs to be decoded

        Returns:
            decoded words
        """
        decoding_dict = dict(zip(self.alphabet_with_keyword, ascii_lowercase))
        return self._crypt(decoding_dict, words_to_decode)

    def _crypt(self, dict_to_crypt, words):
        """Receive crypto_dict from encode/decode methods Cipher class and return encoded/decoded words.

        Recognize multiple and capitalized words, punctuation.

        Parameters:
            dict_to_crypt: a dict that received from encode/decode methods
            words: a words that need to be encoded/decoded

        Returns:
            encoded/decoded words
        """
        result_words = ""
        for char in words:
            key_char = dict_to_crypt.get(char.lower(), char)
            result_words += key_char.upper() if char.isupper() else key_char
        return result_words

    def _form_crypted_alphabet(self, keyword):
        return keyword.lower() + "".join(
            (char for char in ascii_lowercase if char not in keyword.lower()),
        )


def main():
    """Test Cipher class."""
    cipher = Cipher("crypto")
    print(cipher.encode("Hello, world!"))
    # # "Btggj vjmgp!"
    print(cipher.encode("Kojima is genius@"))
    # # # "Fjedhc dn atidsn@"

    print(cipher.decode("Fjedhc, dn atidsn"))
    # # # "Kojima, is genius"
    print(cipher.decode("Btggj vjmgp!"))
    # # "Hello, world!"


if __name__ == "__main__":
    main()
