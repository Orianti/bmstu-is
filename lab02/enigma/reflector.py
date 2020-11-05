from enigma.base_rotor import BaseRotor


class Reflector(BaseRotor):
    def __init__(self, alphabet: bytes = None):
        super().__init__(alphabet)

    def reflect(self, byte: bytes) -> bytes:
        if not isinstance(byte, bytes):
            raise TypeError('byte must be of type \'bytes\'')
        if len(byte) != 1:
            raise ValueError('the length of the byte must be 1')

        pos = self.alphabet.index(byte)
        return bytes([self.alphabet[pos - 1 if pos % 2 else pos + 1]])
