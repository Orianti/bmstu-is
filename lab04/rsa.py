import struct
import random
from typing import Tuple


class Rsa(object):
    def __init__(self, e: int = None, d: int = None, n: int = None, bit_count: int = 32):
        self.__bit_count = bit_count

        if e is None or d is None or n is None:
            self.__e, self.__d, self.__n = self.__generate_keys()
        else:
            self.__e, self.__d, self.__n = e, d, n

    def encrypt_file(self, src: str, dst: str) -> None:
        with open(src, 'rb') as fin, open(dst, 'w') as fout:
            data = fin.read()
            for byte in data:
                fout.write(f'{pow(byte, self.__e, self.__n)}\n')

    def decrypt_file(self, src: str, dst: str) -> None:
        with open(src, 'r') as fin, open(dst, 'wb') as fout:
            line = fin.readline()
            while line:
                fout.write(struct.pack('B', pow(int(line), self.__d, self.__n)))
                line = fin.readline()

    def get_public_key(self) -> Tuple[int, int]:
        return self.__e, self.__n

    def get_private_key(self) -> Tuple[int, int]:
        return self.__d, self.__n

    def __generate_keys(self) -> Tuple[int, int, int]:
        p = self.__random_prime()
        q = self.__random_prime()
        while p == q:
            q = self.__random_prime()

        n = p * q
        phi = (p - 1) * (q - 1)

        e = random.randint(2, phi - 1)
        while self.__gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)

        _, _, d = self.__ext_euclid(phi, e)
        if d < 0:
            d = phi + d

        return e, d, n

    def __random_prime(self) -> int:
        num = random.getrandbits(self.__bit_count)
        while not self.__miller_rabin_test(num):
            num = random.getrandbits(self.__bit_count)

        return num

    def __ext_euclid(self, a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.__ext_euclid(b % a, a)
        x = y1 - (b // a) * x1
        y = x1

        return gcd, x, y

    @staticmethod
    def __gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def __miller_rabin_test(num: int, rounds_count: int = 40) -> bool:
        if num == 2:
            return True

        if num % 2 == 0 or num % 3 == 0:
            return False

        r, s = 0, num - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(rounds_count):
            a = random.randrange(2, num - 1)
            x = pow(a, s, num)
            if x == 1 or x == num - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, num)
                if x == num - 1:
                    break
            else:
                return False
        return True
