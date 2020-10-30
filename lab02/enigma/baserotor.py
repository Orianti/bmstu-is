from secrets import SystemRandom


class BaseRotor(object):
    def __init__(self, alphabet: bytes = None):
        self.alphabet: bytes = alphabet

    @property
    def alphabet(self) -> bytes:
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, alphabet: bytes = None):
        if alphabet is None:
            self.__alphabet = self.generate_alphabet()
        else:
            if not isinstance(alphabet, bytes):
                raise TypeError('alphabet must be of type \'bytes\'')
            if len(alphabet) != 256:
                raise ValueError('the length of the alphabet must be 256')
            if len(set(alphabet)) != 256:
                raise ValueError('elements of the alphabet must be unique')

            self.__alphabet = alphabet

    @staticmethod
    def generate_alphabet() -> bytes:
        alphabet = [i for i in range(256)]
        rng = SystemRandom()
        rng.shuffle(alphabet)
        return bytes([byte for byte in alphabet])
