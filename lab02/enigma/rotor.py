from enigma.baserotor import BaseRotor


class Rotor(BaseRotor):
    def __init__(self, alphabet: bytes = None):
        super().__init__(alphabet)
        self.__pos = 0

    def encrypt(self, byte: bytes) -> bytes:
        if not isinstance(byte, bytes):
            raise TypeError('byte must be of type \'bytes\'')
        if len(byte) != 1:
            raise ValueError('the length of the byte must be 1')

        pos = (int.from_bytes(byte, "big") + self.__pos) % 256
        return bytes([self.__alphabet[pos]])

    def rotate(self) -> int:
        self.__pos = (self.__pos + 1) % 256

        return self.__pos
