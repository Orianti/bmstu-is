from typing import List

from enigma.rotor import Rotor
from enigma.reflector import Reflector


class Enigma(object):
    def __init__(self):
        self.__rotors: List[Rotor] = []
        self.__reflector = None

    def generate_config(self, rotors_count: int = 3):
        if rotors_count > 256:
            raise Exception('too many rotors')

        for _ in range(rotors_count):
            self.__rotors.append(Rotor())
        self.__reflector = Reflector()

    def set_config(self, filename: str):
        self.__rotors.clear()

        with open(filename, 'rb') as f:
            rotors_count = int.from_bytes(f.read(1), 'big')
            for _ in range(rotors_count):
                self.__rotors.append(Rotor(f.read(256)))
            self.__reflector = Reflector(f.read(256))

    def save_config(self, filename: str):
        if len(self.__rotors) == 0:
            raise Exception('no config')

        with open(filename, 'wb') as f:
            f.write(bytes([len(self.__rotors)]))
            for i in range(len(self.__rotors)):
                f.write(self.__rotors[i].alphabet)
            f.write(self.__reflector.alphabet)

    def encrypt_file(self, src: str, dst: str):
        if len(self.__rotors) == 0:
            raise Exception('no config')

        src_f = open(src, 'rb')
        dst_f = open(dst, 'wb')

        byte = src_f.read(1)
        while byte != b'':
            dst_f.write(self.encrypt(byte))
            byte = src_f.read(1)

        dst_f.close()
        src_f.close()

    def encrypt(self, byte: bytes) -> bytes:
        if not isinstance(byte, bytes):
            raise TypeError('byte must be of type \'bytes\'')
        if len(byte) != 1:
            raise ValueError('the length of the byte must be 1')

        for i in range(len(self.__rotors)):
            byte = self.__rotors[i].encrypt(byte)

        byte = self.__reflector.reflect(byte)

        for i in range(len(self.__rotors) - 1, -1, -1):
            byte = self.__rotors[i].encrypt(byte, True)

        for i in range(len(self.__rotors)):
            if self.__rotors[i].rotate() != 0:
                break

        return byte
